#!/usr/bin/python3
"""Module: file_storage"""

from models.base_model import BaseModel
from os import path
import json


class FileStorage:
    """Class FileStorage that serializes instances to a 
    JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all method returns the __object dictionary"""
        return self.__objects

    def new(self, obj):
        """Updates the class with new objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes the object to the JSON file path"""
        serial_objs = {}
        for key, obj in self.__objects.items():
            serial_objs[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serial_objs, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    obj_dict['__class__'] = class_name
                    obj = eval(class_name)(**obj_dict)
                    self.__objects[key] = obj
