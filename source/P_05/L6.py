# Конкретний клас Людина
from source.P_05.L2 import Diagnosable
from source.P_05.L4 import Creature


class Human(Creature, Diagnosable):
    def diagnose(self):
        if self._health <= 0:
            return "you aren't alive!"
        else:
            return 'rest = {}% of life'.format(self._health)
