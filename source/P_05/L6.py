# Базовий клас Траспорт
class Transport:

    def __init__(self, resource=100000):
        self._resource = resource
        self._current_mileage = 0

    def driving(self):
        self._current_mileage += 15000
