#!/usr/bin/python3
""" FileStorage engine for HBNB """


import json
from os import path


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):

        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):

        """
        sets in __objects the obj with key
        <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):

        """Serializes __objects to JSON file."""

        serialized_objects = {}

        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file, indent=2)

    def reload(self):

        """ Deserializes JSON file to __objects """

        try:
            if path.exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r') as file:
                    data = json.load(file)

                    """ Import classes here to avoid circular dependency """
                    from models.base_model import BaseModel
                    from models.user import User
                    from models.state import State
                    from models.city import City
                    from models.amenity import Amenity
                    from models.place import Place
                    from models.review import Review

                    """ Make classes in globals """
                    globals()['BaseModel'] = BaseModel
                    globals()['User'] = User
                    globals()['state'] = State
                    globals()['city'] = City
                    globals()['amenity'] = Amenity
                    globals()['place'] = Place
                    globals()['review'] = Review

                    for key, value in data.items():
                        class_name, obj_id = key.split('.')
                        obj_class = globals().get(class_name)
                        if obj_class:
                            obj = obj_class(**value)
                            FileStorage.__objects[key] = obj
        except Exception as e:
            pass
