#!/usr/bin/python3
"""
Module for BaseModel class
"""
import uuid
from datetime import datetime

class BaseModel:
    """class Basemodel"""
    def __init__(self):
        """ contstructor """
        self.id = str(uuid.uuid4()) #unique id and converted to string

        self.created_at = datetime.now() #datetime when created
        self.updated_at = datetime.now() #datetime when updated

    def __str__(self):
        """

        """
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """

        """
        self.updated_at = datetime.now()
        from models import storage  # Import storage module here
        storage.save(self)

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of '__dict__' of the instance.
        Times are converted to ISO format.
        """
        dict_copy = {}

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dict_copy[key] = value.isoformat()
            else:
                if not value:
                    pass
                else:
                    dict_copy[key] = value
        dict_copy['__class__'] = self.__class__.__name__

        return dict_copy
