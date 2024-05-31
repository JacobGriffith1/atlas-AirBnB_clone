#!/usr/bin/python3
""" Module contains class: FileStorage """
import json


class FileStorage:
    """ Serializes and deserializes JSON objects """
    __file_path = file.json #string - path to the JSON file
    __objects = {} #dictionary - empty but will store all objects by <class name>.id

    def all(self):
        """ Returns the dictionary '__objects' """
        return FileStorage.__objects
    
    def new(self, obj):
        """ Sets in '__objects' the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj
