import os
from dotenv import load_dotenv
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "resume-builder-secret")

    SQLALCHEMY_DATABASE_URI = \
        "sqlite:///" + os.path.join(BASE_DIR, "resume.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False