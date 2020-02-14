# Діагностований Автомобіль
from source.P_05.L5_Diagnosable import Diagnosable
from source.P_05.L6_Car import Car


class DiagnosableCar(Car, Diagnosable):
    def diagnose(self):
        if self._current_mileage >= self._resource:
            return "Your car requires major repairs!"
        rest = self._resource - self._current_mileage
        rest /= self._resource
        rest *= 100
        return "Rest {}% of resource".format(rest)
