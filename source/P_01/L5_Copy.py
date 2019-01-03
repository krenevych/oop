from source.P_01.L4_Triangle import Triangle

from copy import copy

t = Triangle(3, 4, 5)

t1 = copy(t)  # Створення копії об'єкта t

print("t:  ", t.a, t.b, t.c)
print("t1: ", t1.a, t1.b, t1.c)
print()

t1.a = 5
print("t:  ", t.a, t.b, t.c)
print("t1: ", t1.a, t1.b, t1.c)
