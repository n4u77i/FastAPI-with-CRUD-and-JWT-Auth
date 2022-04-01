from pydantic import BaseSettings

class CommonSettings(BaseSettings):
    APP_NAME: str = 'FastAPI with JWT Auth'
    DEBUG_MODE: bool = True
    
    
class ServerSettings(BaseSettings):
    HOST: str = '127.0.0.1'
    PORT: int = 5000
    
    
class Settings(CommonSettings, ServerSettings):
    pass