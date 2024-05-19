#!/usr/bin/python3
""" State Module for HBNB """


from models.base_model import BaseModel


class State(BaseModel):

    """
    State class that inherits from BaseModel.

    Attributes:
        name (str): Name of the state.
    """
    name = ""
