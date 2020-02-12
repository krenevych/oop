from abc import ABCMeta, abstractmethod


##########################################
class Listener(metaclass=ABCMeta):
    """ Інтефейс - Слухач """

    @abstractmethod
    def onDataReceive(self, line):
        pass

