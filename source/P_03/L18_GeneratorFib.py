def Fibonacci():
    F2 = F1 = 1
    yield F2
    yield F1
    while True: # нескінченний цикл
        F2, F1 = F1, F1 + F2
        yield F1


n = int(input("n = "))
i = 0
for f in Fibonacci():
    print(f)
    i += 1
    if i > n:
        break
