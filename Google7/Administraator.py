from Google4.Admin import Kasutaja

class Admin(Kasutaja):
    def privileegid(self, ll=0, le=0, lb=0):
        self.lisamine_kasutaja = ll
        self.eemaldada_kasutaja = le
        self.blokeerida_kasutaja = lb

    def maara_privileegid(self):
        print("Lisa jäätise variendid.")
        while (True):
            valik1 = input('Kasutaja lisamine: 0 või 1')
            self.lisamine_kasutaja(valik1)
            valik2 = input('Kasutaja eemaldamine: 0 või 1')
            self.eemaldada_kasutaja(valik2)
            valik3 = input('Kasutaja blokeerimine: 0 või 1')
            self.blokeerida_kasutaja(valik3)
            break

    def naita_privileegid(self):
        print("Kasutaja lisamine: {0}".format(self.lisamine_kasutaja))
        print("Kasutajat eemaldada: {0}".format(self.eemaldada_kasutaja))
        print("Kasutajat blokeerida: {0}".format(self.blokeerida_kasutaja))
