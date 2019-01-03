class Car:
    ...
    wheel_number = 4  # Статичне поле

    @staticmethod
    def getWheelNumber():
        """ Статичний метод
        :return: значення статичного поля wheel_number
        """
        return Car.wheel_number

    ...


print(Car.wheel_number)

c = Car()
print(c.wheel_number)
