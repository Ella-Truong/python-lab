# Group 6 - Ella Truong & Caleb Sheets 
# Lab 7 - Inheritance - Dragon Trainer

from dragon import Dragon
import random

class FireDragon(Dragon):
    def __init__(self,name,hp,fire_shots=2):
        super().__init__(name,hp)
        self._fire_shots=fire_shots

    def special_attack(self, hero):
        if self._fire_shots > 0:
            dmg_amount=random.randint(6,9)
            hero.take_damage(dmg_amount)
            self._fire_shots-=1
            return f"{self.name} engulfs you in flames for {dmg_amount} damage."
        else:
            return f"{self.name} tries to spit fire at you but was all out of fire shots."
    
    def __str__(self):
        return super().__str__() + f"\n   Fire shots remaining: {self._fire_shots}"
    

