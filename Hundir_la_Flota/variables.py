import random
import numpy as np

dimensiones =(10,10)
filas = 10
columnas = 10
agua = " "
submarino = "B"  # Ocupa una celda
destructor = "B"  # Ocupa dos celdas
fragata = "B"  # Ocupa tres celdas
portaviones = "B" # Ocupa cuatro celdas
disparo_fallado = "X"
disparo_acertado = "O"
tablero = np.full((10,10),fill_value=" ")
cantidad_barcos_iniciales = 10
jugador_1 = "J1"
jugador_2 = "CPU"