#!/usr/bin/python3


"""Unittest User"""


import unittest
import os
from models.user import User
from models.base_model import BaseModel


class test_Amenity(unittest.TestCase):

    @classmethod
    def setup(self):
        self.place1 = Place()
        self.palce1.city_id = "Neverland"
        self.place1.state_id = "Peter_Pan123"
        self.place1.user_id = "Flip"
        self.place1.name = "Shun"
        self.place1.descrip_id = "Lost city"
        self.place.street_id = 0
        self.place.amenity_id = []

    @classmethod
    def tearDown(self):
        del self.place1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_to_dict(self):
        self.assertEqual("to_dict" in dir(self.place1), True)

    def test_functions(self):
        self.assertIsNotNone(Place.__doc__)

    def save_test(self):
        self.place1.save()
        self.assertNotEqual(self.place1.created_at,
                            self.place1.updated_at)

    def test_subclass(self):
        self.assertTrue(issubclass(self.place1.__class__.BaseModel), True)

    def test_attributes(self):
        self.assertTrue("name" in self.place1.__dict__)
        self.assertTrue("created_at" in self.place1.__dict__)
        self.assertTrue("updated_at" in self.place1.__dict__)
        self.assertTrue("id" in self.place1.__dict__)
        self.assertTrue("user_id" in self.place1.__dict__)
        self.assertTrue("city_id" in self.place1.__dict__)
        self.assertTrue("state_id" in self.place1.__dict__)
        self.assertTrue("street_id" in self.place1.__dict__)
        self.assertTrue("descrip_id" in self.place1.__dict__)
        self.assertTrue("amenity_id" in self.place1.__dict__)

    def test_strings(self):
        self.assertEqual(type(self.place1.name), str)
        self.assertEqual(type(self.place1.city_id), str)
        self.assertEqual(type(self.place1.user_id), str)
        self.assertEqual(type(self.place1.state_id), str)
        self.assertEqual(type(self.place1.street_id), str)
        self.assertEqual(type(self.place1.descrip_id), str)
        self.assertEqual(type(self.place1.amenity_id), str)

if __name__ == "__main__":
    unittest.main()
