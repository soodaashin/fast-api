#from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

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

# Initialize settings
settings = Settings()

# Check what is loaded
print(settings.dict())  # This will print all the settings as a dictionary