from ClaseGestorVehiculo import GestorVehiculo

def menu():
    opc=int(input("""
                    1. Agregar vehículos a la colección
                    2. Dada una posición de la lista: Mostrar por pantalla qué tipo de vehículo se encuentra 
                    almacenado en dicha posición (usar la función isinstance()).
                    3. Mostrar la cantidad de vehículos de cada tipo.
                    4. Recorrer la colección y mostrar para todos los Vehículos: modelo, año de fabricación, 
                    capacidad de pasajeros y la tarifa del servicio.
                  Ingrese opcion: """))
    return opc

if __name__=='__main__':
    Ve=GestorVehiculo()
    Ve.cargarVehiculo()
    opc=menu()
    while opc !=0:
        if opc==1:
            try:
                tipoVehi=int(input("Ingrese tipo de vehiculo 1(autobus) o 2(van) o 0(terminar): "))
                while tipoVehi not in (1,2,0):
                    tipoVehi=int(input("Numero INVALIDO, Ingrese tipo de vehiculo 1(autobus) o 2(van) o 0(terminar): "))
                if tipoVehi!=0:
                    xmarca=input("marca: ")
                    xmodelo=input("Modelo: ")
                    xanio=int(input("Anio: "))
                    xcap=int(input("capacidad: "))
                    xpla=float(input("PLazas: "))
                    xdis=float(input("Distancia: "))
                    xtari=float(input("Tarifa: "))
                    if tipoVehi==1:
                        xtiposer=input("tipo de servicio: ")
                        xturno=input("turno(manana, tarde, noche): ")
                        Ve.agregarAutobus(xmarca,xmodelo,xanio,xcap,xpla,xdis,xtari,xtiposer,xturno)
                        Ve.mostrar()
                    else:
                        xcarroceria=input("ingrese tipo de carroceria(van o minivan): ")
                        Ve.agregarVAN(xmarca,xmodelo,xanio,xcap,xpla,xdis,xtari,xcarroceria)
                        Ve.mostrar()
                else:
                    print("Termino inciso 1")

            except ValueError:
                print("se esperaba un numero ")
        elif opc==2:
            try:
                posicion=int(input("Que posicion busca?: "))
                Ve.buscarPosicion(posicion)
            except ValueError:
                print("ERROR, se espera")
        elif opc ==3:
            Ve.calcularCantidad()
                
        elif opc ==4:
            Ve.mostrar()
        opc=int(input("Ingrese nuevamente opcion, 0 para terminar: "))