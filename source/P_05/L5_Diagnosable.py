from abc import ABCMeta, abstractmethod


# Інтерфейс «Діагностований»
class Diagnosable(metaclass=ABCMeta):

    @abstractmethod
    def diagnose(self):
        """ Абстрактний метод діагностувати """
        pass
