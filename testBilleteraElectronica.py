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
    
    # Caso para verificar que existe la clase Billetera Electronica
    
    def testBilleteraElectronicaExist(self):
        BilleteraElectronica("AfJ556tY", "Nelson", "Gonzalez", 19994187, 123456)
        
    # Caso para verificar que existe el constructor de la clase Billetera 
    # Electronica
        
    def testBEAtributes(self):
        BilleteraElectronica("AfJ556tY", "Nelson", "Gonzalez", 19994187, 123456)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()