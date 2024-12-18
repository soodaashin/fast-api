from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import ValidationError


# Load environment variables from the .env file
load_dotenv()

class Settings(BaseSettings):
    database_hostname: str
    database_port: int  
    database_password: str
    database_name: str  
    database_username: str 
    secret_key: str
    algorithm: str
    access_token_expie_minutes: int

    class Config:
        env_file = ".env"
try:
    settings = Settings()
    print(settings.dict())

except ValidationError as e:
    # If there's a validation error, catch it and print the error details
    print("Validation error occurred while loading settings:")
    print(e.json())  # Print detailed error information