class Class7: pass
class Class8: pass
class Class9: pass
class Class6(Class7, Class8): pass
class Class4(Class6): pass
class Class5(Class6, Class9): pass
class Class2(Class4): pass
class Class3(Class5): pass
class Class1(Class2, Class3): pass


print(Class1.__mro__)
