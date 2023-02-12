#!/usr/bin/python3


"""Unittest User"""


import unittest
import os
from models.user import User
from models.base_model import BaseModel


class test_Amenity(unittest.TestCase):
        @classmethod
        def setup(self):
            self.amenity1 = Amenity()
            self.amenity1.name = "Heimdall"

        @classmethod
        def tearDown(self):
            del self.amenity1
            try:
                os.remove("file.json")
            except FileNotFoundError:
                pass

        def test_to_dict(self):
            self.assertEqual("to_dict" in dir(self.amenity1), True)

        def test_functions(self):
            self.assertIsNotNone(Amenity.__doc__)

        def save_test(self):
            self.amenity1.save()
            self.assertNotEqual(self.amenity1.created_at,
                                self.amenity1.updated_at)

        def test_subclass(self):
                self.assertTrue(issubclass(self.amenity1.__class__.BaseModel),
                                True)

        def test_attributes(self):
            self.assertTrue("name" in self.amenity1.__dict__)
            self.assertTrue("created_at" in self.amenity1.__dict__)
            self.assertTrue("updated_at" in self.amenity1.__dict__)
            self.assertTrue("id" in self.amenity1.__dict__)

        def test_strings(self):
            self.assertEqual(type(self.amenity1.name), str)

if __name__ == "__main__":
    unittest.main()
