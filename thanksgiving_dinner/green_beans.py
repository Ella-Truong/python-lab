# Name: Ella Truong & Caleb Sheets
# Lab 12 - Decorator Pattern - Thanksgiving Dinner

from plate_decorator import PlateDecorator

class GreenBeans(PlateDecorator):
    def description(self):
        return super().description() + 'with Greenn Beans'
    
    def area(self):
        return super().area() - 20
    
    def weight(self):
        return super().weight() - 3
    
    def count(self):
        return super().count() + 1
    