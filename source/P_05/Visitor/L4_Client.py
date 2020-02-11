from source.P_05.Visitor.L2_Creature import Human, Pet
from source.P_05.Visitor.L3_Visitor import Doctor, Veterinarian, PetTrainer, Accountant, Robber
from random import Random

rnd = Random()

visitors = [Doctor(), Veterinarian(), PetTrainer(), Accountant(), Robber()]

creatures = []
for i in range(10):
    h = Human("Human_" + str(i))
    creatures.append(h)

for i in range(10):
    p = Pet("Pet_" + str(i))
    creatures.append(p)

for i in range(20):
    creature = creatures[rnd.randint(0, len(creatures)) - 1]
    visitor = visitors[rnd.randint(0, len(visitors)) - 1]
    creature.accept(visitor)

for creature in creatures:
    print(creature)
