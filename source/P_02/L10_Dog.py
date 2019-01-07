from source.P_02.L9_Pet import Pet


class Dog(Pet):
    """ Клас Dog - нащадок класу Pet """

    def getType(self):
        """ Повертає тип тварини
        :return: рядок "Dog"
        """
        return "Dog"

    def voice(self):
        """ Метод "голос" """
        print("Bau-bau!")


if __name__ == "__main__":
    # Створюємо собаку
    flint = Dog("Toby", "Inspector Lestrade")
    flint.showInfo()
