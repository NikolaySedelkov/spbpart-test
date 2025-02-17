import os
from dotenv import load_dotenv

load_dotenv()

class ConfigDB:
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.getenv('DATABASE_USER')}:" \
        f"{os.getenv('DATABASE_PASSWORD')}@" \
        f"{os.getenv('DATABASE_URL')}:" \
        f"{os.getenv('DATABASE_PORT')}/" \
        f"{os.getenv('DATABASE_SCHEMA')}?" \
        f"client_encoding=utf8"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'uploads/'