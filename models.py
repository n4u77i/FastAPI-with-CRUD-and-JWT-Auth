import email
from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel
from typing import Optional, List

class Gender(str, Enum):
    male = 'male'
    female = 'female'
    
    
class Role(str, Enum):
    admin = 'admin'
    user = 'user'
    student = 'student'


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    email: str
    password: str
    gender: Gender
    roles: List[Role]
    
    
class UpdateUser(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    gender: Optional[Gender]
    roles: Optional[List[Role]]