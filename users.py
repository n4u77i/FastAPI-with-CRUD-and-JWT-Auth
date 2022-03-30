from uuid import uuid4
from typing import List

from models import User, Gender, Role

db: List[User] = [
    User(
        id=uuid4(),
        first_name='Jamila',
        last_name='Ahmad',
        email='jamilaahmad@gmail.com',
        password='fakehashedpassword1',
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name='Alex',
        last_name='Jones',
        email='alexjones@gmail.com',
        password='fakehashedpassword2',
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]