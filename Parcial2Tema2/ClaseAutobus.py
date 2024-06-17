from ClaseVehiculo import Vehiculo

class Autobus(Vehiculo):
    __servicio: str
    __turno:str
    def __init__(self, marca, modelo, aniofab, cap, pla, dist, tarifa, serv, turno):
        super().__init__(marca, modelo, aniofab, cap, pla, dist, tarifa)
        self.__servicio=serv
        self.__turno=turno
    
    def __str__(self):
        return f'{super().__str__(),self.__servicio, self.__turno}'
    
    def getTarifaTotal(self):
        base=self.getTarifa()
        total=self.getTarifa()
        if self.__turno=='nocturno' and self.__servicio=='turismo':
            total=(20*base)/100
        else:
            total=(5*base)/100
        return total