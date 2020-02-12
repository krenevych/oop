from abc import ABCMeta, abstractmethod
from source.P_05.Visitor_Pet.L2_Pet import Cat, Dog


##########################################
class Visitor(metaclass=ABCMeta):
    """ Базовий клас Відвідувач """

    @abstractmethod
    def visit(self, pet):
        pass


##########################################
class Veterinarian(Visitor):
    """ Клас лікар - вміє лікувати людей """

    def visit(self, pet):
        pet.treat()

    def __str__(self):
        return "Visitor = Veterinarian"


##########################################
class Scoundrel(Visitor):
    """ Клас Негідник - ображає тварин """

    def visit(self, pet):
        pet.hurt()

    def __str__(self):
        return "Visitor = Scoundrel"


##########################################
class DogTrainer(Visitor):
    """  Клас Дресирувальник домашніх тварин """

    def visit(self, pet):
        if isinstance(pet, Dog):
            pet.training()
        else:
            print("I can train only dogs")

    def __str__(self):
        return "Visitor = DogTrainer"


##########################################
class Master(Visitor):
    """ Клас Господар - вміє годувати тварину """

    def visit(self, pet):
        if isinstance(pet, Cat):
            pet.feed()
        elif isinstance(pet, Dog):
            pet.getBone()

    def __str__(self):
        return "Visitor = Master"


##########################################
class Child(Visitor):
    """ Клас Дитина - вміє вміє розважати тварин """

    def visit(self, pet):
        if isinstance(pet, Cat):
            pet.play()
        elif isinstance(pet, Dog):
            pet.walk()

    def __str__(self):
        return "Visitor = Child"
