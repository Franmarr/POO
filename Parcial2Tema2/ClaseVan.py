from ClaseVehiculo import Vehiculo

class Van(Vehiculo):
    __tcarroceria: str
    
    def __init__(self, marca, modelo, anio, cap, pla, dis, tar, tcarro):
        super().__init__(marca, modelo, anio, cap, pla, dis, tar)
        self.__tcarroceria=tcarro
    
    def __str__(self):
        return f'{super().__str__(),self.__tcarroceria}'
    
    def getTarifaTotal(self):
        base=self.getTarifa()
        total=self.getTarifa()
        if self.__tcarroceria== 'minivan':
            total-=(10*base)/100
        else:
            total+=(2.5*base)/100
        
        return total
        
