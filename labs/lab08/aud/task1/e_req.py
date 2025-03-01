def rec(N):
    """ Знаходження елементів послідовності використовуючи
        рекурентні співвідношення
    :param N: Номер члена послідовності, що необхідно знайти
    :return:  Знайдений член послідовності.
    """
    P = 1.0 / 9.0
    z = 9
    t = 2
    a2 = a3 = 1
    a1 = 3
    for n in range(3, N + 1):
        z = z * 3
        t = t * 2
        a3, a2, a1 = a2, a1, a3 + a2 / t
        P = P * a1 / z
    return P


N = int(input("N = "))
print(rec(N))
