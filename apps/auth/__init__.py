import imp
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer('auth/token')