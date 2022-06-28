import random
import numpy as np
from variables import *


def obtener_tablero_inicial():
    tablero
    return 

# Indica si una coordenada del tablero está vacía
def es_mar(x, y, tablero):
    return tablero[y][x] == agua


def coordenada_en_rango(x, y):
    return x >= 0 and x <= columnas-1 and y >= 0 and y <= filas-1


def colocar_e_imprimir_barcos(tablero, cantidad_barcos, jugador):
    barcos_uno_eslora = cantidad_barcos // 2
    barcos_dos_eslora = cantidad_barcos // 2
    barcos_tres_eslora = cantidad_barcos // 2
    barco_cuatro_eslora = cantidad_barcos // 4
    if jugador == jugador_1:
        print("Imprimiendo barcos del jugador 1 ")
    else:
        print("Imprimiendo barcos del jugador 2 ")
    print(f"Barcos de uno eslora: {barcos_uno_eslora}\nBarcos de dos eslora: {barcos_dos_eslora}\nBarcos de tres eslora: {barcos_tres_eslora}\nBarco de cuatro eslora: {barco_cuatro_eslora}Total: {barcos_uno_eslora+barcos_dos_eslora+barcos_tres_eslora+barco_cuatro_eslora}")
    # Primero colocamos los de cuatro celdas para que se acomoden bien
    tablero = colocar_barcos_de_cuatro(barco_cuatro_eslora, portaviones, tablero)
    tablero = colocar_barcos_de_tres(barcos_tres_eslora, fragata, tablero)
    tablero = colocar_barcos_de_dos(barcos_dos_eslora, destructor, tablero)
    tablero = colocar_barcos_de_una(barcos_uno_eslora, submarino, tablero)
    return tablero



def obtener_x_aleatoria():
    return random.randint(0, columnas-1)


def obtener_y_aleatoria():
    return random.randint(0, filas-1)

def colocar_barcos_de_una(cantidad, tipo_barco, tablero):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        if es_mar(x, y, tablero):
            tablero[y][x] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return tablero


def colocar_barcos_de_dos(cantidad, tipo_barco, tablero):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        x2 = x+1
        if coordenada_en_rango(x, y) and coordenada_en_rango(x2, y) and es_mar(x, y, tablero) and es_mar(x2, y, tablero):
            tablero[y][x] = tipo_barco
            tablero[y][x2] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return tablero


def colocar_barcos_de_tres(cantidad, tipo_barco, tablero):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        y3 = y+2
        if coordenada_en_rango(x, y) and coordenada_en_rango(x, y3) and es_mar(x, y, tablero) and es_mar(x, y3, tablero):
            tablero[y][x] = tipo_barco
            tablero[y3][x] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return tablero

def colocar_barcos_de_cuatro(cantidad, tipo_barco, tablero):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        x4 = x+3
        if coordenada_en_rango(x, y) and coordenada_en_rango(x4, y) and es_mar(x, y, tablero) and es_mar(x4, y, tablero):
            tablero[y][x] = tipo_barco
            tablero[y][x4] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return tablero


def imprimir_tablero(tablero, jugador):
    print(tablero,jugador)


def solicitar_coordenadas(jugador):
    print(f"Solicitando coordenadas de disparo al jugador {jugador}")
    # Ciclo infinito. Se rompe cuando ingresan una fila correcta
    y = None
    x = None
    while True:
        letra_fila = input("Ingresa una letra MAYUSCULA: ")
        # Necesitamos una letra de 1 carácter. Si no es de 1 carácter usamos continue para repetir este ciclo
        if len(letra_fila) != 1:
            print("Ingresa una letra MAYUSCULA")
            continue
        """
        Función ord que cambia las letras a ASCII y le restamos 65 que es el valor de la A
        """
        y = ord(letra_fila) - 65
        # Verificar si es válida. En caso de que sí, rompemos el ciclo
        if coordenada_en_rango(0, y):
            break
        else:
            print("Fila inválida")
    # Hacemos lo mismo pero para la columna
    while True:
        try:
            x = int(input("Ingresa el número de columna: "))
            if coordenada_en_rango(x-1, 0):
                x = x-1  # Queremos el índice, así que restamos un 1 siempre
                break
            else:
                print("Columna inválida")
        except:
            print("Ingresa un número válido")

    return x, y

def disparar(x, y, tablero):
    if es_mar(x, y, tablero):
        tablero[y][x] = disparo_fallado
        return False
    # Si ya había disparado antes, se le cuenta como falla igualmente
    elif tablero[y][x] == disparo_fallado or tablero[y][x] == disparo_acertado:
        return 
    else:
        tablero[y][x] = disparo_acertado
        return True

def disparar_cpu(tablero):
    x = obtener_x_aleatoria()
    y = obtener_y_aleatoria()
    if es_mar(x,y,tablero):
        return False
    elif tablero[y][x] == disparo_fallado or tablero[y][x] == disparo_acertado:
        return
    else:
        tablero[y][x] = disparo_acertado
        return True

def turno(jugador):
    if jugador == jugador_1:
        return jugador_2
    else:
        return jugador_1


def todos_los_barcos_hundidos(tablero):
    for y in range(filas):
        for x in range(columnas):
            celda = tablero[y][x]
            # Si no es mar o un disparo, significa que todavía hay un barco por ahí
            if celda != agua and celda != disparo_acertado and celda != disparo_fallado:
                return False
    # Acabamos de recorrer todo el tablero y no regresamos en la línea anterior. Entonces todos los barcos han sido hundidos
    return True

    
def indicar_victoria(jugador):
    print(f"Fin del juego\nEl jugador {jugador} es el ganador")


def indicar_fracaso(jugador):
    print(f"Fin del juego\nEl jugador {jugador} pierde.")


def imprimir_tablero_con_barcos(tablero_j1, tablero_cpu):
    print("Mostrando ubicación de los barcos de ambos jugadores:")
    imprimir_tablero(tablero_j1, True, jugador_1)
    imprimir_tablero(tablero_cpu, True, jugador_2)