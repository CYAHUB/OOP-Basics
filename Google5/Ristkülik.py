import random

class Ristkulik:
    def __init__(self, laius, korgus, symbol):
        self.laius = int(laius)
        self.korgus = int(korgus)
        self.symbol = str(symbol)

    def __str__(self):
        ruut = []
        for i in range(self.korgus):
            ruut.append(self.symbol * self.laius)
        ruut = '\n'.join(ruut)
        return ruut

    def __add__(self, teine_ristkulik):
        self.laius = self.laius + teine_ristkulik.laius
        self.korgus = self.korgus + teine_ristkulik.korgus
        symbol = random.randint(1, 2)
        if symbol == 1:
            self.symbol = self.symbol
        else:
            self.symbol = teine_ristkulik.symbol
        return self

kujund1 = Ristkulik(10, 3, '*')
print(kujund1)
kujund2 = Ristkulik(8, 3, 'z')
print(kujund2)
print(kujund1.__add__(kujund2))
