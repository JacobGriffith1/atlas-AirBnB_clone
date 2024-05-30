#!/usr/bin/python3
"""
Module for BaseModel classl
"""
import uuid
from datetime import datetime

class BaseModel:
    """classs Basemodel"""
    def __init__(self, *args, **kwargs):
        """ contstructor """
        self.id = str(uuid.uuid4()) #unique id and converted to string

        self.created_at = datetime.utcnow() #datetime when created
        self.updated_at = datetime.utcnow() #datetime when updated

if __name__ == "__main__":
    # Create an instance of BaseModel
    base_model_instance = BaseModel()

    # Print the attributes of the instance
    print(f"ID: {base_model_instance.id}")
    print(f"Created at: {base_model_instance.created_at}")
    print(f"Updated at: {base_model_instance.updated_at}")
