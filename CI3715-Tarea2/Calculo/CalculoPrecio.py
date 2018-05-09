'''
Created on 9 may. 2018

@author: Giulianne Tavano y Angelica Acosta
'''

class Tarifa:
    def __init__(self, tarifaSemana, tarifaFin):
        try:
            assert(tarifaSemana>0 and tarifaFin>0)
        except:
            print("Valor de tarifa invalido")
            exit()

        self.tarifaSemana = tarifaSemana
        self.tarifaFin = tarifaFin

