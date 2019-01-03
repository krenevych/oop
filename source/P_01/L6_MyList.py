from copy import copy, deepcopy


class MyList:
    def __init__(self):
        self.elements = []  # елементи колекції

    def print(self):
        """ Виведення елементів колекції """
        print(self.elements)


l = MyList()
l.elements.append(3)
l.elements.append(4)

l_copy = copy(l)
l_deepcopy = deepcopy(l)

print("Щойно після копіювання:")
l.print()
l_copy.print()
l_deepcopy.print()

l_copy.elements[1] = 444
print("Після інструкції l_copy.elements[1] = 444 : ")
l.print()
l_copy.print()
l_deepcopy.print()

l_deepcopy.elements[0] = 333
print("Після інструкції l_deepcopy.elements[0] = 333 : ")
l.print()
l_copy.print()
l_deepcopy.print()
