N = int(input("N = "))
a = 1                       # a = u
for n in range(1, N+1):
    a = n * a               # a = f(n, p, a)
print("%d! = %d" % (N, a))  # виводимо на екран результат
