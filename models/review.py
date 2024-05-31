#!/usr/bin/python3
"""Module contains class: 'Review'"""
from models.base_model import BaseModel


class Review(BaseModel):
    """User reviews of place"""
    place_id = ""
    user_id = ""
    text = ""
