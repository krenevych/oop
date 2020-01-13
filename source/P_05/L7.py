from source.P_05.L5 import Car
from source.P_05.L6 import Human

c = Car()
h = Human()

for i in range(5):
    c.driving()
    h.attend_party()

print(c.diagnose())
print(h.diagnose())
