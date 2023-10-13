#!/usr/bin/python3
"""Import the base_model module
to allow inheritance"""
from models.base_model import BaseModel


class State(BaseModel):
    """class will hold states and their attributes
    """

    name = ""
