class InputPositiveIntException(Exception):
    def __init__(self, message, err_code, original, converted):
        """ Конструктор

        :param message: повідомлення
        :param err_code: код помилки
        :param original: введене з клавіатури значення
        :param converted: перетворене у ціле введене значення
        """
        super().__init__()
        self.message = message
        self.original_value = original
        self.converted_value = converted
        self.err_code = err_code

    def __str__(self) -> str:
        return "InputPositiveIntException: " + str(self.message)


def input_positive_int(*args, **kwargs):
    """ Обгортка навколо функції input() """
    s = input(*args, **kwargs)
    try:
        i = int(s)
    except ValueError:  # якщо введене з клавіатури не є цілим
        raise InputPositiveIntException("Non integer value", 1, s, None)

    if i < 0:  # якщо введене з клавіатури число від'ємне
        raise InputPositiveIntException("Non positive value", 2, s, i)
    return i


if __name__ == "__main__":

    while True:
        try:
            a = input_positive_int("Enter integer value (type 'exit' to finish) = ")
            print(a)
        except InputPositiveIntException as e:
            if e.err_code == 1 and e.original_value == "exit":
                break
            print(e)








