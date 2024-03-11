#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Class for serializing and deserializing instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized = {}
        for key, value in FileStorage.__objects.items():
            serialized[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                deserialized = json.load(file)
                for key, value in deserialized.items():
                    class_name = value['__class__']
                    del value['__class__']
                    if class_name == "User":
                        obj = User(**value)
                    else:
                        obj = BaseModel(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

