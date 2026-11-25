import os

from dotenv import load_dotenv

load_dotenv()  # загружает .env (если есть)


BASE_URL = "https://www.saucedemo.com/"


def username() -> str:
    user_login = os.getenv("LOGIN")
    assert user_login is not None, "Please set LOGIN environment variable"
    return user_login


def password() -> str:
    pwd = os.getenv("PASSWORD")
    assert pwd is not None, "Please set PASSWORD environment variable"
    return pwd