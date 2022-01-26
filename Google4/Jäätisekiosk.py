class restoraan():
    def __init__(self, k_restoraani_nimi="404", k_soogi_tyyp="404", k_jäätised="404"):
        self.restoraani_nimi = k_restoraani_nimi
        self.soogi_tyyp = k_soogi_tyyp
        self.jäätised = k_jäätised

    def kirjelda_restoraan(self):
        print('Restoraan '+ str(self.restoraani_nimi) + ' pakub ' + str(self.soogi_tyyp))

    def ava_restoraan(self):
        print('Restoraan on avatud')

    def info(self):
        print(self.restoraani_nimi)
        print(self.soogi_tyyp)