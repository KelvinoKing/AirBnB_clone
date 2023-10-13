#!/usr/bin/python3
"""Import BaseModel for City class
to inherit from it
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class defines state id and name
    """

    state_id = ""
    name = ""
