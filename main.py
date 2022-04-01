import uvicorn
from fastapi import FastAPI

from config import setting
from apps.users.router import router as users_router
from apps.auth.router import router as auth_router

app = FastAPI(
    title='FastAPI user auth with JWT'
)

app.include_router(users_router, tags=['Users'], prefix='')
app.include_router(auth_router, tags=['Login / Sign-up'], prefix='/auth')

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=setting.HOST,
        port=setting.PORT,
        reload=setting.DEBUG_MODE,
    )