
def FactorialGenerator(n):
    yield 1  # 0! = 1
    f = 1    # поточний член послідовності
    for k in range(1, n+1):
        f *= k
        yield f

for f in FactorialGenerator(5):
    print(f)

print()

f = FactorialGenerator(5)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
