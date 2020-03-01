from source.P_06.L3_isinstance import Cat

c = Cat("Kuzya")

print(hasattr(c, "getName"))  # пошук методу getName
print(hasattr(c, "_name"))    # пошук поля _name
print(hasattr(c, "legs"))     # пошук статичного поля legs
print(hasattr(c, "unknown"))  # пошук атрибута unknown
