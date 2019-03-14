from Missile import *


class MissileB(Missile):

    def utility(self, alien, increase_time, remove, killed):
        if self.hit(alien):
            if not killed:
                return increase_time + 5, True, False
            else:
                return increase_time, True, killed
        else:
            return increase_time, False, killed
