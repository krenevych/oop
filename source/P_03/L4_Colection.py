class Collection:
    """ Клас захищений список"""
    def __init__(self):
        self.__elements = []  # список елементів колекції

    def __setitem__(self, key, value):
        """ Встановлює значення елемента колекції
        Магічний метод - викликається при використанні
        оператора [] для присвоєння: self[key] = value
        :param key: індекс
        :param value: значення
        """
        try:
            # якщо ключ існує, змінюємо значення за ключем
            self.__elements[key] = value
        except IndexError:  # якщо ключа не існує
            #  додаємо елемент до колекції
            self.__elements.append(value)

    def __str__(self):
        """ Магічний метод перетворення об'єкту у рядок
        :return: Рядкове зображення об'єкта
        """
        return str(self.__elements)

    def __getitem__(self, key):
        """ Повертає значення елемента колекції
        Магічний метод - викликається при використанні
        оператора [] для читання: self[key]
        :param key: індекс
        :return: значення елемента колекції
        """
        try:
            return self.__elements[key]
        except IndexError:       # якщо ключа не існує
            return None          # None

    def __contains__(self, item):
        """ Перевіряє чи входить елемент item у колекцію
        Магічний метод - виклик здійснюється під час виклику
        оператора in:  item in self
        :param item: шуканий елемент
        :return: True, якщо item міститься у колекції
        """
        return item in self.__elements

    def __delitem__(self, key):
        """ Видаляє елемент з колекції
        Магічний метод - викликається при використанні
        оператора del: del self[key]
        :param key: індекс елемента, що видаляється
        """
        try:
            self.__elements.pop(key)
        except IndexError:
            pass

    def __len__(self):
        """ Повертає кількість елементів, у колекції
        Магічний метод, викликається під час виклику функції len:
        len(self)
        :return: кількість елементів у колекції
        """
        return len(self.__elements)


c = Collection()

print("Колекція :", c)
c[0] = 0  # c.__setitem__(0) - додаємо 0-й елемент
print("Колекція :", c)
c[1] = 1  # c.__setitem__(1) - додаємо 1-й елемент
print("Колекція :", c)
c[5] = 5  # c.__setitem__(5) - додаємо 2-й! елемент
print("Колекція :", c)
c[2] = 2  # c.__setitem__(2) - змінюємо 2-й елемент
print("Колекція :", c)
print()

# c = [0, 1, 2]
print(c[1])   # c.__getitem__(1)
print(c[100]) # c.__getitem__(100)
if 2 in c:    # с.__contains__(2):
    print("Елемент 2 входить до колекції!")
print()


# c = [0, 1, 2]
print("Кількість елементів =", len(c))  # c. __len__()
del c[0]   # c.__delitem__(0) - видаляємо 0-й елементprint("Колекція :", c)
print("Колекція :", c)
print("Кількість елементів =", len(c))  # c. __len__()
del c[100] # c.__delitem__(100)
print("Колекція :", c)

