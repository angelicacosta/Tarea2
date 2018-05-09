'''
Created on 9 may. 2018

@author: Giulianne Tavano y Angelica Acosta
'''

import unittest
from datetime import date, time
from CalculoPrecio import Tarifa, Servicio, calcularPrecio

class TestCalculo(unittest.TestCase):
    
    #Caso: Tiene 7 dias y 1 minuto.
    def testMas7Dias(self):
        dia1 = date(2018, 5, 18)
        dia2 = date(2018, 5, 30)
        horaIni = time(hour=1, minute=20, second=0, microsecond=0)
        horaFin = time(hour=1, minute=21, second=0, microsecond=0)
        tarifa = Tarifa(1,2)
        
        tiempoDeServicio = Servicio(dia1, horaIni, dia2, horaFin)
        
        with self.assertRaises(SystemExit) as cm:
            calcularPrecio(tarifa, tiempoDeServicio)
        self.assertEqual(cm.exception.code, None)  

if __name__ == "__main__":  
    unittest.main()        