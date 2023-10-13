#!/usr/bin/python3
"""base_model module contains BaseModel class
being inherited"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class handles a customer review
    """

    place_id = ""
    user_id = ""
    text = ""
