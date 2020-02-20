class Pet:
    def __init__(self, name, masterName):
        """ Конструктор
        :param name: Кличка тварини
        """
        self._name = name  # приватне поле - кличка тварини
        self._masterName = masterName  # ім’я господаря

    def getType(self):
        """ Повертає тип тварини
        :return: рядок "Pet"
        """
        return "Pet"

    def getName(self):
        """ Повертає кличку тварини
        :return: кличку тварини
        """
        return self._name

    def getMasterName(self):
        """ Повертає ім'я господаря
        :return: ім'я господаря
        """
        return self._masterName

    def voice(self):
        """ Метод "голос" """
        print("I'm a base class, I say nothing...")

    def showInfo(self):
        print(self.getType() + "'s name is " + self._name)
        print(self.getType() + "'s master is " + self._masterName)
        print(self.getType() + " says: ", end="")
        self.voice()
