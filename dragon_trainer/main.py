# Group 6 - Ella Truong & Caleb Sheets 
# Lab 7 - Inheritance - Dragon Trainer

from hero import *
from fire import *
from flying import *
from check_input import get_int_range

def main():
    #------- welcoming -------
    print('--- Dragon Trainer ---')

    player_name = input("What is your name, challenger?\n")
    hero = Hero(player_name)
    print(f"Welcome to dragon training, {hero.name.title()}.\nYou must defeat 3 dragons.")


    #------- battle begins -------
    dragons=[Dragon('Deadly Nadder',10), FireDragon('Gronckle',15), FlyingDragon('Timberjack',20)]

    while hero.hp > 0 and dragons:
        print(f"\n{hero}")

        for i,dragon in enumerate(dragons,start=1):
            print(f"{i}. {dragon}")

        # pick dragon to attack
        dragon_to_attack=get_int_range('Choose a dragon to attack: ',1,len(dragons))
        picked_dragon=dragons[dragon_to_attack-1]

        # pick weapon
        print("Attack with:\n1. Arrow (1 D12)\n2. Sword (2 D6)")
        picked_weapon=get_int_range('Enter weapon: ',1,2)
        
        # attack dragon
        if picked_weapon==1:
            print(hero.arrow_attack(picked_dragon))
        else:
            print(hero.sword_attack(picked_dragon))
        
        # remove defeated dragons
        if picked_dragon.hp<=0:
            print(f"You defeated {picked_dragon.name}!")
            dragons.remove(picked_dragon)

        # if no surviving dragons -> player wins, otherwise -> randomly pick dragon to attack hero
        if not dragons:
            print('Congratulations! You have defeated all 3 dragons, you have passed the trials.')
            break
        else:
            survivor=random.choice(dragons)
            attack=random.choice([survivor.basic_attack, survivor.special_attack])
            print(attack(hero))
        
        # hp<=0 -> hero is defeated
        if hero.hp<=0:
            print(f"You was defeated. Game over!")
            break

if __name__=='__main__':
    main()





        




                



    
        
        








