from source.P_05.Visitor_Pet.L3_Visitor import *

dog = Dog("Rex")
cat = Cat("Kuzya")

visitors = [Scoundrel(), Veterinarian(), DogTrainer(), Master(), Child()]

for visitor in visitors:
    print(visitor)
    cat.accept(visitor)
    print(cat)
    print()

for visitor in visitors:
    print(visitor)
    dog.accept(visitor)
    print(dog)
    print()
