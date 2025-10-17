from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from truck import Truck
from check_input import get_int_range
import random

def display_track(track):
    for lane in track:
        print(''.join(lane))


def display_status(vehicles):
    for vehicle in vehicles:
        print(f"{vehicle.name} [Position - {vehicle.position}, Energy - {vehicle.energy}]")
        
    

def get_next_obstacle(obstacle_list,curr_pos):
    for pos in sorted(obstacle_list):
        if pos > curr_pos:
            return pos
    return None


def update_track(track, vehicles,player_pos):
    initials=['P','C','M','T']

    for lane in track:
        for i in range(len(lane)):
            if lane[i] in initials:
                lane[i]='*'

    lane_length=len(track[0])

    for index, vehicle in enumerate(vehicles):
        if vehicle.position >= lane_length:
            pos=lane_length-1
        else:
            pos=vehicle.position
        track[index][pos]='P' if index==player_pos else vehicle.initial
        

def main():
    print('Rad Racer!')
    print("Choose a vehicle and race it down the track (player = P). Slow down for obstacles ('O') or else you'll crash!")
    print("1. Lighting Car - a fast car. Speed: 7. Special: Nitro Boost (1.5x speed).\n"
          "2. Swift Bike - a speedy motorcycle. Speed: 8. Special: Wheelie (2x speed but there's a chance you'll wipe out.)\n"
          "3. Behemoth Truck - a heavy truck. Speed: 6. Special: Ram (2x speed and it smashes through obstacles).")

    # define 3 vehicles
    vehicles=[Car('Lighting Car','C',7), Motorcycle('Swift Bike','M',8), Truck('Behemoth Truck','T',6)] 

    # choose a vehicle
    print('\n')
    vehicle_choice=get_int_range('Choose your vehicle (1-3):',1,3)
    player_index=vehicle_choice-1
    player=vehicles[player_index]

    display_status(vehicles)
    
    # update player's initial in vehicle object
    original_initials=['C','M','T']
    for i,vehicle in enumerate(vehicles):
        vehicle.initial='P' if i==player_index else original_initials[i]

    # 2D LIST FOR THE TRACK
    track_length=100
    track=[['_']*track_length for _ in range(3)]
    
    # OBSTACLES
    '''
     - randomly pick 2 positions for obstacles, excluding 0 and 99 
     - place two 'O' as obstacles on each lane
    '''
    obstacles=[]
    for lane in track:
        obs_pos=random.sample(range(1,track_length-1),2)     # a list of two random numbers
        for pos in obs_pos:
            lane[pos]='O'
        obstacles.append(obs_pos)

    for index, vehicle in enumerate(vehicles):   #vehicle now is updated with 'P' inital
        track[index][0]=vehicle.initial
    
    update_track(track, vehicles,player_index)
    display_track(track)

    # race beginning
    finished=[]
    opponents=[(i,vehicle) for i,vehicle in enumerate(vehicles) if i != player_index]

    while len(finished) < 3:
        
        # keep prompting until player finishes
        if player not in finished:
            # get player's action choice
            action_choice=get_int_range('Choose action (1. Fast, 2. Slow, 3. Special Move):',1,3)
            obs_loc=get_next_obstacle(obstacles[player_index],player.position)

            if action_choice==1:
                player.fast(obs_loc)
            elif action_choice==2:
                player.slow(obs_loc)
            elif action_choice==3:
                player.special_move(obs_loc)
            
            if player.position >= track_length-1:
                finished.append(player)
            
        # get opponent's action randomly
        for i,opponent in opponents:
            if opponent in finished:
                continue

            obs_loc=get_next_obstacle(obstacles[i],opponent.position)

            if opponent.energy<5:
                opponent.slow(obs_loc)
            else:
                move=random.choices([opponent.fast,opponent.slow,opponent.special_move], weights=[0.3,0.4,0.3])[0]
                move(obs_loc)

            if opponent.position >= track_length-1:
                finished.append(opponent)
            
        update_track(track, vehicles,player_index)
        print('\n')
        display_status(vehicles)
        display_track(track)
        
    order=['1st','2nd','3rd']
    for i, racer in enumerate(finished):
        print(f"{order[i]} place: {racer.name} [Position - {racer.position}, Energy - {racer.energy}]")

if __name__=='__main__':
    main()





        


  
        
        
        
            










        

   


    

    