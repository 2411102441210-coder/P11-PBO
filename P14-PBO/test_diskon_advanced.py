import unittest
from diskon_service import DiskonCalculator

class TestDiskonLanjut(unittest.TestCase):
    def setUp(self):
        self.calc = DiskonCalculator()

    def test_nilai_float(self):
        """Uji nilai float (diskon 33% pada 999)."""
        hasil = self.calc.hitung_diskon(999, 33)
        self.assertAlmostEqual(hasil, 669.33, places=2)

    def test_harga_nol(self):
        """Uji Edge Case (harga awal 0)."""
        hasil = self.calc.hitung_diskon(0, 10)
        self.assertEqual(hasil, 0.0)

if __name__ == '__main__':
    unittest.main()