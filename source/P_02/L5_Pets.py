from source.P_02.L1_Pet import Pet


class Parrot(Pet):
    """ Клас Parrot - нащадок класу Pet """

    def __init__(self, name, masterName):
        """ Конструктор

        :param name: ім'я папуги
        :param masterName: ім'я господаря
        """
        Pet.__init__(self, name) # обо'язковий виклик
                                 # конструктора базового класу
        self._masterName = masterName  # ім’я господаря

    def voice(self):
        """ Метод "голос" """
        print("Parrot says:", self._name + " horoshy!")


if __name__ == "__main__":
    # Створюємо папугу Капітана Флінта на ім'я Флінт
    flint = Parrot("Flint", "Captain Flint")
    flint.voice()
