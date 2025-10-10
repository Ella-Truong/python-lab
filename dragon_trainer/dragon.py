# Group 6 - Ella Truong & Caleb Sheets 
# Lab 7 - Inheritance - Dragon Trainer

from entity import Entity
import random

class Dragon(Entity):
    def basic_attack(self,hero):
        dmg_amount=random.randint(2,5)
        hero.take_damage(dmg_amount)
        return f"{self.name} smashes you with its tail for {dmg_amount} damage!"
    
    def special_attack(self,hero):
        dmg_amount=random.randint(3,7)
        hero.take_damage(dmg_amount)
        return f"{self.name} slashes you withs its claw for {dmg_amount} damage!"

