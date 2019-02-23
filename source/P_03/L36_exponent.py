eps = 0.0000000001  # точність

x = float(input("x = "))
a = 1
S = 1
n = 0
while abs(a) >= eps:
    n += 1
    a = x / n * a
    S = S + a

print("exp(%f) = %f" % (x, S))
