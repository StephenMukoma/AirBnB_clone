#!/usr/bin/python3
"""FileStorage Module"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = str(obj.__class__.__name__) + '.' + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path:__file_path)
        """
        save_dict = {}
        for key, value in FileStorage.__objects.items():
            save_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(save_dict))

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists)
        """
        if not (path.exists(FileStorage.__file_path)):
            pass
        else:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                reload_dict = json.loads(f.read())

                for obj in reload_dict.values():
                    self.new(eval(obj["__class__"])(**obj))
