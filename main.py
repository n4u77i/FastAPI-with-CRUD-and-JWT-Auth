from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException, Query, Path

from models import UpdateUser, User
from helper import update_attrs
from users import db

app = FastAPI()


@app.get('/api/v1/users')
def fetch_users():
    return db


@app.post('/api/v1/users')
def register_user(user: User):
    db.append(user)
    return {'Id': user.id}


@app.delete('/api/v1/users/{user_id}')
def delete_user(user_id: UUID = Path(None, description='ID of the user you want to delete')):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"Success": "User deleted successfully!"}
    raise HTTPException(
        status_code=404,
        detail='User with ID not found.'
    )
    
    
@app.put('/api/v1/users/{user_id}')
def update_user(
        *,
        user_id: UUID = Path(None, description='ID of the user you want to update'),
        update_user: UpdateUser
    ):
    for user in db:
        if user.id == user_id:
            update_attrs(user, update_user)
            return {"Success": user}
        
    raise HTTPException(
        status_code=404,
        detail='User with ID not found.'
    )