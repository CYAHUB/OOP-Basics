class AknadUksed:
    def __init__(self, laius, korgus):
        self.pindala = laius * korgus


class Tuba:
    def __init__(self, pikkus, laius, korgus):
        self.pikkus = pikkus
        self.laius = laius
        self.korgus = korgus
        self.aknad_uksed = []

    def lisaAkkenUks(self, laius, korgus):
        self.aknad_uksed.append(AknadUksed(laius, korgus))

    def taispind(self):
        return 2 + self.korgus * (self.pikkus + self.laius)

    def tooPind(self):
        uus_pindala = self.taispind()
        for element in self.aknad_uksed:
            uus_pindala = uus_pindala - element.pindala
        return uus_pindala

    def tapeedid(self, tp, tl):
        return int(self.tooPind() / (tp * tl)) + 1

print("Ruumi mõõtud:")
pikkus = float(input("Pikkus: "))
laius = float(input("Laius: "))
korgus = float(input("Kõrgus: "))

tuba = Tuba(pikkus, laius, korgus)

vastus = input("Kas olemas aknad/uksed? (Jah/Ei): ")
while vastus == "Jah":
    laius = float(input("Akna/Ukse laius: "))
    korgus = float(input("Akna/Ukse kõrgus: "))
    aken_uks = AknadUksed(laius, korgus)
    tuba.aknad_uksed.append(aken_uks)
    vastus = input("Kas olemas aknad/uksed? (Jah/Ei): ")

print("Tapeedi rulli mõõtud:")
tl = float(input("Tapeedi rulli laius: "))
tp = float(input("Tapeedi rulli pikkus: "))

print("Tapeedid on vaja kleepida " + str(tuba.tooPind()) + " ruutmeetrites.")
print("Tapeedi rullide arv " + str(tuba.tapeedid(tp, tl)))
