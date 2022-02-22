class Konto:
    # kirjeldab panga kontot

    def __init__(self, nimi='Tundmatu isik', saldo=0):
        # klassi konstruktor. Iga konto omanik fikseeritud nimega ja konto algsaldoga.
        self.n = nimi
        self.s = saldo


    def ylekanne(self, kogus):
        # ülekanne summas "kogus" - võtakse saldost maha
        kogus = kogus
        if kogus <= self.s:
            a = self.s - kogus
            self.s = a
            print("{0} kandis {1} ja teil on alles raha {2}.".format(self.n, kogus, a))
        elif kogus > self.s:
            print("Teil pole piisavalt raha, et ülekanda.")


    def deposiit(self, kogus):
        self.s = int(self.s) + kogus
        # raha lisamine kontole vastavas koguses


    def naita_saldo(self):
        # tagastab konto saldo
        return str(self.s)


    def naita_nimi(self):
        # tagastab konto omaniku nimi
        print("Teie nimi on" + self.n)
