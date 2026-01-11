# Name: Ella Truong & Caleb Sheets
# Lab 12 - Decorator Pattern - Thanksgiving Dinner

from plate_decorator import PlateDecorator

class Pie(PlateDecorator):
    def description(self):
        return super().description() + 'with Pie'
    
    def area(self):
        return super().area() - 19
    
    def weight(self):
        return super().weight() - 8
    
    def count(self):
        return super().count() + 1
    