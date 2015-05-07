'''
Created on 7/5/2015

@author: Daniela Ortiz (10-10517)
         Maria Lourdes Garcia (10-10264)
'''
import unittest
from BilleteraElectronica import *

class TestBilleteraElectronica(unittest.TestCase):

    ###########################################################################
    #                               Casos TDD                                 #
    ###########################################################################
    
    # Caso para verificar que existe la clase BilleteraElectronica
    
    def testBilleteraElectronicaExist(self):
        BilleteraElectronica("AfJ556tY", "Nelson", "Gonzalez", 19994187, 123456)
        
    # Caso para verificar que existen los atributos de la clase
        
    def testBEAtributes(self):
        BilleteraElectronica("AfJ556tY", "Nelson", "Gonzalez", 19994187, 123456)
        
    # Caso para verificar que existe el metodo saldo
    
    def testSaldoExists(self):
        Billetera = BilleteraElectronica("76rYU0PL", "Manuel", "Pacheco", 21345227, 987654)
        Billetera.saldo()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()