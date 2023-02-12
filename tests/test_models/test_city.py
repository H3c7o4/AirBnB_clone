#!/usr/bin/python3


"""Unittest User"""


import unittest
import os
from models.user import User
from models.base_model import BaseModel


class test_Amenity(unittest.TestCase):

    @classmethod
    def setup(self):
        self.city1 = City()
        self.city1.name = "Neverland"
        self.city1.state_id = "Peter_Pan123"

    @classmethod
    def tearDown(self):
        del self.city1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_to_dict(self):
        self.assertEqual("to_dict" in dir(self.city1), True)

    def test_functions(self):
        self.assertIsNotNone(City.__doc__)

    def save_test(self):
        self.city1.save()
        self.assertNotEqual(self.city1.created_at,
                            self.city1.updated_at)

    def test_subclass(self):
        self.assertTrue(issubclass(self.city1.__class__.BaseModel), True)

    def test_attributes(self):
        self.assertTrue("name" in self.city1.__dict__)
        self.assertTrue("created_at" in self.city1.__dict__)
        self.assertTrue("updated_at" in self.city1.__dict__)
        self.assertTrue("id" in self.city1.__dict__)
        self.assertTrue("state_id" in self.city1.__dict__)

    def test_strings(self):
        self.assertEqual(type(self.city1.name), str)
        self.assertEqual(type(self.city1.state_id), str)

if __name__ == "__main__":
    unittest.main()
