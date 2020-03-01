from source.P_06.L2 import Pet


class Cat(Pet):
    legs = 4
    ears = 2


if __name__ == "__main__":

    print(Cat.__bases__)

    c = Cat("Kuzya")
    print(Cat.__dict__)
    print(c.__dict__)

    print(type(c))   #   у Python 3 буде аналогічним до використання такого print(c.__class__)

    # особливості функцій isinstance та type
    print(isinstance(c, Pet))
    print(type(c) == Pet)
