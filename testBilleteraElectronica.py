'''
Created on 7/5/2015

@author: Daniela Ortiz (10-10517)
         Maria Lourdes Garcia (10-10264)
'''
import unittest
from BilleteraElectronica import *
from datetime import datetime

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
        
    # Caso para verificar que existe la estructura creditos y el metodo recargar
    
    def testRecargarExists(self):
        Billetera = BilleteraElectronica("356TgHJ1", "Maria", "Peres", 5617234, 187423)
        Fecha = datetime(2015, 4, 23, 8, 5)
        Billetera.recargar(12000, Fecha, "981yHJ32")
        
    # Caso para verificar que existe la estructura debitos y el metodo consumir
    
    def testConsumirExists(self):
        Billetera = BilleteraElectronica("24Saa90j" , "Luis", "Garcia", 8226134, 663312)
        Fecha = datetime (2009, 8, 30, 3, 25)
        Billetera.consumir(5000, Fecha, "HOk234t1")
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()