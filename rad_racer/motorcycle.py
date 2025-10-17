from vehicle import Vehicle
import random

class Motorcycle(Vehicle):
    def slow(self,obs_loc):
        if obs_loc is not None:
            distance_to_obstacle=obs_loc-self._position
        else:
            distance_to_obstacle=100-self._position 

        move_distance=random.randint((3*self._speed//4)-1,(3*self._speed//4)+1)
        self._position+=move_distance
        print(f"{self._name} slowly dodges the obstacles and moves {move_distance} units!")

    def special_move(self, obs_loc):
        if obs_loc is not None:
            distance_to_obstacle=obs_loc-self._position
        else:
            distance_to_obstacle=100-self._position

        if self._energy>=15:
            self._energy-=15

            # randomly create a chance
            chance=random.random()     #return a float number in [0.0,1.0)
            if chance<0.75:
                move_distance=random.randint(2*self._speed-1,2*self._speed+1)
                if move_distance<distance_to_obstacle:
                    self._position+=move_distance
                    print(f"{self._name} pop a wheelie and moves {move_distance} units!!")
                else:
                    self._position+=distance_to_obstacle
                    print(f"{self._name} pop a wheelie and CRASHED an obstacle after moving {move_distance} units!")
            else:
                self._position+=1
                print(f"{self._name} tries to pop a wheelie, but fell over and only moved 1 unit!")
        else: 
            self._position+=1
            print(f"{self._name} tries to quickly move forward, but is all out of energy!")