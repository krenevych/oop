from source.P_03.L12_Iterable import Iterable

c = Iterable()
c.append(1)
c.append(2)
c.append(3)
c.append(4)


# Явне створення ітератора
it = iter(c)  # виклик спеціального методу __iter__()
while True:
    try:
        val = next(it) # Явно викликається функція next(it)
        print(val)
    except StopIteration: # якщо елементи скінчилися
        break             # завершуємо цикл

