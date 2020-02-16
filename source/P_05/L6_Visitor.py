from abc import ABCMeta, abstractmethod

##########################################
class Visitor(metaclass=ABCMeta):
    """ Базовий клас Відвідувач """

    @abstractmethod
    def visitCat(self, pet):
        """ Абстрактний метод відвідати Кота """
        pass

    @abstractmethod
    def visitDog(self, pet):
        """ Абстрактний метод відвідати Собаку """
        pass


##########################################
class Veterinarian(Visitor):
    """ Клас лікар - вміє лікувати людей """

    def visitCat(self, pet):
        pet.treat()

    def visitDog(self, pet):
        pet.treat()

    def __str__(self):
        return "Visitor = Veterinarian"


##########################################
class Scoundrel(Visitor):
    """ Клас Негідник - ображає тварин """

    def visitCat(self, pet):
        pet.hurt()

    def visitDog(self, pet):
        pet.hurt()

    def __str__(self):
        return "Visitor = Scoundrel"


##########################################
class DogTrainer(Visitor):
    """  Клас Дресирувальник домашніх тварин """

    def visitCat(self, pet):
        print("I can train only dogs")

    def visitDog(self, pet):
        pet.training()

    def __str__(self):
        return "Visitor = DogTrainer"


##########################################
class Master(Visitor):
    """ Клас Господар - вміє годувати тварину """

    def visitCat(self, pet):
        pet.feed()

    def visitDog(self, pet):
        pet.getBone()

    def __str__(self):
        return "Visitor = Master"


##########################################
class Child(Visitor):
    """ Клас Дитина - вміє вміє розважати тварин """

    def visitCat(self, pet):
        pet.play()

    def visitDog(self, pet):
        pet.walk()

    def __str__(self):
        return "Visitor = Child"
