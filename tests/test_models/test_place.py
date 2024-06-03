#!/usr/bin/python3
""" unittest for place.py """
import unittest
from models.place import Place


class Test_Place(unittest.TestCase):
    """ test cases for place class """

    def test_place_initialization(self):
        """ test initialization of place attributes """
        self.place = Place()
        
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_attributes(self):
        """ check that attributes are properly assigned """
        self.place = Place()

        # assign values to attributes
        self.place.city_id = "1234"
        self.place.user_id = "5678"
        self.place.name = ""
        self.place.description = "Tallest house ever"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 51.5128
        self.place.longitude = 0.1234
        self.place.amenity_ids = ["wifi", "parking"]
        # check that attributes hold assigned values
        self.assertEqual(self.place.city_id, "1234")
        self.assertEqual(self.place.user_id, "5678")
        self.assertEqual(self.place.name, "Really Tall House")
        self.assertEqual(self.place.description, "Tallest house ever")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 51.5128)
        self.assertEqual(self.place.longitude, 0.1234)
        self.assertEqual(self.place.amenity_ids, ["wifi", "parking"])

if __name__ == '__main__':
    unittest.main()
