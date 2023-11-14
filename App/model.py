"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
import datetime
from tabulate import tabulate
import math


assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    sismo = { "seg" : None

    }

    sismo["seg"] = om.newMap(omaptype="RBT",cmpfunction=compareDates
                                      )
    return sismo
#comparefunction=compareDates
# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    pass


def add_seg(sismo,data):
    fechasis = data["time"]    
    
    if data.get("cdi")== "":
        cdi = "Unavailable"
    else:
        cdi = data.get('cdi')
        

    if data.get("mmi")== "":
        mmi = "Unavailable"
    else:
        mmi = data.get('mmi')
        
    if data.get("nst")== "":
        nst = 1
    else:
        nst = data.get('nst')
        
    if data.get("gap")== "":
        gap = 0.00
    else:
        gap = data.get('gap')
    
    dicc = {}
    dicc["time"] = data.get('time')
    dicc["mag"] = data.get('mag')
    dicc["lat"] = data.get('lat')
    dicc["long"] = data.get('long')
    dicc["depth"] = data.get('depth')
    dicc["sig"] = data.get('sig')
    dicc["gap"] = gap
    dicc["nst"] = nst
    dicc["title"] = data.get('title')

    dicc["cdi"] = cdi
    dicc["mmi"] = mmi
    dicc["magType"] = data.get('magType')

    dicc["type"] = data.get('type')

    dicc["code"] = data.get('code')

    
    fecha = datetime.datetime.strptime(fechasis,"%Y-%m-%dT%H:%M:%S.%fz")
        
    om.put(sismo,fecha,dicc)
    return sismo
# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass

def primeros_ultimos_5(mapa):
    ultimo_elemento = om.size(mapa)
    
    if ultimo_elemento < 7:
        return om.valueSet(mapa),ultimo_elemento
    
    primero = om.select(mapa,0)
    quinto = om.select(mapa,4)
    ultimo = om.select(mapa,ultimo_elemento-1)
    quintoultimo = om.select(mapa,ultimo_elemento-5)
    
    primeros = om.values(mapa,primero,quinto)
    ultimos = om.values(mapa,quintoultimo,ultimo)
    return crear_lista(ultimos,primeros),ultimo_elemento

def crear_lista(a,b):
    lt.exchange(a,1,3)
    lt.exchange(b,1,3)
    
    for resultados in lt.iterator(b):
         lt.addLast(a,resultados)
    return a

def lab_lista(lista_de_listas):
    lista = lt.newList("ARRAY_LIST")
    for cada_lista in lt.iterator(lista_de_listas):
        lt.addLast(lista, lt.getElement(cada_lista,1))
    return lista


def lab_lista2(lista_de_listas):
    lista = lt.newList("ARRAY_LIST")
    for cada_lista in lt.iterator(lista_de_listas):
        lt.addLast(lista,lt.getElement(cada_lista,1))
        lt.addLast(lista,lt.getElement(cada_lista,2))
        lt.addLast(lista,lt.getElement(cada_lista,3))
    return lista

def lab_lista_req1(lista_de_listas):
    lista = lt.newList("ARRAY_LIST")
    total_sis = 0
    

    for cada_lista in lt.iterator(lista_de_listas):
        lista2 = lt.newList("ARRAY_LIST")
        fecha = lt.getElement(cada_lista,1)["time"]
        size = lt.size(cada_lista)
        total_sis = size + total_sis
        lt.addLast(lista2,fecha)
        lt.addLast(lista2,size)
        tabla = tabulate(lt.iterator(cada_lista),headers = "keys",tablefmt="grid")

        lt.addLast(lista2, tabla)
        lt.addLast(lista,lista2)
    total_dates = lt.size(lista)

    return total_dates,total_sis,lista

def ultimos_primeros(data):
    
    if lt.size(data) < 6:
        return data
    else:
        a = lt.size(data)-2
        return crear_lista(lt.subList(data,a,3),lt.subList(data,1,3))

def req_1(sismos,inicial,final):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    inicial = datetime.datetime.strptime(inicial,"%Y-%m-%dT%H:%M")
    final = datetime.datetime.strptime(final,"%Y-%m-%dT%H:%M")
    
    valores = om.valueSet(sismos)
    bst = om.newMap(omaptype="RBT",cmpfunction=compareDates)
    for valor in lt.iterator(valores):
          
        lista = lt.newList("ARRAY_LIST")
        
        fecha = datetime.datetime.strptime(valor["time"][:-11],"%Y-%m-%dT%H:%M")
        entry = om.get(bst,fecha)
        if entry:
            lista = me.getValue(entry)
            lt.removeLast(lista)
        if valor != None:
            lt.addLast(lista,valor)
        valor.pop("time")
        lt.addLast(lista,fecha)
        om.put(bst,fecha,lista)
    
    return om.values(bst,inicial,final)

def tabulate_req_1(bst):
    
    lista = lt.newList("ARRAY_LIST")
    
    contador = 0
    for cada_lista in lt.iterator(bst):
        lista2 = lt.newList("ARRAY_LIST")
        fecha = lt.lastElement(cada_lista)
        lt.removeLast(cada_lista)
        size = lt.size(cada_lista)
        contador = contador + size
        lt.addLast(lista2,fecha)
        lt.addLast(lista2,size)
        
        tabla = tabulate(lt.iterator(cada_lista),headers = "keys",tablefmt="grid")

        lt.addLast(lista2, tabla)
        lt.addLast(lista,lista2)

    return lt.size(bst),contador, lista 

def req_2(sismo):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    valores = om.valueSet(sismo)
    mag = om.newMap(omaptype="RBT",cmpfunction=compareMag)
    contador = 0
    for valor in lt.iterator(valores):
        magnitud = float(valor["mag"])
        fecha = valor["time"]
        
        llavevalor = om.get(mag,magnitud)
        if llavevalor is None:
            mapa = om.newMap(omaptype="RBT",cmpfunction=compareDates2)
            
        else:
            mapa = me.getValue(llavevalor)
            contador = contador + 1
            
        om.put(mapa,fecha,valor)  
        om.put(mag,magnitud,mapa)

    return contador,mag

def tabulate_req_2(bts,inf,sup):
    inf = om.ceiling(bts,inf)
    sup = om.floor(bts,sup)

    filtrado = om.values(bts,inf,sup)
    contador = 0
    listas = lt.newList("ARRAY_LIST") 
    for cada_mapa in lt.iterator(filtrado):
        lista = lt.newList("ARRAY_LIST") 
        vals = om.valueSet(cada_mapa)
        events = lt.size(vals)
        vals = ultimos_primeros(vals)
        contador = lt.size(vals) + contador
    
        tabla = tabulate(lt.iterator(vals),headers = "keys", tablefmt="grid")
        
        magnitud = lt.getElement(vals,1)["mag"]
        
        
        lt.addLast(lista,magnitud)
        lt.addLast(lista,events)
        lt.addLast(lista,tabla)
        lt.addLast(listas,lista)
    return lt.size(listas),filtrado,listas


def req_3(sismo, mag, depth):
    """
    Función que soluciona el requerimiento 3
    """
    values = om.valueSet(sismo)
    bst = om.newMap(omaptype = "RBT", cmpfunction = compareDates)
    cont = 0

    for value in lt.iterator(values):
        if float(value["mag"]) > mag and value != None and float(value["depth"]) >= depth:                        
            cont += 1

            lists = lt.newList("ARRAY_LIST")
            date = datetime.datetime.strptime(value["time"][:-11],"%Y-%m-%dT%H:%M")
            entry = om.get(bst, date)

            if entry:
                lists = me.getValue(entry)
                lt.removeLast(lists)

            if value != None:
                lt.addLast(lists, value)

            value.pop("time")
            lt.addLast(lists, date)
            om.put(bst, date, lists)

    return(om.size(bst), cont, tabulate_req_3(bst, om.size(bst)))


def tabulate_req_3(bst, num):
    ini = om.select(bst, num - 20)
    ult = om.select(bst, num - 1)
    lista_de_listas = om.values(bst,ini,ult)

    lista = lt.newList("ARRAY_LIST")

    for cada_lista in lt.iterator(lista_de_listas):
        lista2 = lt.newList("ARRAY_LIST")
        fecha = lt.lastElement(cada_lista)
        lt.removeLast(cada_lista)
        size = lt.size(cada_lista)

        lt.addLast(lista2,fecha)
        lt.addLast(lista2,size)

        tabla = tabulate(lt.iterator(cada_lista), headers = "keys", tablefmt = "grid")

        lt.addLast(lista2, tabla)
        lt.addLast(lista, lista2)

    return lista


def req_4(sismo,sig,gap):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    valores = om.valueSet(sismo)
    bst = om.newMap(omaptype="RBT",cmpfunction=compareDates)
    contador = 0
    for valor in lt.iterator(valores):
        
        if int(valor["sig"])>=sig and float(valor["gap"])<=gap and valor != None:
            copia = valor.copy()   
            contador =contador + 1
            
            lista = lt.newList("ARRAY_LIST")
            
            fecha = datetime.datetime.strptime(valor["time"][:-11],"%Y-%m-%dT%H:%M")
            entry = om.get(bst,fecha)
            if entry:
                lista = me.getValue(entry)
                lt.removeLast(lista)
            if valor != None:
                lt.addLast(lista,copia)
            copia.pop("time")
            lt.addLast(lista,fecha)
            om.put(bst,fecha,lista)
    num = om.size(bst)
    
    
    num = om.size(bst)
    ini = om.select(bst,num-15)
    ult = om.select(bst,num-1)
    
    lista_de_listas = om.values(bst,ini,ult)
    
    total_dates = om.size(bst)
    total_events = contador
    return total_dates, total_events,lista_de_listas


def tabulate_req_4(lista_de_listas):
    
    
    lista = lt.newList("ARRAY_LIST")
    

    for cada_lista in lt.iterator(lista_de_listas):
        lista2 = lt.newList("ARRAY_LIST")
        fecha = lt.lastElement(cada_lista)
        lt.removeLast(cada_lista)
        size = lt.size(cada_lista)
        
        lt.addLast(lista2,fecha)
        lt.addLast(lista2,size)
        
        tabla = tabulate(lt.iterator(cada_lista),headers = "keys",tablefmt="grid")

        lt.addLast(lista2, tabla)
        lt.addLast(lista,lista2)

    return lista


def req_5(sismo, depth, nst):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    valores = om.valueSet(sismo)
    bst = om.newMap(omaptype="RBT",cmpfunction=compareDates)
    contador = 0
    for valor in lt.iterator(valores):
        
        if float(valor["depth"])>=depth and float(valor["nst"])>=nst and valor != None:
            copia = valor.copy()    
            contador =contador + 1
            
            lista = lt.newList("ARRAY_LIST")
            
            fecha = datetime.datetime.strptime(valor["time"][:-11],"%Y-%m-%dT%H:%M")
            entry = om.get(bst,fecha)
            if entry:
                lista = me.getValue(entry)
                lt.removeLast(lista)
            if copia != None:
                lt.addLast(lista,copia)
            copia.pop("time")
            lt.addLast(lista,fecha)
            om.put(bst,fecha,lista)
    num = om.size(bst)
    data = tabulate_req_5(bst,num)
    total_dates = om.size(bst)
    total_events = contador
    return total_dates, total_events,data


def tabulate_req_5(bst,num):
    ini = om.select(bst,num-19)
    ult = om.select(bst,num-1)
    lista_de_listas = om.values(bst,ini,ult)
    
    lista = lt.newList("ARRAY_LIST")
    

    for cada_lista in lt.iterator(lista_de_listas):
        lista2 = lt.newList("ARRAY_LIST")
        fecha = lt.lastElement(cada_lista)
        lt.removeLast(cada_lista)
        size = lt.size(cada_lista)
        
        lt.addLast(lista2,fecha)
        lt.addLast(lista2,size)
        
        tabla = tabulate(lt.iterator(cada_lista),headers = "keys",tablefmt="grid")

        lt.addLast(lista2, tabla)
        lt.addLast(lista,lista2)

    return lista


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compareMag(date1, date2):
    """
    Compara dos fechas
    """
    date1 = float(date1)
    date2 = float(date2)
    
    
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
    
def compareDates2(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 < date2):
        return 1
    else:
        return -1

def Haversine(lat1,lat2,long1,long2):
    lat1 = float(lat1)
    lat1 = float(lat2)
    long1 = float(long1)
    long2 = float(long2)
    
    lat1= math.radians(lat1)
    lat2 =  math.radians(lat2)
    long1 = math.radians(long1)
    long2 = math.radians(long2)
    
    delta_lat = lat2-lat1
    delta_long = long2-long1
    a = math.sin(delta_lat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_long/2)**2
    
    c = math.sqrt(a)
    distancia = 2 * 6731 * math.asin(c)
    
    return distancia