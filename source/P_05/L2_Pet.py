from abc import ABCMeta, abstractmethod


class Pet(metaclass=ABCMeta):
    """ Абстрактний клас Домашня тварина """

    def __init__(self, name) -> None:
        self.name = name  # ім'я домашньої тварини
        self.isHealthy = True  # чи здорова тварина
        self.isHungry = False  # чи голодна тварина
        self.isHappy = True  # чи щаслива тварина

    @abstractmethod
    def accept(self, visitor):
        """ Абстрактний метод, що використовується для реалізації шаблону проектування Відвідувач
        :param visitor: відмідувач
        """
        pass

    def __str__(self):
        return "Name: " + self.name + ";\nHappy = " + str(self.isHappy) + ";\nHungry = " + str(
            self.isHungry) + ";\nHealthy = " + str(self.isHealthy)

    def treat(self):
        """ Лікувати тварину """
        self.isHealthy = True

    def hurt(self):
        """ Ображати тварину """
        self.isHealthy = False
        self.isHappy = False


class Cat(Pet):
    """ Клас Кіт """

    def __str__(self):
        return "== Cat ==\n" + super().__str__()

    def accept(self, visitor):
        visitor.visit(self)

    def feed(self):
        """ Годувати кота """
        self.isHungry = False

    def play(self):
        """ Пограти з котом """
        self.isHappy = True
        self.isHungry = True


class Dog(Pet):
    """ Клас Кіт """

    def __init__(self, name) -> None:
        super().__init__(name)
        self.skills = 0

    def __str__(self):
        return "== Dog ==\n" + super().__str__() + ";\nSkills = " + str(self.skills)

    def accept(self, visitor):
        visitor.visit(self)

    def getBone(self):
        """ Отримати кістку """
        self.isHungry = False

    def walk(self):
        """ Вигуляти собаку """
        self.isHappy = True
        self.isHungry = True

    def training(self):
        """ Тренувати собаку """
        self.skills += 10
        self.isHappy = False
