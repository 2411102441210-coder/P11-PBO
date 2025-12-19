import unittest
from diskon_service import DiskonCalculator

class TestDiskon(unittest.TestCase):
    def setUp(self):
        self.calc = DiskonCalculator()

    def test_diskon_sepuluh_persen(self):
        self.assertEqual(self.calc.hitung_diskon(1000, 10), 900.0)

    def test_diskon_nol(self):
        self.assertEqual(self.calc.hitung_diskon(1000, 0), 1000.0)
