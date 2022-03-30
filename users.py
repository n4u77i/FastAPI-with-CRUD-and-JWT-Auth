from uuid import uuid4
from typing import List

from models import User, Gender, Role

db: List[User] = [
    User(
        id=uuid4(),
        first_name='Jamila',
        last_name='Ahmad',
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name='Alex',
        last_name='Jones',
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]