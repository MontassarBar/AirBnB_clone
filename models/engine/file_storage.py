#!/usr/bin/python3
from models.base_model import BaseModel
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            self.__objects["{}.{}".format(
                obj.__class__.__name__, obj.id)] = obj

    def save(self):
        dicty = {}
        for key, value in self.__objects.items():
            dicty[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as x:
            json.dump(dicty, x)

    def reload(self):
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as x:
                f = json.load(x)
            for key, value in f.items():
                name = key.split('.')[0]
                self.__objects[key] = eval(name)(**value)
        except FileNotFoundError:
            pass
