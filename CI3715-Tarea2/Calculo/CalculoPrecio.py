'''
Created on 9 may. 2018

@author: Giulianne Tavano y Angelica Acosta
'''
from math import ceil, floor
from datetime import timedelta

class Tarifa:
    def __init__(self, tarifaSemana, tarifaFin):
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
        
def calcularPrecio(tarifa, tiempoDeServicio):
    inicio = tiempoDeServicio.inicioDeServicio
    fin = tiempoDeServicio.finDeServicio
    
    try:
        #Verificamos que el servicio dura al menos 15 minutos
        if (inicio.fecha == fin.fecha):
            assert(fin.hora - inicio.hora >= 0.25)
        elif (fin.fecha > inicio.fecha):
            assert( (24-inicio.hora +fin.hora)>=0.25)

        #Verificamos que el servicio dura como maximo 7 dias
        assert(0 <= (fin.fecha - inicio.fecha).days <= 7)

        if ((fin.fecha - inicio.fecha).days == 7):
            assert(fin.hora<=inicio.hora)

    except:
        print("Duracion de Servicio Invalida")
        exit()
        
    try:
        #Verificamos que las tarifas sean validas
        assert(tarifa.tarifaSemana>0 and tarifa.tarifaFin>0)
    except:
        print("Valor de tarifa invalido")
        exit()
        
    costo = 0
    diasServicio = (fin.fecha - inicio.fecha).days

    if (diasServicio == 0):
        costo = ceil(fin.hora - inicio.hora)
        if (1<=inicio.fecha.isoweekday()<=5):
            costo = costo * tarifa.tarifaSemana
        else:
            costo = costo * tarifa.tarifaFin
        return costo
    
    #Para el primer dia
    if (1<=inicio.fecha.isoweekday()<=5):
        costo = tarifa.tarifaSemana * (24-floor(inicio.hora))
    else:
        costo = tarifa.tarifaFin * (24-floor(inicio.hora))

    #Para los dias intermedio
    diasCompletos =  diasServicio - 1
    diaActual = inicio.fecha + timedelta(days=1)
    
    if (diasCompletos > 0):
        for i in range(diasCompletos):
            if (1<=diaActual.isoweekday()<=5):
                costo = costo + tarifa.tarifaSemana * 24 
            else:
                costo = costo + tarifa.tarifaFin * 24
            diaActual = diaActual + timedelta(days=1)

    #Para el ultimo
    if (1<=fin.fecha.isoweekday()<=5):
        costo = costo + tarifa.tarifaSemana * ceil(fin.hora)
    else:
        costo = costo + tarifa.tarifaFin * ceil(fin.hora)
        
    return costo
