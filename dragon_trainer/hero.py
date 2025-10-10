# Group 6 - Ella Truong & Caleb Sheets 
# Lab 7 - Inheritance - Dragon Trainer

from entity import Entity
import random

class Hero(Entity):
    def sword_attack(self,dragon):
        dmg_amount=random.randint(1,6) + random.randint(1,6)
        dragon.take_damage(dmg_amount)
        return f"You slash the {dragon.name} with your sword for {dmg_amount} damage."
    
    def arrow_attack(self,dragon):
        dmg_amount=random.randint(1,12)
        dragon.take_damage(dmg_amount)
        return f"You hit the {dragon.name} with an arrow for {dmg_amount} damage."
    




