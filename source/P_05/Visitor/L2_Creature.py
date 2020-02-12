from abc import ABCMeta, abstractmethod


class Creature(metaclass=ABCMeta):
    """ Абстрактний клас Істота """

    def __init__(self, name) -> None:
        self.mHealth = 100  # відсоток здоров'я
        self.mName = name   # ім'я істоти

    @abstractmethod
    def accept(self, visitor):
        """ Абстрактний метод, що використовується для реалізації шаблону проектування Відвідувач
        :param visitor: відмідувач
        """
        pass

    def treat(self):
        if self.mHealth == 100:
            print("Good health!")
        elif self.mHealth <= 0:
            print("The health is irreparable!")
        else:
            print("Health is improved!")
            self.mHealth = 100

    def spoilHealth(self):
        self.mHealth -= 10
        if self.mHealth <= 0:
            self.mHealth = 0
            print("Game over")

    def getName(self):
        return self.mName

    def __str__(self):
        return "Name: " + self.mName + "; Health = " + str(self.mHealth)


class Human(Creature):
    """ Клас людина """

    def __init__(self, name) -> None:
        super().__init__(name)
        self.mMoney = 0

    def accept(self, visitor):
        visitor.visit(self)

    def updateMoney(self, delta):
        self.mMoney += delta

    def resetMoney(self):
        money = self.mMoney;
        self.mMoney = 0
        return money

    def __str__(self):
        return super().__str__() + "; Money = " + str(self.mMoney)


class Pet(Creature):
    """ Клас домашня тварина """

    def __init__(self, name) -> None:
        super().__init__(name)
        self.mTrainingSkills = 0  # Рівень вишколу домашньої тварини

    def accept(self, visitor):
        visitor.visit(self)

    def improveSkills(self):
        self.mTrainingSkills += 10

    def __str__(self):
        return super().__str__() + "; Skills = " + str(self.mTrainingSkills)
