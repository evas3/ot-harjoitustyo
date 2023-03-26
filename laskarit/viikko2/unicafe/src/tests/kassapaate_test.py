import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_alustus_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset+self.kassa.maukkaat, 0)

    def test_edullinen_kateisella_riittavasti(self):
        palautus = self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(palautus, 260)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_maukas_kateisella_riittavasti(self):
        palautus = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(palautus, 100)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_edullinen_kateisella_vahan(self):
        palautus = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(palautus, 200)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukas_kateisella_vahan(self):
        palautus = self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(palautus, 300)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_edullinen_kortilla_riittavasti(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.60 euroa")

    def test_maukas_kortilla_riittavasti(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")

    def test_edullinen_kortilla_vahan(self):
        self.maksukortti = Maksukortti(200)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.maksukortti), False)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 2.00 euroa")

    def test_maukas_kortilla_vahan(self):
        self.maksukortti = Maksukortti(300)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.maksukortti), False)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 3.00 euroa")

    def test_kortille_rahaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100200)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 12.00 euroa")

    def test_kortille_neg_rahaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")