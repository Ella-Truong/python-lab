# Name: Ella Truong & Caleb Sheets
# Lab 12 - Decorator Pattern - Thanksgiving Dinner

from plate import Plate

class SmallPlate(Plate):
    def description(self):
        return 'Sturdy 10 inch paper plate '

    def area(self):
        return 78
        
    def weight(self):
        return 32

    def count(self):
        return 0

