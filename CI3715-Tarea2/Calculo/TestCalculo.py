'''
Created on 9 may. 2018

@author: Giulianne Tavano y Angelica Acosta
'''

import unittest
from datetime import date, time
from Calculo.CalculoPrecio import Tarifa, Servicio, calcularPrecio

class TestCalculo(unittest.TestCase):
    
    #Caso: inicia a finales de un año y finaliza en principios del otro.
    def testFinAnio(self):
        dia1 = date(2018, 12, 30)
        dia2 = date(2019, 1, 2)
        horaIni = time(hour=1, minute=20, second=0, microsecond=0)
        horaFin = time(hour=1, minute=20, second=0, microsecond=0)
        tarifa = Tarifa(1,2)

        tiempoDeServicio = Servicio(dia1, horaIni, dia2, horaFin)
        

        assert calcularPrecio(tarifa, tiempoDeServicio)==96, "No se esta calculando bien el precio"
    
  
 