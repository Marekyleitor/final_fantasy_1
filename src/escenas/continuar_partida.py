import os

from src.clases.partida import Partida
from src.escenas.juego import continue_game

def continuar_partida(partida):
    arrChar = partida.arrChar
    location =partida.location
    estado_de_juego = partida.estado_de_juego
    inventory = partida.inventory
    gil = partida.gil
    continue_game(arrChar, location, estado_de_juego, inventory, gil)

def mostrar_partidas_en_paquete_saves():
    # ruta_al_archivo = "./saves/FF1-save "
    # nombre_archivo = "FF1-save "
    print()
    for i in range(1, 11):
        ruta_al_archivo = "./saves/FF1-save " + str(i)
        # ruta_al_archivo = ruta_al_archivo + str(i)
        if os.path.exists(ruta_al_archivo):
            nombre_archivo = "FF1-save " + str(i)
            # nombre_archivo = nombre_archivo + str(i)
            print(f"{i}. {nombre_archivo}.")
        else:
            print(f"{i}. -")