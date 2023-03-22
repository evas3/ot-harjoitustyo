import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def kortin_saldo_alussa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10 euroa")

    def rahan_lataaminen(self):
        self.maksukortti.lataa_rahaa(self, 1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20 euroa")

    def rahan_ottaminen_saldoa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(self, 1000)
        self.assertEqual(self.maksukortti.ota_rahaa, True)

    def rahan_ottaminen_saldoa_liianvahan(self):
        self.maksukortti.ota_rahaa(self, 2000)
        self.assertEqual(self.maksukortti.ota_rahaa, False)
