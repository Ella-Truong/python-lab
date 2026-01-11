# Name: Ella Truong & Caleb Sheets
# Lab 12 - Decorator Pattern - Thanksgiving Dinner

from plate import Plate
from check_input import get_int_range
from turkey import Turkey
from stuffing import Stuffing
from pie import Pie
from green_beans import GreenBeans
from potatoes import Potatoes
from small import SmallPlate
from large import LargePlate

def examine_plate(p: Plate):
    print(p.description())
   
    if p.area<=0 or p.weight<=0:
        if p.area <=0 and p.weight<=0:
            return("Your plate has is overloaded!")
        elif p.area<=0:
            return("Your plate isn't big enough for this much food! Your food spills over the edge.")
        else:
            return("Your plate isn't strong enough for this much food! Your food spills over the edge.") 
        return True
        
    if p.area<=20:
        hint='A tiny bit'
    elif p.area<=40:
        hint='Some'
    else:
        hint='Plenty'

    if p.weight<=6:
        weight_hint='Bending'
    elif p.weight<=12:
        weight_hint='Weak'
    else:
        weight_hint='Strong'
    
    print(f"Sturdiness: {hint}\nSpace avaiable: {weight_hint}")
    
    return False
    

def main():
    print("-- Thanksgiving Dinner --")
    print('Serve yourself as much food as you like from the buffet, but make sure that your plate will hold without spilling everywhere!')
    
    plate_choice=get_int_range('Choose a plate:\n1. Small Sturdy Plate\n2. Large Flimsy Plate\n>',1,2)
    
    foods=[Turkey(), Stuffing(), Potatoes(), GreenBeans(), Pie()]

    food_choice=get_int_range('1. Turkey\n2. Stuffing\n3. Potatoes\n4. Green Beans\n5. Pie\n6. Quit\n>',1,6)
    food_to_add=foods[food_choice-1]

    if plate_choice==1:
        if food_choice==1:
            print(food_to_add.description())
       
        

    






