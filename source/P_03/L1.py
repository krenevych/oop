from source.P_02.L3_Pet import Pet


class Cat(Pet):
    """ Клас Cat - нащадок класу Pet """

    def voice(self):
        """ Метод "голос" """
        print("Miu...")


print("Ім'я класу     (__name__):  ", Cat.__name__)
print("Базовий клас   (__bases__): ", Cat.__bases__)
print("Атрибути класу (__dict__):  ", Cat.__dict__)
cat = Cat("Tom")    # Екземпляр класу
print("Атрибути екземпляру (__dict__): ", cat.__dict__)
