from source.P_05.Listener.Listener import Listener


class FileReader:
    """ Файловий читач - клас, екземпляр якого читає заданий текстовий файл
        та надсилає підписаним слухачам по одному рядки цього файлу"""

    def __init__(self, filename):
        self._filename = filename  # ім'я файлу
        self._listeners = []       # список підписників-слухачів

    def addListener(self, listener: Listener):
        """ Підписує слухача на отримання повідомлень від

        :param listener: слухач
        """
        self._listeners.append(listener)

    def read(self):
        with open(self._filename) as f:
            for line in f:
                line = line.strip()
                for listener in self._listeners:  # кожному підписаному слухачу
                    listener.onReadLine(line)     # надсилає прочитаний з файлу рядок
