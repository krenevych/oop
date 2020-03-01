from source.P_06.L3_isinstance import Cat


print(hasattr(Cat, "getName"))  # пошук методу getName
print(hasattr(Cat, "_name"))    # пошук поля _name
print(hasattr(Cat, "legs"))     # пошук статичного поля legs
