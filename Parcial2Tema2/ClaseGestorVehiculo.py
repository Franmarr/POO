from ClaseVehiculo import Vehiculo
from ClaseAutobus import Autobus
from ClaseVan import Van
import csv

class GestorVehiculo():
    __listaV: list
    def __init__(self):
        self.__listaV=[]

    def agregarAutobus(self, marca, modelo, aniofab, cap, pla, dist, tarifa, serv, turno):
        self.__listaV.append(Autobus(marca, modelo, aniofab, cap, pla, dist, tarifa, serv, turno))

    def agregarVAN(self, marca, modelo, anio, cap, pla, dis,  tar, tcarro):
        self.__listaV.append(Van(marca,modelo,anio,cap,pla,dis,tar, tcarro))

    def mostrar(self): #no lo pide pero lo hago para mostrar si cargo o no los vehiculos
        for lista in self.__listaV:
            print(lista)

    def buscarPosicion(self,xpos):
        if (isinstance(self.__listaV[xpos], Autobus)):
            print(f"Es un autobus: {self.__listaV[xpos]}")
        else:
            print(f"Es un van: {self.__listaV[xpos]}")

    def mostrarCantidad(self,a,v):
        print(f"""La cantidad de autobuses es: {a}
                La cantidad de vanes es: {v}""")

    def calcularCantidad(self):
        a=0
        v=0
        for unVehiculo in self.__listaV:
            if (isinstance(unVehiculo, Autobus)):
                a+=1
            else:
                v+=1
        self.mostrarCantidad(a,v)
        
            

    def cargarVehiculo(self):
        archivo=open('vehiculos.csv')
        reader=csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            if fila[0] == 'A':
                self.agregarAutobus(fila[1],fila[2],int(fila[3]),int(fila[4]),int(fila[5]),float(fila[6]),float(fila[7]),fila[8],fila[9])
            elif fila[0]== 'V':
                self.agregarVAN(fila[1],fila[2],fila[3],int(fila[4]),int(fila[5]),float(fila[6]),float(fila[7]),fila[8])
            else:
                print("no se pudo cargar.")

        for lista in self.__listaV:#no lo pide pero para ver si carga o no
            print(lista)

        assert self.__listaV!=None,"No cargo nada"