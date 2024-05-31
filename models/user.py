#!/usr/bin/python3
"""Module contains class: 'User'"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines user credentials"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
