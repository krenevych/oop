from abc import ABCMeta, abstractmethod


##########################################
class Observer(metaclass=ABCMeta):
    """ Інтефейс - Слухач """

    @abstractmethod
    def onDataReceive(self, line):
        pass

