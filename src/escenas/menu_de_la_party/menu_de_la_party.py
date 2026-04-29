import os

from src.clases.arrCharacter import ArrCharacter
from src.clases.partida import Partida
# from src.clases.game_state import GameState
from src.escenas.menu_de_la_party.opciones.equipar import equipar
from src.escenas.menu_de_la_party.opciones.inventario import inventario


# def menu_de_la_party(arrChar, location, estado_de_juego, inventory, gil):
def menu_de_la_party(partida):
    while True:
        print("\n=== Menu de la Party ===")
        print("1. Inventario")
        print("2. Magia")
        print("3. Equipar")
        print("4. Estado")
        print("5. Formación")
        print("6. Configuración")
        print("7. Guardar")
        print("Q. Salir")
        print(f"Gil: {partida.gil}")

        opcion = input("Seleccione una opción: ")

        # Un return dentro de estas opciones ocasiona que salga del bucle y aquí no se quiere eso.

        if opcion == "1":
            ## Inventario
            # arrChar, estado_de_juego, inventory = inventario(arrChar, estado_de_juego, inventory)
            partida = inventario(partida)
        elif opcion == "2":
            ## Magia
            # magia()
            pass
        elif opcion == "3":
            ## Equipar
            # arrChar, inventory = equipar(arrChar, inventory)
            partida = equipar(partida)
        elif opcion == "4":
            ## Estado
            # estado()
            pass
        elif opcion == "5":
            ## Formación
            # formacion()
            pass
        elif opcion == "6":
            ## Configuración
            # configuracion()
            pass
        elif opcion == "7":
            ## Guardar
            # guardar(arrChar, location, estado_de_juego, inventory, gil)
            guardar(partida)
        elif opcion.upper() == "Q":
            ## Salir
            # return arrChar, location, estado_de_juego, inventory, gil
            return partida

# def guardar(arrChar, location, estado_de_juego, inventory, gil):
def guardar(partida):
    # partida = Partida(arrChar, location, estado_de_juego, inventory, gil)
    # partida = Partida(partida)    # Si recibe un objeto Partida, ya no tengo que crearlo
    mostrar_partidas()
    while True:
        ranura = input(f"Guardar Partida en la Ranura (1 - 10) (q: Salir): ")
        if ranura.upper() == "Q":
            break
        try:
            ranura = int(ranura)
            if 1 <= ranura <= 10:
                # Validar si existe y consultar si se quiere sobreescribir
                if os.path.exists(f"./saves/FF1-save {ranura}"):
                    if input("¿Quieres sobreescribir esta partida guardada? (S/N): ").upper() == 'S':
                        partida.guardar_partida(str(ranura))
                        break
                else:
                    partida.guardar_partida(str(ranura))
                    break
        except ValueError:
            print("Valor inválido.")

def mostrar_partidas():
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