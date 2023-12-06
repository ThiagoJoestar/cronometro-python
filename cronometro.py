import time

import os

class Cronometro:
    
    
    def __init__(self,milesimos = 0, segundos = 0, minutos = 0, horas = 0):
        self.milesimos = milesimos
        self.segundos = segundos
        self.minutos = minutos
        self.horas = horas
        
    def __repr__(self) :
        return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}:{self.milesimos:02d}'
    
    def incremento(self):
        self.milesimos += 1
        if self.milesimos >= 10:
           self.segundos += 1
           self.milesimos = 0
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1
            
    def start(self):
        while True:
            os.system('cls') #Cmd para limpar o terminal no Windows, para Linux usar 'clear'
            print(self)
            self.incremento()
            time.sleep(0.10)

cronometro1 = Cronometro()

cronometro1.start()

        