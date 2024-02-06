import os

from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")

API_HOST = os.environ.get("API_HOST")
API_PORT = os.environ.get("API_PORT")

USER_API_HOST = os.environ.get("USER_API_HOST")
USER_API_PORT = os.environ.get("USER_API_PORT")

COMMENT_API_HOST = os.environ.get("COMMENT_API_HOST")
COMMENT_API_PORT = os.environ.get("COMMENT_API_PORT")

VALIDATION_API_HOST = os.environ.get("VALIDATION_API_HOST")
VALIDATION_API_PORT = os.environ.get("VALIDATION_API_PORT")