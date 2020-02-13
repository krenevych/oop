# Базовий клас Автомобіль
class Car:

    def __init__(self, resource=100000):
        """ Конструктор

        :param resource: ресурс автомобіля до капітального ремонту
        """
        self._resource = resource
        self._current_mileage = 0  # поточний пробіг автомобіля

    def driving(self):
        self._current_mileage += 15000
