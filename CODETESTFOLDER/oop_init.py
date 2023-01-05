#!/usr/bin/python3

class Person:
    def __init__(self,name): #define name and initialize it to self
        self.name = name

    def hello(self): #define hello function
        print("Hello my name is", self.name)

p = Person("kinuthia") # call the person class

p.hello() #call the hello function

#the previous 2 lines can also be written as
#Person("Kinuthia").hello()