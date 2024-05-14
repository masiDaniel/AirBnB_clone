#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """user class inheriting from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
