class restoraan():
    def __init__(self,k_restoraani_nimi,k_soogi_tyyp):
        self.restoraani_nimi = k_restoraani_nimi
        self.soogi_tyyp = k_soogi_tyyp


    def kirjelda_restoraan(self):
        print('Restoraan '+ str(self.restoraani_nimi) + ' pakub ' + str(self.soogi_tyyp))

    def ava_restoraan(self, avatud):
        print('Restoraan on avatud')

    def info(self):
        print(self.restoraani_nimi)
        print(self.soogi_tyyp)