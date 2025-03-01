def reqS(N):
    """ Знаходження елементів послідовності використовуючи
        рекурентні співвідношення

    :param N: Номер члена послідовності, що необхідно знайти
    :return:  Знайдений член послідовності.
    """
    S = 1
    for n in range(2, N + 1):
        S += 1 / n
    return S


S = reqS(10)    # Знайдемо 10-й член послідовності
print("S =", S) # Виводимо результат на екран
