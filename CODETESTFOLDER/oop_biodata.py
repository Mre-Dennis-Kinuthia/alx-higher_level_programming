#!/usr/bin/python3

class person():
    def __init__(self, name, age, orientation):
        self.name = name
        self.age = age
        self.orientation = orientation

    def res(self):
        print("you are", self.name, self.age, self.orientation)

p = person("Dennis", "24", "Pan")

p.res()