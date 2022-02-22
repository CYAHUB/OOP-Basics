from Google9.EZPZ import AknadUksed, Tuba

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