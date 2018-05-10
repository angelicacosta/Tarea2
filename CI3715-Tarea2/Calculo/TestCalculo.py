'''
Created on 9 may. 2018

@author: Giulianne Tavano y Angelica Acosta
'''


import unittest
from datetime import date, time
from CalculoPrecio import Tarifa, Servicio, calcularPrecio

class TestCalculo(unittest.TestCase):
	
	#Caso: inicia a finales de un year y finaliza en principios del otro.
	def testFinAnio(self):
		dia1 = date(2018, 12, 30)
		dia2 = date(2019, 1, 2)
		horaIni = time(hour=1, minute=20, second=0, microsecond=0)
		horaFin = time(hour=1, minute=20, second=0, microsecond=0)
		tarifa = Tarifa(1,2)

		tiempoDeServicio = Servicio(dia1, horaIni, dia2, horaFin)
		
		assert calcularPrecio(tarifa, tiempoDeServicio)==96, "No se esta calculando bien el precio"
	
	#Caso: Tiene solo un dia pero menos de 15 minutos
	def testMenos15Minutos(self):
		dia1 = date(2018, 5, 18)
		dia2 = date(2018, 5, 18)
		horaIni = time(hour=1, minute=20, second=0, microsecond=0)
		horaFin = time(hour=1, minute=21, second=0, microsecond=0)
		tarifa = Tarifa(1,2)

		tiempoDeServicio = Servicio(dia1, horaIni, dia2, horaFin)
		
		with self.assertRaises(SystemExit) as cm:
			calcularPrecio(tarifa, tiempoDeServicio)
		self.assertEqual(cm.exception.code, None)

	#Caso: Mismo dia, exactamente 15 minutos.
	def testExact15Minutos(self):
		dia1 = date(2018, 5, 18)
		dia2 = date(2018, 5, 18)
		horaIni = time(hour=1, minute=0, second=0, microsecond=0)
		horaFin = time(hour=1, minute=15, second=0, microsecond=0)
		tarifa = Tarifa(1,2)

		tiempoDeServicio = Servicio(dia1, horaIni, dia2, horaFin)
		assert calcularPrecio(tarifa, tiempoDeServicio)==1, "No se esta calculando bien el precio"
		
	#Caso: Mismo dia, exactamente 15 minutos.
	def testMas15Minutos(self):
		dia1 = date(2018, 5, 18)
		dia2 = date(2018, 5, 18)
		horaIni = time(hour=1, minute=0, second=0, microsecond=0)
		horaFin = time(hour=1, minute=16, second=0, microsecond=0)
		tarifa = Tarifa(1,1)

		tiempoDeServicio = Servicio(dia1, horaIni, dia2, horaFin)
		assert calcularPrecio(tarifa, tiempoDeServicio)==1, "No se esta calculando bien el precio"

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
    
    #Caso: Tiene exactamente 7 dias.    
	def testExact7Dias(self):
		dia1 = date(2018, 5, 1)
		dia2 = date(2018, 5, 8)
		horaIni = time(hour=1, minute=0, second=0, microsecond=0)
		horaFin = time(hour=1, minute=0, second=0, microsecond=0)
		tarifa = Tarifa(1,1)

<<<<<<< HEAD
        tiempoDeServicio = Servicio(dia1, horaIni, dia2, horaFin)
        

        assert calcularPrecio(tarifa, tiempoDeServicio)==96, "No se esta calculando bien el precio"
=======
		tiempoDeServicio = Servicio(dia1, horaIni, dia2, horaFin)
>>>>>>> refs/remotes/origin/master
    
		assert calcularPrecio(tarifa, tiempoDeServicio)==168, "No se esta calculando bien el precio"
	
	#Caso: Tiene menos de 7 dias.
	def testMenos7Dias(self):
		dia1 = date(2018, 5, 18)
		dia2 = date(2018, 5, 20)
		horaIni = time(hour=1, minute=20, second=0, microsecond=0)
		horaFin = time(hour=1, minute=30, second=0, microsecond=0)
		tarifa = Tarifa(1,1)

<<<<<<< HEAD
        tiempoDeServicio = Servicio(dia1, horaIni, dia2, horaFin)
        
        with self.assertRaises(SystemExit) as cm:
            calcularPrecio(tarifa, tiempoDeServicio)
        self.assertEqual(cm.exception.code, None)
        #assert (self.assertRaises(SystemExit),1)
        #assert self.assertEqual(calcularPrecio(tarifa, tiempoDeServicio), "Fechas invalidas") 
    
    #Caso: Mismo dia, exactamente 15 minutos.
    def testExact15Minutos(self):
        dia1 = date(2018, 5, 18)
        dia2 = date(2018, 5, 18)
        horaIni = time(hour=1, minute=0, second=0, microsecond=0)
        horaFin = time(hour=1, minute=15, second=0, microsecond=0)
        tarifa = Tarifa(1,2)
=======
		tiempoDeServicio = Servicio(dia1, horaIni, dia2, horaFin)

		assert calcularPrecio(tarifa, tiempoDeServicio)==49, "No se esta calculando bien el precio"
>>>>>>> refs/remotes/origin/master

	#Caso: Acepta bisiestos.  
	def testAnioBisiesto(self):
		dia1 = date(2020, 2, 28)
		dia2 = date(2020, 3, 1)
		horaIni = time(hour=3, minute=0, second=0, microsecond=0)
		horaFin = time(hour=3, minute=0, second=0, microsecond=0)
		tarifa = Tarifa(1,1)

<<<<<<< HEAD
        tiempoDeServicio = Servicio(dia1, horaIni, dia2, horaFin)
        assert calcularPrecio(tarifa, tiempoDeServicio)==1, "No se esta calculando bien el precio"
    
    #Caso: Entra y sale en el mismo momento.
    def testIniFinIgual(self):
        dia1 = date(2018, 5, 18)
        dia2 = date(2018, 5, 18)
        horaIni = time(hour=1, minute=0, second=0, microsecond=0)
        horaFin = time(hour=1, minute=0, second=0, microsecond=0)
        tarifa = Tarifa(1,1)

        tiempoDeServicio = Servicio(dia1, horaIni, dia2, horaFin)
        with self.assertRaises(SystemExit) as cm:
            calcularPrecio(tarifa, tiempoDeServicio)
        self.assertEqual(cm.exception.code, None)
          
    #Caso: Horas al reves, el servicio termina antes de empezar
    def testHorasAlReves(self):
        dia1 = date(2018, 6, 7)
        dia2 = date(2018, 6, 7)
        horaIni = time(hour=18, minute=0, second=0, microsecond=0)
        horaFin = time(hour=10, minute=0, second=0, microsecond=0)
        tarifa = Tarifa(1,10)

        tiempoDeServicio = Servicio(dia1, horaIni, dia2, horaFin)
               
        with self.assertRaises(SystemExit) as cm:
            calcularPrecio(tarifa, tiempoDeServicio)
        self.assertEqual(cm.exception.code, None)
                 
    #Caso: Caso cuando tarifa es nula.  
    def testNulo(self):
        dia1 = date(2018, 5, 18)
        dia2 = date(2018, 5, 18)
        horaIni = time(hour=1, minute=0, second=0, microsecond=0)
        horaFin = time(hour=1, minute=1, second=0, microsecond=0)
        tarifa = Tarifa(0,0)

        tiempoDeServicio = Servicio(dia1, horaIni, dia2, horaFin)
        with self.assertRaises(SystemExit) as cm:
            calcularPrecio(tarifa, tiempoDeServicio)
        self.assertEqual(cm.exception.code, None) 
    
=======
		tiempoDeServicio = Servicio(dia1, horaIni, dia2, horaFin)

		assert calcularPrecio(tarifa, tiempoDeServicio)==48, "No se esta calculando bien el precio"

if __name__ == "__main__":  
	unittest.main()        
>>>>>>> refs/remotes/origin/master
