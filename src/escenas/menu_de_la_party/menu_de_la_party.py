import os

from src.clases.arrCharacter import ArrCharacter
from src.escenas.menu_de_la_party.opciones.equipar import equipar
from src.escenas.menu_de_la_party.opciones.inventario import inventario
from src.clases.partida import Partida

def menu_de_la_party(arrChar, location, estado_de_juego, inventory, gil):
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
        print(f"Gil: {gil}")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ## Inventario
            arrChar, estado_de_juego, inventory = inventario(arrChar, estado_de_juego, inventory)
            # return arrChar, location, estado_de_juego, inventory, gil
        elif opcion == "2":
            ## Magia
            # magia()
            pass
        elif opcion == "3":
            ## Equipar
            arrChar, inventory = equipar(arrChar, inventory)
        if opcion == "4":
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
            guardar(arrChar, location, estado_de_juego, inventory, gil)
        elif opcion.upper() == "Q":
            ## Salir
            return arrChar, location, estado_de_juego, inventory, gil

def guardar(arrChar, location, estado_de_juego, inventory, gil):
    partida = Partida(arrChar, location, estado_de_juego, inventory, gil)
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