class Inimene:
    def __init__(self, n_eesnimi="tundmatu", n_perenimi="tundmatu", n_kk=1):
        self.eesnimi = n_eesnimi
        self.perenimi = n_perenimi
        self.kk = int(n_kk)

    def __del__(self):
        print("Kõike head, {0}, {1}!".format(self.eesnimi, self.perenimi))

    def tutvustus(self):
        print("Tere, olen {0} {1}".format(self.eesnimi, self.perenimi))

    def vallandatud(self):
        if self.kk == 0:
            print("\nSa oled vallandatud {0} {1} sest, teie kutsekvalifikatsioon on väiksem kui 1!\n".format(self.eesnimi, self.perenimi))
