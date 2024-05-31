#!/usr/bin/python3
""" Module contains class: FileStorage """
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """ Serializes and deserializes JSON objects """
    __file_path = "file.json" #string - path to the JSON file
    __objects = {} #dictionary - empty but will store all objects by <class name>.id

    def all(self):
        """ Returns the dictionary '__objects' """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in '__objects' the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes '__objects' to the JSON file
        (path: __file_path)
        """
        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dictionary, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing.)
        """
        dictionary = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City,
                    'Amenity': Amenity, 'Review': Review}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(dictionary[value['__class__']](**value))
