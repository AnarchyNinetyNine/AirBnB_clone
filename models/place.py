#!/usr/bin/python3
""" Place Module for HBNB """


from models.base_model import BaseModel


class Place(BaseModel):

    """
    Place class that inherits from BaseModel.

    Attributes:
        city_id (str): The ID of the city the place is located in.
        user_id (str): The ID of the user who owns the place.
        name (str): Name of the place.
        description (str): Description of the place.
        number_rooms (int): Number of rooms in the place.
        number_bathrooms (int): Number of bathrooms in the place.
        max_guest (int): Maximum number of guests allowed.
        price_by_night (int): Price per night of the place.
        latitude (float): Latitude of the place.
        longitude (float): Longitude of the place.
        amenity_ids (list): List of Amenity IDs associated with the place.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
