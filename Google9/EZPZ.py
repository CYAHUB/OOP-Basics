class AknadUksed:
    """AknadUksed: __init__ """
    def __init__(self, laius, korgus):
        """"""
        self.pindala = laius * korgus


class Tuba:
    """Tuba on klass mis annab võimaluse kasutada edasi programme mis on võimalik kasutada mitu korda ja salvestab endale kõik ära. V.a fail"""
    def __init__(self, pikkus, laius, korgus):
        """Annab tähtsuse pikkusele, laiusele, kõrgusele"""
        self.pikkus = pikkus
        self.laius = laius
        self.korgus = korgus
        self.aknad_uksed = []

    def lisaAkkenUks(self, laius, korgus):
        """Wat?"""
        self.aknad_uksed.append(AknadUksed(laius, korgus))

    def taispind(self):
        """
        Korrutab tais pindala.
        Esmalt liidab pikkuse ja laiuse kokku.
        Ja parast korrutab korgusega peale seda liidab 2 juurte.
        """
        return 2 + self.korgus * (self.pikkus + self.laius)

    def tooPind(self):
        """Lahutab uue pindala elementiga"""
        uus_pindala = self.taispind()
        for element in self.aknad_uksed:
            uus_pindala = uus_pindala - element.pindala
        return uus_pindala

    def tapeedid(self, tp, tl):
        """Jagab uue_pindala ja tapeedi summaga"""
        return int(self.tooPind() / (tp * tl)) + 1
