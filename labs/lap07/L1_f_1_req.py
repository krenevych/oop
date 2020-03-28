eps = 0.0000000001  # точність


def exp(x):
    a = 1
    S = 1
    n = 0
    while abs(a) >= eps:
        n += 1
        a = x / n * a
        S = S + a
    return S


x = float(input("x = "))
print("exp(%f) = %f" % (x, exp(x)))
