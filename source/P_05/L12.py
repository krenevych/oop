from source.P_05.L10_DiagnosableCar import DiagnosableCar
from source.P_05.L11_DiagnosableHuman import DiagnosableHuman

c = DiagnosableCar()
h = DiagnosableHuman()

for i in range(5):
    c.driving()
    h.eat("junk food")

print(c.diagnose())
print(h.diagnose())
