from vehicle import Vehicle
import random
class Car(Vehicle):
    def special_move(self, obs_loc):
        if obs_loc is not None:
            distance_to_obstacle=obs_loc-self._position
        else:
            distance_to_obstacle=100-self._position    

        if self._energy>=15:
            self._energy-=15
            move_distance=random.randint(int(self._speed*1.5)-1,int(self._speed*1.5)+1)

            if move_distance>distance_to_obstacle:
                self._position+=distance_to_obstacle
                print(f"{self._name} uses nitro boost, but CRASHED into an obstacle after moving {move_distance} units!")
            else:
                self._position+=move_distance
                print(f"{self._name} uses nitro boost and moves {move_distance} units!!")
        else:
            self._position+=1
            print(f"{self._name} tries to quickly move forward, but is all out of energy!")