
import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        pass

    def test_konstruktori_asettaa_saldon_oikein(self):
        # alustetaan maksukortti, jossa on 10 euroa (1000 senttiä)
        kortti = Maksukortti(1000)
        vastaus = str(kortti)

        self.assertEqual(vastaus, "Kortilla on rahaa 10.00 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        kortti = Maksukortti(1000)
        kortti.syo_edullisesti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 7.50 euroa")



    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        kortti = Maksukortti(1000)
        kortti.syo_maukkaasti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 6.00 euroa")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_edullisesti()


        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35.00 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(20000)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150.00 euroa")

    def test_syo_maukkaasti_ei _vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_maukkaasti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_saldo_ei_negatiiviseksi(self):
        kortti = Maksukortti(-100)

        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")

    def test_minimimaara_riittaa_edulliseen(self):
        kortti = Maksukortti(250)
        kortti.syo_edullisesti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")

    def test_minimimaara_riittaa_maukkaaseen(self):
        kortti = Maksukortti(400)
        kortti.syo_maukkaasti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")
