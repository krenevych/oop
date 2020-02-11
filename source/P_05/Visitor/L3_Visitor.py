from abc import ABCMeta, abstractmethod
from source.P_05.Visitor.L2_Creature import Human, Pet


##########################################
class Visitor(metaclass=ABCMeta):
    """
    Базовий клас Відвідувач
    """

    @abstractmethod
    def visit(self, creature):
        pass


##########################################
class Doctor(Visitor):
    """
    Клас лікар - вміє лікувати людей
    """

    def visit(self, creature):
        if isinstance(creature, Human):
            creature.treat()
        elif isinstance(creature, Pet):
            print("I can't treat pets")


##########################################
class Veterinarian(Visitor):
    """
    Клас Ветеринар - вміє лікувати тварин
    """

    def visit(self, creature):
        if isinstance(creature, Human):
            print("I can't treat humans")
        elif isinstance(creature, Pet):
            creature.treat()


##########################################
class PetTrainer(Visitor):
    """
    Клас Дресирувальник домашніх тварин
    """

    def visit(self, creature):
        if isinstance(creature, Human):
            print("I can't train humans")
        elif isinstance(creature, Pet):
            creature.improveSkills()


##########################################
class Accountant(Visitor):
    """
    Клас Бухгалтер - вміє нараховувати заробітну плату працівникам
    """

    def visit(self, creature):
        if isinstance(creature, Human):
            creature.updateMoney(100)
        elif isinstance(creature, Pet):
            creature.improveSkills()


##########################################
class Robber(Visitor):
    """
    Клас грабіжник - відбирає гроші у людей та псує здоров'я
    """

    def visit(self, creature):
        if isinstance(creature, Human):
            creature.spoilHealth()
            confiscatedMoney = creature.resetMoney()
            if confiscatedMoney == 0:
                print("Dammit!")
        elif isinstance(creature, Pet):
            print("I do not robber pets")
