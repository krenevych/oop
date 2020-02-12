from abc import ABCMeta

from source.P_05.Listener.Listener import Listener


class ListenedObject(metaclass=ABCMeta):
    """ Абстрактний клас, за станами екземплярів якого можуть спостерігати об'єкти-слухачі """

    def __init__(self):
        self._listeners = []  # список підписників-слухачів

    def registerListener(self, listener: Listener):
        """ Підписує слухача на отримання повідомлень
        :param listener: слухач
        """
        self._listeners.append(listener)

    def notifyListeners(self, data):
        """ Інформує слухачів, надсилаючи кожному з них дані
        :param data: дані, що надсилаються слухачу.
        """
        for listener in self._listeners:  # кожному підписаному слухачу
            listener.onDataReceive(data)  # надсилає дані


class FileReader(ListenedObject):
    """ Файловий читач - клас-нададок класу ListenedObject.
        Його екземпляри читають заданий текстовий файл
        та надсилають підписаним слухачам по одному рядки цього файлу"""

    def __init__(self, filename):
        super().__init__()
        self._filename = filename  # ім'я файлу

    def read(self):
        with open(self._filename) as f:
            for line in f:
                self.notifyListeners(line.strip())

