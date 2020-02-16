# Діагностована Людина
from source.P_05.L7_Diagnosable import Diagnosable
from source.P_05.L9_Human import Human


class DiagnosableHuman(Human, Diagnosable):
    def diagnose(self):
        if self._health <= 0:
            return "A junk food has killed you!"
        elif self._health == 100:
            return "You have a great health!"
        else:
            return "Please, visit a doctor "
