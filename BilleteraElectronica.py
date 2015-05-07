'''
Created on 7/5/2015

@author: Daniela Ortiz (10-10517)
         Maria Lourdes Garcia (10-10264)
'''

class BilleteraElectronica():
    
    def __init__(self, ID, nombres, apellidos, CI, PIN):
        self.ID = ID
        self.nombres = nombres
        self.apellidos = apellidos
        self.CI = CI
        self.PIN = PIN
        self.creditos = []
        self.debitos = []
        self.balance = 0