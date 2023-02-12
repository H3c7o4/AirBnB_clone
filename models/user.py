#!/usr/bin/env python3
"""
Module that contains a class


class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that inherits from Base Models

    Attributes:
             email: string - the user's email
             password: string - the user's password
             first_name: string - the user's first name
             last_name: string - the user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
