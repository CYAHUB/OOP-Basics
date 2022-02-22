class Raamat:
    def __init__(self, pealkiri, autor, hind, reiting):
        self.pealkiri = pealkiri
        self.autor = autor
        self.hind = hind
        self.reiting = reiting

class Raamatupood:
    def __init__(self, nimi, reiting):
        self.nimi = nimi
        self.reiting = reiting

    def saan_lisada_raamat(self, raamat):
        self.raamat = raamat
        reiting_kogu = 0
        arv = 0
        kesk_reiting = reiting_kogu / arv

    #- meetod, mis kontrollib, kas antud raamatut saab poodi lisada. Tagastab vastavalt tõeväärtuse.

    # if there no title or author then false or shop avarage raiting is under it.
        if self.pealkiri == str and self.author == str or self.reiting <= kesk_reiting:
            print("Ei ole võimalik lisada raamatut")




    def lisa_raamat(self, raamat):
        print("no")
    #- meetod, mis lisab raamatut poodi kui see on võimalik.

    def saan_eemaldada_raamat(self, raamat):
        print("no")
    #- meetod kontrollib, kas antud raamatut saab poest eemaldada. Eemaldada saab raamatut, mis on antud poes olemas. Tagastab tõeväärtuse (True, kui raamat on poes, False, kui raamatut pole poes).

    def eemalda_raamat(self, raamat):
        print("no")
    #- meetod, mis eemaldab raamatu poest, kui see on võimalik.

    def naita_koik_raamatud(self):
        print("no")
    #- meetod, mis tagastab listi raamatutega, mis on antud poes olemas.

    def naita_raamatud_hinna_jargi(self):
        print("no")
    #- meetod, mis tagastab raamatud sorteeritud hinna alusel (odavamad enne).

    def naita_koige_populaarsem_raamat(self):
        print("no")
    #- meetod, mis tagastab listi kõige populaarsema (kõrgeima reitinguga) raamatuga (raamatutega) selles poes. Kui mitu tükki on sama reitinguga, siis on listis mitu raamatut.