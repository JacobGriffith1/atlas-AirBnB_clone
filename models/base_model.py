#!/usr/bin/python3
"""
Module for BaseModel classl
"""
import uuid
from datetime import datetime

class BaseModel:
    """classs Basemodel"""
    def __init__(self):
        """ contstructor """
        self.id = str(uuid.uuid4()) #unique id and converted to string

        self.created_at = datetime.utcnow() #datetime when created
        self.updated_at = datetime.utcnow() #datetime when updated

    def __str__(self):
        """

        """
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """

        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """

        """
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy