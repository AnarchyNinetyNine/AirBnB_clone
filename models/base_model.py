#!/usr/bin/python3

"""
    A module defining a base model for generic data representation:

    This module contains the `BaseModel` class, which serves as
    a foundational model for creating generic data objects with
    unique identifiers and timestamp tracking. The `BaseModel` class
    provides methods for managing object state, such as saving
    changes and converting instances to dictionary representations.

    Attributes:
        None

    Classes:
        BaseModel: A base model representing a generic data model with ID,
        creation, and update timestamps.
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """
    A base model representing a generic data model with ID, creation,
    and update timestamps.

    Attributes:
            id (str): The unique identifier for the model instance.
            created_at (datetime): The timestamp indicating when
                                   the model instance was created.
            updated_at (datetime): The timestamp indicating when
                                   the model instance was last updated.

    Methods:
            __init__(): Initializes a new BaseModel instance with a unique ID
                        and creation timestamp.
            __str__(): Returns a string representation of
                       the BaseModel instance.
            save(): Updates the `updated_at` timestamp to the current time.
            to_dict(): Converts the BaseModel instance to a dictionary
                       representation.

    """

    def __init__(self, *args, **kwargs):

        """
        Initializes a new BaseModel instance.

        Sets the `id` to a unique identifier, `created_at`
        to the current timestamp, and `updated_at` to the same value
        as `created_at`.

        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(value))
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):

        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A formatted string containing the class name, ID,
                 and attributes dictionary.

        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):

        """Updates the `updated_at` timestamp to the current time."""

        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):

        """
        Converts the BaseModel instance to a dictionary representation.

        Returns:
            dict: A dictionary containing all attributes of
                  the BaseModel instance, including class name,
                  creation timestamp (`created_at`), and update
                  timestamp (`updated_at`).

        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["created_at"] = self.created_at.isoformat()
        return obj_dict
