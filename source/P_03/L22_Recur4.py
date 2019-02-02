def req(N):
    """ Знаходження елементів послідовності використовуючи
        рекурентні співвідношення

    :param N: Номер члена послідовності, що необхідно знайти
    :return:  Знайдений член послідовності.
    """
    S = 1
    for n in range(2, N + 1):
        S = 2 * S + n ** 2
    return S


print("S(10) = ", req(10))




