class Iterator:
    """ Клас Ітератор """

    def __init__(self, collection):
        """ Конструктор ітератора
        :param collection: посилання на колекцію
        """
        self._collection = collection
        self._cursor = 0  # поточна позиція ітератора у колекції

    def __next__(self):
        try:
            value = self._collection[self._cursor]
            self._cursor += 1
            return value
        except IndexError:
            raise StopIteration

