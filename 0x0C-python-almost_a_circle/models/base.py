#!/usr/bin/python3
"""This module defines the Base class."""

import json


class Base:
    """Base class for managing id attribute in derived classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base class.

        Args:
            id (int): An optional integer ID for the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list of dict): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs : A list of instances that inherit from Base.
        """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        diclist = [obj.to_dictionary() for obj in list_objs]
        dicjsonlist = cls.to_json_string(diclist)

        with open(filename, mode="w") as file:
            json.dump(dicjsonlist, file)

    @staticmethod
    def from_json_string(json_string):
        """Return a list from the JSON string representation.

        Args:
            json_string (str): A JSON string representing a list of dictionari

        Returns:
            list: A list of dictionaries.
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set using a dictionary.

        Args:
            dictionary (dict): A dictionary containing attribute-value pairs.

        Returns:
           Base instance: Aninstanceoftheclasswithattributessetfromdictionary
            """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance
