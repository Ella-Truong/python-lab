# Group 6 - Ella Truong & Caleb Sheets 
# Lab 7 - Inheritance - Dragon Trainer

class Entity:
    def __init__(self,name,max_hp=50):
        self._name=name
        self._max_hp=max_hp
        self._hp=max_hp

    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    @property
    def max_hp(self):
        return self._max_hp

    def take_damage(self,dmg):
        self._hp-=dmg
        if self._hp<0:
            self._hp=0
        return self._hp
    
    def __str__(self):
        return f"{self._name.title()}: {self._hp}/{self._max_hp}"

        