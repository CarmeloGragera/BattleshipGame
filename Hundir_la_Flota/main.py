import random
import numpy as np
from funciones import *
from variables import *

def jugar():
    cantidad_barcos=5
    tablero_j1, tablero_cpu = tablero, tablero
    tablero_j1 = colocar_e_imprimir_barcos(tablero_j1,cantidad_barcos, jugador_1)
    tablero_cpu = colocar_e_imprimir_barcos(tablero_cpu,cantidad_barcos, jugador_2)
    turno_actual = jugador_1
    while True:
        imprimir_tablero(tablero,jugador_1)
        print(f"Turno de {turno_actual}")
        if turno_actual == jugador_1:
            
            x, y = solicitar_coordenadas(turno_actual)
            acertado = disparar(x, y, tablero_cpu)
        
        elif turno_actual== jugador_2:
            
            acertado = disparar_cpu(tablero_j1)
        

        if acertado:
            print("Disparo acertado")
            if todos_los_barcos_hundidos(tablero_cpu):
                indicar_victoria(turno_actual)
                   # imprimir_tablero_con_barcos(tablero_j1, tablero_cpu)
                break
            else: 
                disparo_fallado
                print("Disparo fallado")
                turno_actual = turno(turno_actual)
         
jugar()