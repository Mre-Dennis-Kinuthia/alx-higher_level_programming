#!/usr/bin/python3
""" Base Class Module """
import json
import csv


class Base:
    """ Base Class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the id attribute of an instance of the class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = str(cls.__name__) + ".json"
        dict_list = []
        with open(filename, "w", encoding="utf-8") as my_file:
            if list_objs is None:
                my_file.write(cls.to_json_string(dict_list))
            else:
                for obj in list_objs:
                    dict_list.append(obj.to_dictionary())

                my_file.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        classname = cls.__name__
        if classname == "Rectangle":
            dummy = cls(1, 1)
        if classname == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = str(cls.__name__) + ".json"
        instance_list = []
        try:
            with open(filename, "r", encoding="utf-8") as my_file:
                dict_from_file = cls.from_json_string(my_file.read())

                for dictionary in dict_from_file:
                    instance_list.append(cls.create(**dictionary))

                return instance_list
        except FileNotFoundError:
            return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes in CSV, similar to save_to_file(json) """
        filename = str(cls.__name__) + ".csv"
        with open(filename, "w", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            dict_list = []
            if list_objs is None:
                csv_writer.writerow(dict_list)
            else:
                for obj in list_objs:
                    for key, value in obj.to_dictionary().items():
                        dict_list.append(value)
                    csv_writer.writerow(dict_list)
                    dict_list = []

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes in CSV, similar to from_file(json) """
        filename = str(cls.__name__) + ".csv"
        instance_list = []
        if filename is None:
            return instance_list
        else:
            with open(filename, "r", encoding="utf-8") as csv_file:
                csv_reader = csv.reader(csv_file)
                if cls.__name__ == "Rectangle":
                    attrs = ['id', 'width', 'height', 'x', 'y']
                if cls.__name__ == "Square":
                    attrs = ['id', 'size', 'x', 'y']

                for row in csv_reader:
                    attr_dict = {attrs: int(row)
                                 for attrs, row in zip(attrs, row)}
                    instance_list.append(cls.create(**attr_dict))

            return instance_list
