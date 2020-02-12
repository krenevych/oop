from abc import ABCMeta, abstractmethod


# Інтерфейс «Діагностований»
class Diagnosable(metaclass=ABCMeta):

    # Абстрактний метод діагностувати
    @abstractmethod
    def diagnose(self):
        pass
