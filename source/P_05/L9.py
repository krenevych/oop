# Конкретний клас Людина
from source.P_05.L5 import Diagnosable
from source.P_05.L7 import Creature


class Human(Creature, Diagnosable):
    def diagnose(self):
        if self._health <= 0:
            return "you aren't alive!"
        else:
            return 'rest = {}% of life'.format(self._health)
