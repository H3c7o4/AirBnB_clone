#!/usr/bin/env python3
"""
Module that Contains a class


Class State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class that inherit from BaseModel
    and defines the state of a room

    Attributes:
            name: string
    """
    name = ""
