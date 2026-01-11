# Name: Ella Truong & Caleb Sheets
# Lab 12 - Decorator Pattern - Thanksgiving Dinner

from plate_decorator import PlateDecorator

class Stuffing(PlateDecorator):
    def description(self):
        return super().description() + 'with Stuffing'
    
    def area(self):
        return super().area() - 18
    
    def weight(self):
        return super().weight() - 7
    
    def count(self):
        return super().count() + 1
    