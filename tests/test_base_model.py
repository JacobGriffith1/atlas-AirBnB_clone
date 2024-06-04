#!/usr/bin/python3
""" unittest file for base_model.py"""
import unittest
import os
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for base model"""

    def test_instance_creation(self):
        """tests instantiation with no arguments"""
        model = BaseModel()
        # check that model is an instance of BaseModel
        self.assertIsInstance(model, BaseModel)
        # check that id is string
        self.assertIsInstance(model.id, str)
    
    def test_save_method(self):
        """test the save method"""
        model = BaseModel()
        self.model.old = "Old"
        self.model.save()

        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime.datetime)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_to_dict_method(self):
        """test the to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        # check that id, created_at, and updated_at are set and are strings
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'],
                         model.updated_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
