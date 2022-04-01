import jwt
from passlib.hash import bcrypt
from typing import Dict

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from . import oauth2_scheme
from apps.users.schema import User, db

router = APIRouter()
JWT_SECRET = 'mytopsecret'

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        for user in db:
            if payload.get('id') == user.id:
                return payload
    except:
        raise HTTPException(
            status_code=401,
            detail='Invalid token'
        )
    

@router.post('/signup')
def register_user(user: User):
    user.hashed_password = bcrypt.hash(user.hashed_password)
    db.append(user)
    return {'Id': user.id}


@router.get('/login')
def login_user(user: Dict = Depends(get_current_user)):
    return user
    
    
@router.post('/token')
def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    for user in db:
        if form_data.username == user.first_name and form_data.password == user.hashed_password:
            token = jwt.encode(user.dict(), key=JWT_SECRET, algorithm='HS256')
            return {
                'access_token': token,
                'token_type': 'Bearer',
            }
    raise HTTPException(
                status_code=401,
                detail='Invalid username or password'
            )
            
        