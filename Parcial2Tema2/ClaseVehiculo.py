import abc
from abc import ABC

class Vehiculo(ABC):
    __marca:str
    __modelo: str
    __aniofab: int
    __capacidad: int
    __plazas: int
    __distancia: float
    __tarifa: float
    def __init__(self,marca, modelo, anio, cap, pla, dis, tar):
        self.__marca=marca
        self.__modelo=modelo
        self.__aniofab=anio 
        self.__capacidad=cap
        self.__plazas=pla
        self.__distancia=dis 
        self.__tarifa= tar
    
    def getTarifa(self):
        return self.__tarifa

    @abc.abstractmethod
    def getTarifaTotal(self):
        pass

    def __str__(self):
        return f"""Modelo: {self.__modelo}
                    Anio de Fabricacion: {self.__aniofab}
                    Capacidad de pasajeros: {self.__capacidad}
                    Tarifa TOTAL de servicio: {self.getTarifaTotal()}"""
        #return f'{self.__marca, self.__modelo, self.__aniofab,self.__capacidad,self.__plazas,self.__distancia,self.__tarifa}'
