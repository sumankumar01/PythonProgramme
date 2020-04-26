import unittest
from Library.Company import get_Company

class TestLibrary(unittest.TestCase):
    def test_allow_country(self):
        self.assertEqual(True, get_Company(iso_code='Dk'))
    def test_disllow_country(self):
        self.assertEqual(False, get_Company(iso_code='Debmark'))

