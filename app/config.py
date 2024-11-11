from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname: str
    database_post: str
    database_password: str
    database_name: str  # Fixed typo
    database_username: str 
    algorithm: str
    access_token_expie_minutes: int

    class Config:
        env_file = ".env"  # Ensure .env file exists and is in the same directory

settings = Settings()
print(settings)
