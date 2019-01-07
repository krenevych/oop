from source.P_02.L1_Pet import Pet


class Cat(Pet):
    """ Клас Cat - нащадок класу Pet """

    def voice(self):
        """ Метод "голос" """
        print("Cat", self._name, "says:" , "Miu, miu, miu...")


class Dog(Pet):
    """ Клас Dog - нащадок класу Pet """

    def voice(self):
        """ Метод "голос" """
        print("Dog", self._name, "says:" , "Gav, gav, gav...!!!")


class Parrot(Pet):
    """ Клас Parrot - нащадок класу Pet """

    def voice(self):
        """ Метод "голос" """
        print("Parrot says:", self._name + " horoshy!")

if __name__ == "__main__":
    # Створюємо домашніх тварин
    # Як екземпляри відповідних класів
    my_cat = Cat("Kuzya")        # кличка кота - Кузя
    my_dog = Dog("Barbos")       # кличка собаки - Барбос
    my_parrot = Parrot("Flint")  # кличка папуги - Флінт

    # Викликаємо метод voice для кожного об’єкту
    my_cat.voice()
    my_dog.voice()
    my_parrot.voice()
