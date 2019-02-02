def rec(N, x):
    """ Знаходження елементів послідовності використовуючи
        рекурентні співвідношення
    :param N: Номер члена послідовності, що необхідно знайти
    :param x: Параметр
    :return:  Знайдений член послідовності.
    """
    a = 1
    S = 1
    for n in range(1, N+1):
        a = x / n * a
        S = S + a
    return S


N = int(input("N = "))
x = float(input("x = "))
S = rec(N, x)
print("S(%d, %f) = %f", (N, x, S))
