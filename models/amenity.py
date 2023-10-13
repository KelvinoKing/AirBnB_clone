#!/usr/bin/python3
"""Imports base_model module to inherit the
BaseModel class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class defines the amenities in the airbnb
    """

    name = ""
