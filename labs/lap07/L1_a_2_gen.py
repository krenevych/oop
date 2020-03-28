def gen(x, n):
    """ Генератор """
    a = 1  # найперший член послідовності
    yield a
    for k in range(1, n + 1):
        a = x / k * a  # обчилюємо наступний член послідовності
        yield a        # повертаємо поточний член послідовності


# Головна програма
n = int(input("n = "))
x = float(input("x = "))
for el in gen(x, n):
    print(el)

