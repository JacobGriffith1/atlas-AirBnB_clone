#!/usr/bin/python3
""" unittest for file_storage.py """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os

class TestFileStorage(unittest.TestCase):
    """ test cases for FileStorage class """

    def setUp(self):
        """ set up test environment """
        self.storage = FileStorage()

        # check if the storage file exists, if it does, remove it
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def tearDown(self):
        """ tear down test environment """

        # check if the storage file exists, if it does, remove it
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_save(self):
        """ test save method """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
         # asserting that the file now exists, indicating the save operation was successful
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

if __name__ == "__main__":
    unittest.main()
