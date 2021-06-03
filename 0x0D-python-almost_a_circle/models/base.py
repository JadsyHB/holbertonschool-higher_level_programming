#!/usr/bin/python3
"""
Base module
"""


import json


class Base:
    """
    Base class
    Attributes: __nb_objects
    Functions: def __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialization
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return JSON rep of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write json of list_objs into file
        """
        to_save = []
        if list_objs is not None:
            for ins in list_objs:
                to_save.append(cls.to_dictionary(ins))
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(to_save))

    @staticmethod
    def from_json_string(json_string):
        """
        return list from json rep
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        return an instance with all attributes set
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        return a list of instances
        """
        filename = cls.__name__ + ".json"
        lista = []
        try:
            with open(filename, "r") as f:
                content = cls.from_json_string(f.read())
            for i, j in enumerate(content):
                lista.append(cls.create(**content[i]))
        except:
            pass
        return lista
