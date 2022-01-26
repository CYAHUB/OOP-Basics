class restoraan():
    restoraani_nimi = 'Aken'
    soogi_tyyp = 'Error'
    avatud = 'Avatud'

    def kirjelda_restoraan(self, restoraani_nimi, soogi_tyyp):
        print('Restoraan '+ str(self.restoraani_nimi) + ' pakub ' + str(self.soogi_tyyp))

    def ava_restoraan(self, avatud):
        print('Restoraan on avatud')

    def info(self):
        print(self.restoraani_nimi)
        print(self.soogi_tyyp)
        print(self.avatud)

Restoraan = restoraan()
Restoraan.info()