# Group 6 - Ella Truong & Caleb Sheets 
# Lab 7 - Inheritance - Dragon Trainer

from dragon import Dragon
import random

class FlyingDragon(Dragon):
    def __init__(self,name,hp,scoops=3):
        super().__init__(name,hp)
        self._swoops=scoops

    def special_attack(self,hero):
        if self._swoops > 0:
            dmg_amount=random.randint(5,8)
            hero.take_damage(dmg_amount)
            self._swoops-=1
            return f"{self.name} special swoop attack you {dmg_amount} damage."
        else:
            return f"{self.name} tries to swoop you but was all out of swoop."
        
    def __str__(self):
        return super().__str__() + f"\n   Swoop attacks remaining: {self._swoops}"