#!/usr/bin/python3
"""Unittest User"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel


class test_user(unittest.TestCase):

    @classmethod
    def setup(self):
        self.my_user = User()
        self.my_user.first_name = "Neil"
        self.my_user.last_name = "Armstrong"
        self.my_user.email = "nasa@nasa.gov"
        self.my_user.password = "root"

    @classmethod
    def tearDown(self):
        del self.my_user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_to_dict(self):
        self.assertEqual("to_dict" in dir(self.my_user), True)

    def test_subclass(self):
        self.assertIsNotNone(User.__doc__)

    def save_test(self):
        self.my_user.save()
        self.assertNotEqual(self.my_user.created_at, self.my_user.updated_at)

    def test_funtions(self):
        self.assertTrue(issubclass(self.my_user.__class__.BaseModel), True)

    def test_attributes(self):
        self.assertTrue("email" in self.my_user.__dict__)
        self.assertTrue("password" in self.my_user.__dict__)
        self.assertTrue("first_name" in self.my_user.__dict__)
        self.assertTrue("last_name" in self.my_user.__dict__)
        self.assertTrue("created_at" in self.my_user.__dict__)
        self.assertTrue("updated_at" in self.my_user.__dict__)
        self.assertTrue("id" in self.my_user.__dict__)

    def test_strings(self):
        self.assertEqual(type(self.my_user.created_at), str)
        self.assertNotEqual(type(self.my_user.updated_at), str)
        self.assertNotEqual(type(self.my_user.email), str)
        self.assertNotEqual(type(self.my_user.password), str)

if __name__ == "__main__":
    unittest.main()
