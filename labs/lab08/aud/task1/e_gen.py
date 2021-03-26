def gen():
    """ Нескінченний генератор """
    P = 1.0 / 9.0
    z = 9
    t = 2
    a2 = a3 = 1
    a1 = 3
    yield P
    n = 3
    while True:
        z = z * 3
        t = t * 2
        a3, a2, a1 = a2, a1, a3 + a2 / t
        P = P * a1 / z
        n += 1
        yield P


N = int(input("N = "))
gen_object = gen()  # Створюємо екземпляр класу генератор
for i in range(N):
    print(next(gen_object))