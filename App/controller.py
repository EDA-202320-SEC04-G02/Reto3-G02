﻿"""
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
 """

import config as cf
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }   
    return control


# Funciones para la carga de datos

def load_data(control, tamaño):
    """
    Carga los datos del reto
    """
    inicio = get_time()

    tamaño = int(tamaño)
    tm = 'small'
    if tamaño == 2:
        tm = "5pct"
    if tamaño == 3:
        tm = "10pct"
    if tamaño == 4:
        tm = "20pct"
    if tamaño == 5:
        tm = "30pct"
    if tamaño == 6:
        tm = "50pct"
    if tamaño == 7:
        tm = "80pct"
    if tamaño == 8:
        tm = "large"
    
    control["model"] = model.new_data_structs()
    sismo = control["model"]
    load_date(sismo,tm)
    primero_ultimos,size = model.primeros_ultimos_5(sismo["seg"])
    final = get_time()
    delta = delta_time(inicio,final)
    
    return primero_ultimos,size



# Funciones de ordenamiento

def load_date(sismo,tm):
    
    temblorefile = cf.data_dir + 'earthquakes/temblores-utf8-' + tm + '.csv'
    input_file = csv.DictReader(open(temblorefile, encoding='utf-8'))
    
    for data in input_file:
        
        model.add_seg(sismo["seg"],data)
    
        
    return sismo

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control,inicial,final):
    """
    Retorna el resultado del requerimiento 1
    """
    inicio = get_time()
    sismo = control["model"]
    datos = model.req_1(sismo["seg"],inicial,final)
    final = get_time()
    delta = delta_time(inicio,final)
    
    diff_dates,total_sis,datos_finales= model.tabulate_req_1(datos)
    datos_finales = model.ultimos_primeros(datos_finales)
    
    
    
    return diff_dates,total_sis,datos_finales, delta


def req_2(control,inf,sup):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    inicial = get_time()
    sismo = control["model"]
    consult_size,datos = model.req_2(sismo["seg"])
    total_mag,total_events, lista_final = model.tabulate_req_2(datos,inf,sup)
    lista_final = model.ultimos_primeros(lista_final)
    
    return total_mag, total_events,consult_size,lista_final


def req_3(control, mag, depth):
    """
    Retorna el resultado del requerimiento 3
    """
    inicial = get_time()
    sismo = control["model"]
    mag = int(mag)
    depth = float(depth)

    total_dates, total_events,datos = model.req_3(sismo["seg"], mag, depth)

    datos = model.tabulate_req_3(datos)
    datos = model.ultimos_primeros(datos)
    final = get_time()
    delta = delta_time(inicial,final)

    return total_dates, total_events, datos, delta


def req_4(control,sig,gap):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    inicial = get_time()
    
    sismo = control["model"]
    sig = int(sig)
    gap = float(gap)
    total_dates, total_events,datos = model.req_4(sismo["seg"],sig,gap)
    
    datos = model.tabulate_req_4(datos)
    datos = model.ultimos_primeros(datos)
    final = get_time()
    delta = delta_time(inicial,final)
    return total_dates, total_events,datos,delta


def req_5(control, depth, nst):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    
    inicial = get_time()
    sismo = control["model"]
    depth = float(depth)
    nst = int(nst)
    
    total_dates, total_events,datos = model.req_5(sismo["seg"], depth, nst)
    final = get_time()
    delta = delta_time(inicial,final)
    datos = model.ultimos_primeros(datos)
    
    return total_dates, total_events,datos,delta

def req_6(control, year, lat1, long1, radius,important_events):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    inicial = get_time()
    sismo = control["model"]
    total_dates,total_events,lista_de_listas,the_choosen_one = model.req_6(sismo["seg"], year, lat1, long1, radius,important_events)

    final = get_time()
    delta = delta_time(inicial,final)
    data = model.tabulate_req_6(lista_de_listas)
    data = model.ultimos_primeros(data)
    return total_dates,total_events,data,the_choosen_one,delta

def req_7(control, anio, title, prop, bins):
    """
    Retorna el resultado del requerimiento 7
    """
    sismo = control["model"]
    datos = model.req_7(sismo["seg"])
    lista = model.tabulate_req_7(datos, anio, title, prop, bins)
    lista = model.ultimos_primeros(datos)

    return lista

def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
