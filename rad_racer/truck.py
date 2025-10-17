from vehicle import Vehicle

class Truck(Vehicle):
    def special_move(self, obs_loc):
        if obs_loc is not None:
            distance_to_obstacle=obs_loc-self._position
        else:
            distance_to_obstacle=100-self._position
        
        if self._energy>=15:
            self._energy-=15
            move_distance=2*self._speed
            self._position+=move_distance
            print(f"{self._name} rams forward {move_distance} units!")
        else:
            self._position+=1
            print(f"{self._name} tries to quickly move forward, but is all out of energy!")