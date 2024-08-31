import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_KEY: str = os.getenv( "RGAPI_KEY" )

settings = Settings()


def get_settings():
    return settings
