#!/usr/bin/python3
"""Module contains class: 'City'"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines city and state in which it is found"""
    state_id = ""
    name = ""
