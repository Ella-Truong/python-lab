# Name: Ella Truong & Caleb Sheets
# Lab 12 - Decorator Pattern - Thanksgiving Dinner

from plate_decorator import PlateDecorator

class Turkey(PlateDecorator):
    def description(self):
        return super().description() + 'with Turkey'
    
    def area(self):
        return super().area() - 15
    
    def weight(self):
        return super().weight() - 4
    
    def count(self):
        return super().count() + 1
    