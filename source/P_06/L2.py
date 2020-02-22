class Pet:
    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name


if __name__ == "__main__":
    p = Pet("Kuzya")
    print(dir(p))
