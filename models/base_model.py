#!/usr/bin/env python3
"""
Module that contains a base model for all the other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """This class defines all common attributes/methods for other classes

    Attributes:
        id (Public): string-assign with a uuid when an instance is created
        created_at: datetime-assign with the current datetime when
                    an instance is created
        updated_at: datetime-assign with the current datetime when
                    an instance is created and it will be updated
                    every time you change your object
    """
    def __init__(self, *args, **kwargs):
        """Initializes the default attributes of the of the BaseModel object.

        Args:
            *args: unused.
            **kwargs (dict): a dictionnary containing wanted attributes.
        """
        if (kwargs is not None) and (kwargs != {}):
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Overrides the default behaviour of the __str__ method."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    # Public instance methods
    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dico = self.__dict__.copy()
        dico['__class__'] = self.__class__.__name__
        dico['created_at'] = self.created_at.isoformat()
        dico['updated_at'] = self.updated_at.isoformat()
        return dico

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects
