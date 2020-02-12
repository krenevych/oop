# Базовий клас Істота
class Creature:

    def __init__(self):
        self._health = 100

    def attend_party(self):
        self._health -= 20
        if self._health < 0:
            self._health = 0
