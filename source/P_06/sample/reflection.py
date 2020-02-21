class Foo(object):
    r = 10

    def __init__(self, val):
        self.x = val

        def definner_hello():
                print("innerhello : " + str(self.x))

        self.innerhello = definner_hello

    def hello(self):
        print(self.x)

    def bar(self):
        print("invoked bar method")


# Без рефлексии
obj = Foo("HELLO, WORLD")


# obj.hello()
# print(hasattr(obj, "bar"))

# if hasattr(obj, "r"):
#     delattr(obj, 'r')
#
# print(hasattr(obj, "r"))
#
# def bar1(self):
#     print("invoked bar method")
#
#
# setattr(Foo, "newbar", bar1)

# print(dir(Foo))

obj2 = Foo(123)


# obj2.newbar()

# del obj2.x

# obj2.hello()
# delattr(obj2, "x")
# if hasattr(obj2, "x"):
#     obj2.hello()



# С рефлексией
# class_name = "Foo"
clazz = globals()["Foo"]
obj3 = clazz("1234")
# hello = getattr(obj3, "hello")
# hello()
hello = getattr(obj3, "innerhello")
hello()


obj7 = Foo(7)
obj8 = Foo(8)
hello7 = getattr(obj7, "innerhello")
hello8 = getattr(obj8, "innerhello")
hello7()
hello8()

# obj = clazz("HUUUUUU")
# hello = getattr(obj, "hello")
# hello()

# r = dir(obj)
#
# print(r)


# # С eval
# eval("Foo('HELLO, WORLD2!').hello()")
# print(eval("(1 + 2)"))
