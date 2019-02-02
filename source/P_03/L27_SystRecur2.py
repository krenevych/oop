def rec(N, a, b):
    """ Знаходження елементів послідовності використовуючи
        рекурентні співвідношення
    :param N: Номер члена послідовності, що необхідно знайти
    :param a: Параметр
    :param b: Параметр
    :return:  Знайдений член послідовності.
    """
    S = x = 1
    for n in range(1, N + 1):
        x = a * x
        S = b * S + x


N = int(input("N = "))
a = float(input("a = "))
b = float(input("b = "))
print(rec(N, a, b))
