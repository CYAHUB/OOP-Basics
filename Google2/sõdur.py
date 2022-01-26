from random import randint
class Health():
    hp = 100
    name = 'Person name'
    def setsõdur(self, hp, name):
        self.hp = hp
        self.name = name

    def info(self):
        print(self.hp)
        print(self.name)


sõdur1 = Health()
sõdur1.setsõdur(100, 'Sõdur 1')
sõdur2 = Health()
sõdur2.setsõdur(100, 'Sõdur 2')
