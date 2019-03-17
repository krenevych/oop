class InputPositiveIntException(Exception):
    def __init__(self, message, err_code, original_value, converted_value):
        super().__init__()
        self.message = message
        self.original_value = original_value
        self.converted_value = converted_value
        self.err_code = err_code

    def __str__(self) -> str:
        return str(self.message)


def input_positive_int(*args, **kwargs):
    s = input(*args, **kwargs)
    try:
        i = int(s)
    except ValueError:
        raise InputPositiveIntException("Non integer value", 1, s, None)

    if i < 0:
        raise InputPositiveIntException("Non positive value", 2, s, i)
    return i


while True:
    try:
        a = input_positive_int("Enter integer value (type 'exit' to finish) = ")
        print(a)
    except InputPositiveIntException as e:
        if e.err_code == 1 and e.original_value == "exit":
            break
        print(e)








