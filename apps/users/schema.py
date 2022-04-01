from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel
from typing import Optional, List
from passlib.hash import bcrypt

class Gender(str, Enum):
    male = 'male'
    female = 'female'
    
    
class Role(str, Enum):
    admin = 'admin'
    user = 'user'
    student = 'student'


class User(BaseModel):
    id: Optional[str] = str(uuid4())
    first_name: str
    last_name: str
    middle_name: Optional[str]
    hashed_password: str
    gender: Gender
    roles: List[Role]
    
    
class UpdateUser(BaseModel):
    id: Optional[str] = None
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    hashed_password: Optional[str] = None
    gender: Optional[Gender]
    roles: Optional[List[Role]]
    
    
db: List[User] = [
    User(
        id=str(uuid4()),
        first_name='Jamila',
        last_name='Ahmad',
        hashed_password = bcrypt.hash('fakehashedpassword1'),
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=str(uuid4()),
        first_name='Alex',
        last_name='Jones',
        hashed_password = bcrypt.hash('fakehashedpassword2'),
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
    User(
        id=str(uuid4()),
        first_name='Admin',
        last_name='Admin',
        hashed_password = 'adminpass',
        gender=Gender.male,
        roles=[Role.admin]
    )
]