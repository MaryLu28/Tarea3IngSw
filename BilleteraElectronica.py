'''
Created on 7/5/2015

@author: Daniela Ortiz (10-10517)
         Maria Lourdes Garcia (10-10264)
'''

# -*- coding: utf-8 -*-

class BilleteraElectronica():
    
    def __init__(self, ID, nombres, apellidos, CI, PIN):
        if type(CI) != int:
            raise Exception("Cedula Invalida")
        if type(PIN) != int:
            raise Exception("PIN Invalido")
        self.ID = ID
        self.nombres = nombres
        self.apellidos = apellidos
        self.CI = CI
        self.PIN = PIN
        self.creditos = []
        self.debitos = []
        self.balance = 0
        
    def saldo (self):
        return(self.balance)
    
    def recargar(self, monto, fecha, identificador):
        if monto <= 0:
            raise Exception("Recarga invalida: Monto negativo o cero")
        else:
            recarga = (monto,fecha,identificador) 
            self.creditos.append(recarga)
            self.balance += monto
        
    def consumir(self, monto, fecha, identificador, PIN):
        if monto <= 0:
            raise Exception("Consumo invalida: Monto negativo o cero")
        elif monto > self.balance:
            raise Exception("Saldo Insuficiente")
        elif PIN != self.PIN:
            raise Exception("PIN Invalido")
        else:
            consumo = (monto,fecha,identificador)
            self.debitos.append(consumo)
            self.balance -= monto
