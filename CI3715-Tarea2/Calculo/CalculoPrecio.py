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

class Formato:
    def __init__(self, fecha, hora):
        self.fecha = fecha
        self.hora = hora
        
class Servicio:
    def __init__(self, inicioFecha, inicioHora, finFecha, finHora):
        #Transformamos las horas con minutos a un formato que pueda
        #entender la funcion CalculoPrecio
        horaNuevaIni = inicioHora.hour + (inicioHora.minute)/60
        horaNuevaFin = finHora.hour + (finHora.minute)/60
        
        self.inicioDeServicio = Formato(inicioFecha, horaNuevaIni)
        self.finDeServicio = Formato(finFecha, horaNuevaFin)