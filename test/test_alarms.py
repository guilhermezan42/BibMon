import unittest
import numpy as np
from bibmon._alarms import detecOutlier  

class TestDetecOutlier(unittest.TestCase):

    def test_CT1_sem_nan_modo_vetor(self):
        
        data = np.array([1, 2, 3])
        lim = 2
        resultado = detecOutlier(data, lim, count=False)
        esperado = np.array([0, 0, 1])
        np.testing.assert_array_equal(resultado, esperado)

    def test_CT2_com_nan_modo_vetor(self):
       
        data = np.array([1, np.nan, 3])
        lim = 1.5
        resultado = detecOutlier(data, lim, count=False)
        esperado = np.array([0, 0, 1])  
        np.testing.assert_array_equal(resultado, esperado)
    
    def test_CT3_count_acima_limite(self):
    
        data = np.array([5, 6, 7])
        lim = 4
        resultado = detecOutlier(data, lim, count=True, count_limit=2)
        esperado = 1
        self.assertEqual(resultado, esperado)

    def test_CT4_count_abaixo_ou_igual_limite(self):

        data = np.array([2, 3])
        lim = 2
        resultado = detecOutlier(data, lim, count=True, count_limit=2)
        esperado = 0
        self.assertEqual(resultado, esperado)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)