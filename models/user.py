#!/usr/bin/python3
"""models module to inherit the BaseModel class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Contains all user details such as name, email, etc
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
