#!/usr/bin/python3
""" unittest for file_storage.py """
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage


class Test_File_Storage(unittest.TestCase):
    """ test cases for FileStorage class """

    def test_setup(self):
        """ set up for tests """
        self.file_path = FileStorage.__file_path
        self.storage = FileStorage()
        self.test_obj = BaseModel()
        self.test_obj.id = "1234"
        self.storage.new(self.test_obj)

    def test_save(self):
        """ test that save method serializes '__objects' to the JSON file """
        
        # call save method
        storage.save()

        # check that the file was created
        self.assertTrue(os.path.exists(FileStorage.__file_path))

        # check that file contains correct data
        with open(self.file_path, 'r') as f:
            data = json.load(f)

        key = "{}.{}".format(self.test_obj.__class__.__name__, "1234")
        # check that key is in JSON file
        self.assertIn(key, data)
        # verify that data in the file matches test objects attributes
        self.assertEqual(data[key]['id'], self.test_obj.id)
        self.assertEqual(data[key]['__class__'], self.test_obj__class__.__name__)

if __name__ == '__main__':
    unittest.main()
