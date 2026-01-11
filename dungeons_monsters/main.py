# Name: Ella Truong & Caleb Sheets
# Lab 10 - Singleton - Dungeon Maze

from hero import Hero
from map import Map
from enemy import Enemy
import random
from check_input import get_int_range

def main():
    # get player's name
    user_name=input('What is your name, traveler? ')

    # create Hero object for player to print infor
    # player starts at row=0, col=0
    player=Hero(user_name)

    # construct Map object 
    game_map=Map()

    # display player's position in maze at beginning
    game_map.show_map(player.loc)
    
    while player.hp > 0:
        print(player)

        print(game_map.show_map(player.loc))

        print("\n1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit")

        user_choice=get_int_range('Enter choice: ',1,5)

        if user_choice==1:
            move=player.go_north()
        elif user_choice==2:
            move=player.go_south()
        elif user_choice==3:
            move=player.go_east()
        elif user_choice==4:
            move=player.go_west()
        else:
            print('Thank you for playing!')
            break
        
        game_map.reveal(player.loc)

        if move=='o':
            print('You cannot go that way...')

        elif move=='m':
            enemy=Enemy()
            print("You encounter",str(enemy))

            while enemy.hp>0 and player.hp>0:
                print(f"1. Attack {enemy.name}\n2. Run away")
                choice=get_int_range('Enter choice: ',1,2)

                if choice==1:
                    print(player.attack(enemy))
                    if enemy.hp > 0:
                        print(enemy.attack(player))
                    else:
                        print(f"You have slain a {enemy.name}")
                        game_map.remove_at_loc(player.loc)
                        break
                else:
                    print('You ran away!')
                    directions=[player.go_north, player.go_south, player.go_east, player.go_west]
                    random.choice(directions)()
                    game_map.reveal(player.loc)
                    break

        elif move=='n':
            print('There is nothing here...')
            game_map.remove_at_loc(player.loc)
        elif move=='s':
            print('You came back to the start of the dungeon...')
        elif move=='i':
            print("You found a Health Potion! You drink it to restore your health")
            player.heal()
            game_map.remove_at_loc(player.loc)
        elif move=='f':
            print(player)
            print(game_map.show_map(player.loc),end='\n')
            print("Congratulations! You found the exit.\n Game Over")  
            break  

    if player.hp <= 0:
        print('You die. Game over')

if __name__=='__main__':
    main()



        





    















