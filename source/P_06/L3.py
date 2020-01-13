from source.P_06.L2 import benchmark


@benchmark
def Fib1(n):
    F1 = F2 = 1
    for i in range(2, n + 1):
        F2, F1 = F1, F1 + F2
    return F1


def FibRecursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return FibRecursive(n - 1) + FibRecursive(n - 2)


@benchmark
def Fib2(n):
    return FibRecursive(n)
