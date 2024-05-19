#!/usr/bin/python3
""" City Module for HBNB """


from models.base_model import BaseModel


class City(BaseModel):

    """
    City class that inherits from BaseModel.

    Attributes:
        state_id (str): The ID of the state the city belongs to.
        name (str): Name of the city.
    """
    state_id = ""
    name = ""
