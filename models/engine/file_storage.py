#!/usr/bin/python3

import json
from models.base_model import BaseModel
from os.path import exists

class FileStorage:
    """file storage for class definition"""
    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """return dictionary of classes"""

        classes = {
            "BaseModel": BaseModel
        }

        return classes
    
    def all(self):
        """returns the dictionary objects """
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in objects the obj with key """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
    
    def save(self):
        """serialize object to the json file"""
        
        obj_dict = {}
        for key in FileStorage.__objects:
            obj_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)
        return
    
    def reload(self):
        """deserialize json file"""
        obj_dict = {}
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
        for key, value in obj_dict.items():
                class_name = value["__class__"]
                obj = self.classes()[class_name](**value)
                FileStorage.__objects[key] = obj