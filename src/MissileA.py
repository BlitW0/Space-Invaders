from Missile import *


class MissileA(Missile):

    def utility(self, alien, increase_time, remove, killed):
        if self.hit(alien):
            return 0, True, True
        else:
            return increase_time, False, killed
