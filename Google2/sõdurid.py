from random import randint
from Google2.sõdur import Health

sõdur1 = Health()
sõdur2 = Health()

while(sõdur1.hp > 0 and sõdur2.hp > 0):
    kes_loob = randint(1, 2)
    if(kes_loob == 1):
        print("Esimese lööb teist")
        sõdur2.hp = sõdur2.hp - 20
        print("Teise sõduri tervis = " + str(sõdur2.hp))
    if(kes_loob == 2):
        print("Teine loob esimest")
        sõdur1.hp = sõdur1.hp - 20
        print("Esimese sõduri tervis = " + str(sõdur1.hp))

if(sõdur1.hp == 0):
    print("Teine sõdur on võitnud")
else:
    print("Esimene sõdur on võitnud")