#!/usr/bin/python3
""" Review Module for HBNB """


from models.base_model import BaseModel


class Review(BaseModel):

    """
    Review class that inherits from BaseModel.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
