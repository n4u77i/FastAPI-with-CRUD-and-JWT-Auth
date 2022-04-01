from passlib.hash import bcrypt
from fastapi import APIRouter, HTTPException, Depends, Path

from util import update_attrs
from apps.users.schema import UpdateUser, db
from apps.auth.router import get_current_user

router = APIRouter()

@router.get('/api/v1/users')
def fetch_users(_: str = Depends(get_current_user)):
    return db


@router.delete('/api/v1/users/{user_id}')
def delete_user(
        *,
        user_id: str = Path(None, description='ID of the user you want to delete'),
        _: str = Depends(get_current_user)
    ):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"Success": "User deleted successfully!"}
    raise HTTPException(
        status_code=404,
        detail='User with ID not found.'
    )
    
    
@router.put('/api/v1/users/{user_id}')
def update_user(
        *,
        user_id: str = Path(None, description='ID of the user you want to update'),
        update_user: UpdateUser,
        _: str = Depends(get_current_user)
    ):
    for user in db:
        if user.id == user_id:
            update_user.hashed_password = bcrypt.hash(update_user.hashed_password) if update_user.hashed_password else None
            update_attrs(user, update_user)
            return {"Success": user}
        
    raise HTTPException(
        status_code=404,
        detail='User with ID not found.'
    )