#!/usr/bin/env python3
"""
Module that contains a class


class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class that inherits from Base Models

    Attributes:
            place_id: string
            user_id: string
            text: string
    """
    place_id = ""
    user_id = ""
    text = ""
