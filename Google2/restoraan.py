class Restoraan:
    restoraan_nimi = ""
    soogi_tyyp = ""

    def kirjelda_restoraan(self):
        """Kirjeldab restoraani nime ja pakub soogi_tüüpi"""

        kirj_tekst = self.restoraan_nimi + " pakub " + self.soogi_tyyp
        print(kirj_tekst)

    def ava_restoraan(self):
        """Prindib restoraani nime ja avab restoraani"""
        print(self.restoraan_nimi, "on avatud!")