import libcomplex as lc
import unittest

class TestCplxMethods(unittest.TestCase):

    def test_cplxsum(self):
        # Caso de prueba (3 + 5i)+(-2.4 + 6.8i) = (0.6 + 11.8i)
        suma = lc.cplxsum((3.0,5.0),(-2.4,6.8))
        self.assertAlmostEqual(suma[0], 0.6)
        self.assertAlmostEqual(suma[1],11.8)

if __name__ == '__main__':
    unittest.main()

