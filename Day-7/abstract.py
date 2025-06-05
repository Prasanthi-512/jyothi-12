from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# Concrete Class
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

# Creating an object
bike = Bike()
bike.start_engine()  # Output: Bike engine started
