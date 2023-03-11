#!/usr/bin/python3
""" File Storage Module for Serialization and Deserialization"""
import os
import json
from base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity


class FileStorage:
    """ Serializes instances to a JSON file and
        Deserializes JSON file to instances
    """

    __file_path = "file.json"  # file path name
    __object = {}  # to store all instances
    className = {'BaseModel': BaseModel,
                 'User': User,
                 'State': State,
                 'City': City,
                 'Amenity': Amenity
                 }

    def all(self):
        """ returns the dictionary __object """
        return FileStorage.__object

    def new(self, obj):
        """ setup  __objects (adding new obj to __object):
                value obj with key <obj class name>.id
        """
        key = obj.__class__.name + "." + obj.id
        FileStorage.__object[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open("FileStorage.__file_path", "w", encoding="UTF-8") as f:
            my_dict = {}
            for key, values in FileStorage.__objects.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, f, ensure_ascii=false)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.exists(FileStorage.__file_path):
            with open("FileStorage.__file_path", "r") as f:
                dict_obj_dicts = json.load(f)
            for key, value in obj_dict.items():
                obj_classname = value["__class__"]
                FileStorage.__object[key] = className[obj_classname](**value)
