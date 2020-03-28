eps = 0.0000000001  # точність


def gen_exp(x):
    a = 1
    S = 1
    n = 0
    yield S, a
    while True:
        n += 1
        a = x / n * a
        S = S + a
        yield S, a


x = float(input("x = "))
for s, a in gen_exp(x):
    if abs(a) < eps:
        print("exp(%f) = %f" % (x, s))
        break
