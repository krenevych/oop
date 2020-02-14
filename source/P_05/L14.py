from abc import ABCMeta, abstractmethod


class Pet(metaclass = ABCMeta):
    def __init__(self, name, legs, fleas):
        """ Конструктор
        :param name: Кличка тварини
        """
        self._name = name   # кличка тварини
        self._legs = legs   # кількість лап
        self._fleas = fleas # кількість бліх

    @abstractmethod
    def voice(self): # абстрактний метод
        pass         # порожня реалізація


class Cat(Pet):
    """ Клас Cat - нащадок класу Pet """

    def voice(self):
        """ Метод "голос" """
        print("Cat", self._name, "says:" , "Miu, miu, miu...")


class Dog(Pet):
    """ Клас Dog - нащадок класу Pet """

    def voice(self):
        """ Метод "голос" """
        print("Dog", self._name, "says:" , "Gav, gav, gav...!!!")


class Parrot(Pet):
    """ Клас Parrot - нащадок класу Pet """

    def voice(self):
        """ Метод "голос" """
        print("Parrot says:", self._name + " horoshy!")

