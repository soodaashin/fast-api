from pydantic_settings import BaseSettings, SettingsConfigDict

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

settings = Settings()

# Print the settings to verify the values are correctly loaded
print("Settings Loaded:")
print(f"Database Hostname: {settings.database_hostname}")
print(f"Database Port: {settings.database_port}")
print(f"Database Password: {settings.database_password}")
print(f"Database Name: {settings.database_name}")
print(f"Database Username: {settings.database_username}")
print(f"Secret Key: {settings.secret_key}")
print(f"Algorithm: {settings.algorithm}")
print(f"Access Token Expiry Minutes: {settings.access_token_expie_minutes}")