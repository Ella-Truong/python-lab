# Name: Ella Truong & Caleb Sheets
# Lab 10 - Singleton - Dungeon Maze

from entity import Entity
from enemy import Enemy
from map import Map
import random

class Hero(Entity):
    def __init__(self,name):
        super().__init__(name,max_hp=25)
        self._loc=[0,0]       #[row,col] - starting location
    
    @property
    def loc(self):
        return self._loc
    
    def attack(self,entity):
        if isinstance(entity,Enemy):
            dmg_amount=random.randint(2,5)
            entity.take_damage(dmg_amount)
            return f"{self._name} attack {entity.name} for {dmg_amount} damage."
        else:
            raise TypeError('Hero can only attack enemy.')
    
    def go_north(self):
        row, col=self._loc
        if row>0:
            self._loc[0]-=1
            return Map()._map[self._loc[0]][col]
        return 'o'
    
    def go_south(self):
        row, col=self._loc
        if row<len(Map()._map)-1:
            self._loc[0]+=1
            return Map()._map[self._loc[0]][col]
        return 'o'
    
    def go_east(self):
        row, col=self._loc
        if col<len(Map()._map[0])-1:
            self._loc[1]+=1
            return Map()._map[row][self._loc[1]]
        return 'o'
    
    def go_west(self):
        game_map=Map()
        row, col=self._loc
        if col>0:
            self._loc[1]-=1
            return Map()._map[row][self._loc[1]]
        return 'o'









