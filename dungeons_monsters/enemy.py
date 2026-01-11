# Name: Ella Truong & Caleb Sheets
# Lab 10 - Singleton - Dungeon Maze

from entity import Entity
import random

class Enemy(Entity):
    def __init__(self):
        name=random.choice(['Goblin', 'Vampire', 'Ghoul', 'Skeleton', 'Zombie'])
        max_hp=random.randint(4,8)
        super().__init__(name,max_hp)
    
    def attack(self,entity):
        dmg_amount=random.randint(1,4)
        entity.take_damage(dmg_amount)
        return f"{self.name} attacks {entity.name} for {dmg_amount} damage."
