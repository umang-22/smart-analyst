from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://smart:smart@localhost:5432/smart_analyst"

    class Config:
        env_file = ".env"

settings = Settings()
