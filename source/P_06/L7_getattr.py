from source.P_06.L3_isinstance import Cat

c = Cat("Kuzya")

method1 = getattr(Cat, "getName")  # метод getName класу Cat
method2 = getattr(c, "getName")    # метод getName об'єкту c

print(method1)
print(method2)


print(method1(c))  # рефлексивний виклик методу getName об'єкту c


