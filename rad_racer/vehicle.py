import abc
from abc import ABC
import random
from check_input import get_int_range

class Vehicle(ABC):
    def __init__(self,name,initial,speed):
        self._name=name
        self._initial=initial
        self._speed=speed
        self._position=0
        self._energy=100
    
    @property
    def name(self):
        return self._name

    @property
    def initial(self):
        return self._initial

    @initial.setter
    def initial(self, value):
        self._initial=value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position=value

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        self._energy=value

    def fast(self,obs_loc):
        #calculate distance to obstacle, obs_loc can be integer or None if there is no obstacle
        if obs_loc is not None:
            distance_to_obstacle=obs_loc-self._position
        else:
            distance_to_obstacle=100-self._position      # no obstacle -> use distance to end of track

        if self._energy>=5:
            move_distance=random.randint(self._speed-1,self._speed+1)
            self._energy-=5
            if move_distance<distance_to_obstacle:
                self._position+=move_distance
                print(f"{self._name} quickly moves {move_distance} units!")
            else:
                self._position+=distance_to_obstacle
                print(f"{self._name} CRASHED into an obstacle!")
        else:
            self._position+=1
            print(f"{self._name} tries to quickly move forward, but is all out of energy!")


    def slow(self,obs_loc):
        move_distance=random.randint((self._speed)//2-1,(self._speed)//2+1)
        self._position+=move_distance
        print(f"{self._name} slowly moves {move_distance} units!")
    
    @abc.abstractmethod
    def special_move(self,obs_loc):
        pass

    def __str__(self):
        return f"{self._name}, {self._position}, {self._energy}"



    
    




    










