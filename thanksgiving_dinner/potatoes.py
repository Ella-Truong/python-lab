# Name: Ella Truong & Caleb Sheets
# Lab 12 - Decorator Pattern - Thanksgiving Dinner

from plate_decorator import PlateDecorator

class Potatoes(PlateDecorator):
    def description(self):
        return super().description() + 'with Potatoes'
    
    def area(self):
        return super().area() - 18
    
    def weight(self):
        return super().weight() - 6
    
    def count(self):
        return super().count() + 1
    