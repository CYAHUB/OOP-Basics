from random import randint
from Google4.Sodur import Sodur

armee_1 = []
armee_2 = []

for kord in range(20):
    millisse_armeese = randint(1, 2)
    sodur = Sodur(millisse_armeese)
    if millisse_armeese == 1:
        armee_1.append(sodur)
    if millisse_armeese == 2:
        armee_2.append(sodur)

print("Armee 1")
for sodur in armee_1:
    sodur.info()
print("======================")
print("Armee 2")
for sodur in armee_2:
    sodur.info()
