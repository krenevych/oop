class Car:

    wheel_number = 4  # Статичне поле

    @staticmethod
    def getWheelNumber():
        """ Статичний метод
        :return: значення статичного поля wheel_number
        """
        return Car.wheel_number

if __name__ == "__main__":
    # Звернення до статичного поля через ім'я класу
    print(Car.wheel_number)

    c = Car()
    # Звернення до статичного поля через екземпляр класу
    print(c.wheel_number)

    # Виклик статичного методу через ім'я класу
    print(Car.getWheelNumber())

    # Виклик статичного методу через екземпляр класу
    print(c.getWheelNumber())