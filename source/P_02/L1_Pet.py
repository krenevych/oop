class Pet:
    def __init__(self, name):
        """ Конструктор
        :param name: Кличка тварини
        """
        self._name = name  # приватне поле - кличка тварини

    def getName(self):
        """ Повертає кличку тварини
        :return: кличку тварини
        """
        return self._name