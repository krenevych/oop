from source.P_05.L8_DiagnosableCar import DiagnosableCar
from source.P_05.L9_DiagnosableHuman import DiagnosableHuman

c = DiagnosableCar()
h = DiagnosableHuman()

for i in range(5):
    c.driving()
    h.eat("junk food")

print(c.diagnose())
print(h.diagnose())
