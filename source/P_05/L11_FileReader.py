from abc import ABCMeta

from source.P_05.L12_Observer import Observer


class Subject(metaclass=ABCMeta):
    """ Абстрактний клас, що визначає методи для додавання та сповіщення спостерігачів """

    def __init__(self):
        self._observers = []  # список підписників-спостерігачів

    def register_observers(self, observer: Observer):
        """ Підписує спостерігача на отримання повідомлень
        :param observer: спостерігач
        """
        self._observers.append(observer)

    def notify_observers(self, data):
        """ Інформує спостерігачів, надсилаючи кожному з них дані
        :param data: дані, що надсилаються спостерігачу.
        """
        for observer in self._observers:  # кожному підписаному спостерігачу
            observer.onDataReceive(data)  # надсилає дані


class FileReader(Subject):
    """ Файловий читач - конкретна реалізація класу Subject.
        Його екземпляри читають заданий текстовий файл
        та надсилають підписаним спостерігачам по одному рядки цього файлу """

    def __init__(self, filename):
        super().__init__()
        self._filename = filename  # ім'я файлу

    def read(self):
        with open(self._filename) as f:
            for line in f:
                self.notify_observers(line.strip())

