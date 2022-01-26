from Google4.Jäätisekiosk import restoraan


class jaatisekiosk(restoraan):
    jaatise_balik = []

    def naita_jaatise_valik(self):
        for jk in range(1, len(self.jaatise_balik) + 1):
            print("{0}. {1}".format(jk, self.jaatise_balik[jk-1]))
    #setter
    def maara_jaatise_valik(self):
        print("Lisa jäätise variendid.")
        while(True):
            valik = input('Sisesta: ')
            if (valik == ''):
                break
            self.jaatise_balik.append(valik)