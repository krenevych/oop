from source.P_03.L12_Iterable import Iterable

c = Iterable()
c.append(1)
c.append(2)
c.append(3)
c.append(4)

# c = [1, 2, 3, 4]
# Створення першого ітератора для колекції c
it1 = iter(c)
# Створення другого ітератора для колекції c
it2 = iter(c)
print(next(it1))  # наступний елемент для ітератора it1
print(next(it2))  # наступний елемент для ітератора it2
print(next(it1))  # наступний елемент для ітератора it1
print(next(it2))  # наступний елемент для ітератора it2

