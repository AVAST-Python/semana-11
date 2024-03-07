import unittest
from suma_dos_numeros import suma


class TestSuma(unittest.TestCase):

    def test_suma_de_positivos(self):
        res = suma(1,2)
        expected = 3
        self.assertEqual(res, expected)

    def test_suma_con_cero(self):
        res = suma(0,2)
        expected = 2
        self.assertEqual(res, expected)

    def test_suma_negativo_y_positivo(self):
        res = suma(-1,2)
        expected = 1
        self.assertEqual(res, expected)

    def test_suma_de_negativos(self):
        res = suma(-1,-2)
        expected = -3
        self.assertEqual(res, expected)

