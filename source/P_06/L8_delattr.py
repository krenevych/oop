class A:
    static_property = 1  # статичне поле

    def __init__(self, prop):
        self.property = prop  # локальне поле

    def method(self):      # тетод
        pass


if __name__ == "__main__":
    a = A(1)
    print(hasattr(a, "property"))
    delattr(a, "property")
    print(hasattr(a, "property"))


    # delattr(a, "static_property")  #  породжується помилка AttributeError
    # delattr(a, "method")           #  породжується помилка AttributeError

    delattr(A, "static_property") # видалення атрибуту static_property у класу A
    delattr(A, "method")          # видалення атрибуту method у класу A
    # перевірка наявності атрибутів у екземплярі класу A
    print(hasattr(a, "static_property"))
    print(hasattr(a, "method"))
