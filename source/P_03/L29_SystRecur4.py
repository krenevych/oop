def rec(N):
    """ Знаходження елементів послідовності використовуючи
        рекурентні співвідношення
    :param N: Номер члена послідовності, що необхідно знайти
    :return:  Знайдений член послідовності.
    """
    S = 0.5
    a = b = 1
    for n in range(1, N + 1):
        a, b = a * b, a + b
        S = S + a / (1 + b)
    return S


N = int(input("N = "))
print(rec(N))
