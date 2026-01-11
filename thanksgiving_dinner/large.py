# Name: Ella Truong & Caleb Sheets
# Lab 12 - Decorator Pattern - Thanksgiving Dinner

from plate import Plate

class LargePlate(Plate):
    def description(self):
        return 'Flimsy 12 inch paper plate '

    def area(self):
        return 113
        
    def weight(self):
        return 24

    def count(self):
        return 0

