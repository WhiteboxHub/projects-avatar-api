from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    port: int

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        extra = "allow"

settings = Settings()
