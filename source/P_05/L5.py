# Конкретний клас Автомобіль
from source.P_05.L2 import Diagnosable
from source.P_05.L3 import Transport


class Car(Transport, Diagnosable):
    def diagnose(self):
        if self._current_mileage >= self._resource:
            return "your car requires major repairs"
        rest = self._resource - self._current_mileage
        rest /= self._resource
        rest *= 100
        return "rest {}% of resource".format(rest)
