"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """

    control = controller.new_controller()
   
    return control   


def print_menu():
    print("\nBienvenido")
    print("1- Cargar información")
    print("2- Conocer los eventos sismicos entre dos fechas")
    print("3- Conocer los eventos sísmicos entre dos magnitudes")
    print("4- Consultar los 10 eventos más recientes según una magnitud y profundidad indicadas")
    print("5- Consultar los 15 eventos sísmicos más recientes según su significancia y una distancia azimutal ")
    print("6- Consultar los 20 eventos más recientes para una profundidad dada y registrados por un cierto número de estaciones")
    print("7- Reportar el evento más significativo y los N eventos más próximos cronológicamente ocurridos dentro del área alrededor de un punto")
    print("8- Graficar un histograma anual de los eventos ocurridos según la región y propiedades de los eventos")
    print("9- Visualizar los eventos sísmicos de cada requerimiento en un mapa interactivo ")
    print("0- Salir")


def load_data(control,tamaño):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    return controller.load_data(control,tamaño)


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    print("\n=============== Req No. 1 Inputs ===============")
    inicial = input("Start date: ")
    final = input("End date: ")
    
    return controller.req_1(control, inicial,final)


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    print("\n=============== Req No. 2 Inputs ===============")
    inf = input("El límite inferior de la magnitud: ")
    sup = input("El límite superior de la magnitud: ")
    
    return controller.req_2(control,float(inf),float(sup))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    print("\n=============== Req No. 4 Inputs ===============")
    sig = input("La significancia mínima del evento: ")
    gap = input("La distancia azimutal máxima del evento: ")
    return controller.req_4(control,sig,gap)


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    print("\n=============== Req No. 5 Inputs ===============")
    depth = input("Min depth: ")
    nst = input("Max nst (seismic stations): ")
    return controller.req_5(control, depth, nst)


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    print("\n=============== Req No. 6 Inputs ===============")
    year = input("Year: ")
    latitude = input("Focus Latitude: ")
    longitude = input("Focus Longitude: ")
    radius = input("Relevant Radius: " + "[km]")
    m_i_events = input("Number of most imoortant events: \n\n")
    return controller.req_5(control, year, latitude, longitude, radius, m_i_events)


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('\nSeleccione una opción para continuar\n')
        if int(inputs) == 1:
            
            print("\nTamaño de los archivos: ")
            print(" 1. small\n 2. 5pct\n 3. 10pct\n 4. 20pct\n 5. 30pct\n 6. 50pct\n 7. 80pct\n 8. large")
    
            tamaño = input("\nSeleccione el tamaño de los archivos: ")
            
            print("Cargando información de los archivos ....\n")
            
            
            
            
            data,size = load_data(control, tamaño)
            print("Numero de sismos cargados: " + str(size))
            print(tabulate(lt.iterator(data),headers="keys", tablefmt="grid"))
            
        elif int(inputs) == 2:
            diff_dates,total_sis,data = print_req_1(control)
            listas = []
            for datos in lt.iterator(data):
                uno = lt.getElement(datos,1)
                dos = lt.getElement(datos,2)
                tres = lt.getElement(datos,3)
                lista = []
                lista.append(uno)
                lista.append(dos)
                lista.append(tres)
                listas.append(lista)
            
            print("\n=============== Req No. 1 Results ===============")
            print("Total different dates: " +str(diff_dates))
            print("Total events between dates: " +str(total_sis))
            print("Consult size: " +str(consult_size) + "Only the first and last '3' results are:")
            
            keys = ["time","events","details"]
            print(tabulate(listas,headers= keys ,tablefmt="grid"))

        elif int(inputs) == 3:
            
            total_mag, total_events,consult_size,data = print_req_2(control)
            listas = []
            for datos in lt.iterator(data):
                uno = lt.getElement(datos,1)
                dos = lt.getElement(datos,2)
                tres = lt.getElement(datos,3)
                lista = []
                lista.append(uno)
                lista.append(dos)
                lista.append(tres)
                listas.append(lista)
                
            print("\n=============== Req No. 2 Results ===============")
            print("Total different dates: " +str(total_mag))
            print("Total events between dates: " +str(total_events))
            print("Consult has " + str(total_mag) + " results")
            print("Consult size: " +str(consult_size) + "Only the first and last '3' results are:")
            
            keys = ["time","events","details"]
            print(tabulate(listas,headers= keys ,tablefmt="grid"))

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            total_dates, total_events,data = print_req_4(control)
            listas = []
            for datos in lt.iterator(data):
                uno = lt.getElement(datos,1)
                dos = lt.getElement(datos,2)
                tres = lt.getElement(datos,3)
                lista = []
                lista.append(uno)
                lista.append(dos)
                lista.append(tres)
                listas.append(lista)
            
            print("\n=============== Req No. 4 Results ===============")
            print("Total different dates: " +str(total_dates))
            print("Total events between dates: " +str(total_events))
            print("Selecting the first 15 results...")
            print("Consult size: " +str(total_dates) + " The first and last '3' of the '15' results are:")
            
            
            keys = ["time","events","details"]
            print(tabulate(listas,headers= keys ,tablefmt="grid"))

        elif int(inputs) == 6:
            total_dates, total_events, data = print_req_5(control)
            listas = []
            for datos in lt.iterator(data):
                uno = lt.getElement(datos,1)
                dos = lt.getElement(datos,2)
                tres = lt.getElement(datos,3)
                lista = []
                lista.append(uno)
                lista.append(dos)
                lista.append(tres)
                listas.append(lista)
            
            print("\n=============== Req No. 5 Results ===============")
            print(f"Total different dates: '{str(total_dates)}'")
            print(f"Total events between dates: '{str(total_events)}'")
            print("Selecting the first 20 results...\n")
            print(f"Consult size: '{str(total_dates)}' The first and last '3' of the '20' results are:")
            
            
            keys = ["time","events","details"]
            print(tabulate(listas,headers= keys ,tablefmt="grid"))
            print()

        elif int(inputs) == 7:
            print(f"Max event code: '{str(total_dates)}'")
            print(f"Post n events: '{str(total_dates)}'")
            print(f"Pre n events: '{str(total_dates)}'\n")
            
            print("\n=============== Req No. 6 Results ===============")
            print(f"Number of events within radius: '{str(total_dates)}'")
            print(f"Max number of possible events: '{str(total_events)}'")
            print(f"Total different dates: '{str(total_events)}'")
            print(f"Total events between dates: '{str(total_events)}'")
            print("Selecting the first 20 results...\n")
            print(f"Consult size: '{str(total_dates)}' The first and last '3' of the '20' results are:")

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
