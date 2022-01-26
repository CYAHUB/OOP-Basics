class Kasutajad:
    def __init__(self, eesnimi="tundmatu", perenimi="tundmatu", vanus=0, parool="qwerty"):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.vanus = vanus
        self.parool = parool

    def kirjelda_kasutaja(self):
        print("Kasutaja andmed: ")
        print("Eesnimi: " + str(self.eesnimi))
        print("Perenimi: " + str(self.perenimi))
        print("Vanus: " + str(self.vanus))


    def tervita_kasutaja(self):
        print("Tervist {0} {1}".format(self.eesnimi, self.perenimi) + " ja oled " + str(self.vanus) + " aastane.\n")
