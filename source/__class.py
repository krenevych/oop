class Collection:
    ...

    def __iter__(self):
        return self  # Повертаємо об'єкт для якого
        #  визначено метод __next__(self)

    def __next__(self):
        try:
            # по черзі повертаємо елементи колекції
            cur = self.__current
            self.__current += 1
            return self.__elements[cur]
        except IndexError:       # якщо таке виключення, то
                                 #  у колекції скінчилися елементи
            raise StopIteration # ініціюємо виключення


collection = [1, 2, 3, 4]

for element in collection:
    print(element)
