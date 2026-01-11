# Name: Ella Truong & Caleb Sheets
# Lab 10 - Singleton - Dungeon Maze

import abc

class Entity(abc.ABC):
    def __init__(self,name,max_hp=25):
        self._name=name
        self._hp=max_hp
        self._max_hp=max_hp
    
    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    def take_damage(self,dmg):
        self._hp-=dmg
        if self._hp<0:
            self._hp=0
        return self._hp
    
    def heal(self):
        self._hp=self._max_hp
        return self._hp
    
    def __str__(self):
        return f"{self._name}\nHP: {self._hp}/{self._max_hp}"
    
    @abc.abstractmethod
    def attack(self, entity):
        pass



