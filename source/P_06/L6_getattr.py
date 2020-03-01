from source.P_06.L3_isinstance import Cat

c = Cat("Kuzya")

n = getattr(c, "_name")  # поле _name об'єкту c
print(n)

l = getattr(c, "legs")   # статичне поле legs об'єкту c
print(l)

method = getattr(c, "getName")  # метод getName об'єкту c
print(method())    # рефлексивний виклик методу getName об'єкту c


