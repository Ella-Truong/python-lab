# Name: Ella Truong & Caleb Sheets
# Lab 12 - Decorator Pattern - Thanksgiving Dinner

import abc
from plate import Plate

class PlateDecorator(abc.ABC, Plate):
    def __init__(self, p: Plate):
        self._plate=p
    
    def description(self):
        return self._plate.description()

    def area(self):
        return self._plate.area()
        
    def weight(self):
        return self._plate.weight()

    def count(self):
        return self._plate.count()