from src.clases.arrCharacter import ArrCharacter
from src.escenas.batalla.batalla import batalla
from src.escenas.menu_de_la_party.menu_de_la_party import menu_de_la_party
from src.escenas.pueblo.entrar_al_pueblo import entrar_al_pueblo
from src.utils.constantes import all_armas_locations, all_armaduras_locations, all_items_locations, all_locations
from src.utils.constantes import VERDE, ROJO, AZUL, RESET


def start_game(arrChar):
    # # 1.5. Leveleo y descansados
    # nivel_objetivo = 83
    # for i in range(nivel_objetivo - 1):
    #     for pj in arrChar.arr:
    #         pj.Lv1UP()
    #         pj.HP = pj.HP_MAX
    #         pj.MP = pj.MP_MAX
    # 2. Seleccionar Location Inicial ("Cornelia")
    location = "Cornelia"
    estado_de_juego = "Mundo Abierto" # Puede ser: Mundo Abierto, Town, Dungeon, Batalla
    inventory = {"Potion": 10, "Hi-Potion": 8, "X-Potion": 5, "Ether": 10, "Turbo Ether": 8, "Dry Ether": 5,
                 "Elixir": 7, "Megalixir": 5, "Phoenix Down": 6, "\x1b[95mKnife | Legendary | 1.6\x1b[0m": 1,
                 "\x1b[90mKnife | Regular | 1.0\x1b[0m": 1, "\x1b[92mKnife | Superior | 1.25\x1b[0m": 1}
    gil = 500

    while True:
        print("\n=== ¿Qué deseas hacer? ===")
        print("1. Entrar al Pueblo")
        print("2. Buscar batalla")
        print("3. Menu de la Party")
        print("4. Viajar")
        print("Q. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ## Entrar al Pueblo
            # arrChar, location, estado_de_juego, inventory, gil = entrar_al_pueblo(arrChar, location, estado_de_juego, inventory, gil)
            pass
        elif opcion == "2":
            ## Buscar batalla
            ultimo_estado_de_juego = estado_de_juego    # guarda el último estado_de_juego
            arrChar, location, estado_de_juego, inventory, gil = batalla(arrChar, location, estado_de_juego, inventory, gil)
            if estado_de_juego == "Batalla":
                estado_de_juego = ultimo_estado_de_juego
        elif opcion == "3":
            ## Menu de la Party
            arrChar, location, estado_de_juego, inventory, gil = menu_de_la_party(arrChar, location, estado_de_juego, inventory, gil)
        elif opcion == "4":
            ## Viajar
            while True:
                print("\n=== Viajar ===")
                print("1. Ver todos los lugares. ")
                print("2. Donde hay armas (Buy y Find).")
                print("3. Donde hay armadurass (Buy y Find).")
                print("4. Donde hay Items (Buy y Find).")
                print("5. Escribir el destino.")

                opcion_de_viaje = input("Seleccione tu opción de viaje (q: Salir): ")

                if opcion_de_viaje.upper() == "Q":
                    break
                try:
                    opcion_de_viaje = int(opcion_de_viaje)
                    print()
                    if opcion_de_viaje == 1:
                        for indice, location in all_locations:
                            print(f"  {indice}) {location}")
                    elif opcion_de_viaje == 2:
                        for indice, location in all_armas_locations:
                            print(f"  {indice}) {location}")
                    elif opcion_de_viaje == 3:
                        for indice, location in all_armaduras_locations:
                            print(f"  {indice}) {location}")
                    elif opcion_de_viaje == 4:
                        for indice, location in all_items_locations:
                            print(f"  {indice}) {location}")
                    elif opcion_de_viaje == 5:
                        while True:
                            destino_de_viaje = input("Seleccione tu opción de viaje (q: Salir): ")
                            if destino_de_viaje.upper() == "Q":
                                break
                            elif destino_de_viaje in all_locations:
                                location = destino_de_viaje
                                print(f"Location ahora es {AZUL}{location}{RESET}")

                except ValueError:
                    print("Valor inválido.")


            # if input(f"Lugar de destino: ")
        elif opcion.upper() == "Q":
            ## Salir
            if input("¿Estás seguro que quieres salir? Perderás el progreso no guardado.? (S/N): ").upper() == 'S':
                break
            else:
                pass

def continue_game(arrChar, location, estado_de_juego, inventory, gil):
    while True:
        print("\n=== ¿Qué deseas hacer? ===")
        print("1. Entrar al Pueblo")
        print("2. Buscar batalla")
        print("3. Menu de la Party")
        print("4. Viajar")
        print("Q. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ## Entrar al Pueblo
            arrChar, location, estado_de_juego, inventory, gil = entrar_al_pueblo(arrChar, location, estado_de_juego, inventory, gil)
        elif opcion == "2":
            ## Buscar batalla
            ultimo_estado_de_juego = estado_de_juego  # guarda el último estado_de_juego
            arrChar, location, estado_de_juego, inventory, gil = batalla(arrChar, location, estado_de_juego, inventory, gil)
            if estado_de_juego == "Batalla":
                estado_de_juego = ultimo_estado_de_juego
        elif opcion == "3":
            ## Menu de la Party
            arrChar, location, estado_de_juego, inventory, gil = menu_de_la_party(arrChar, location, estado_de_juego, inventory, gil)
        elif opcion == "4":
            ## Viajar
            while True:
                print("\n=== Viajar ===")
                print("1. Ver todos los lugares. ")
                print("2. Donde hay armas (Buy y Find).")
                print("3. Donde hay armadurass (Buy y Find).")
                print("4. Donde hay Items (Buy y Find).")
                print("5. Escribir el destino.")

                opcion_de_viaje = input("Seleccione tu opción de viaje (q: Salir): ")

                if opcion_de_viaje.upper() == "Q":
                    break
                try:
                    opcion_de_viaje = int(opcion_de_viaje)
                    print()
                    if opcion_de_viaje == 1:
                        for indice, location in enumerate(all_locations):
                            print(f"  {indice}) {location}")
                    elif opcion_de_viaje == 2:
                        for indice, location in enumerate(all_armas_locations):
                            print(f"  {indice}) {location}")
                    elif opcion_de_viaje == 3:
                        for indice, location in enumerate(all_armaduras_locations):
                            print(f"  {indice}) {location}")
                    elif opcion_de_viaje == 4:
                        for indice, location in enumerate(all_items_locations):
                            print(f"  {indice}) {location}")
                    elif opcion_de_viaje == 5:
                        while True:
                            destino_de_viaje = input("Lugar de destino (q: Salir): ")
                            if destino_de_viaje.upper() == "Q":
                                break
                            elif destino_de_viaje in all_locations:
                                location = destino_de_viaje
                                print(f"Location ahora es {AZUL}{location}{RESET}")

                except ValueError:
                    print("Valor inválido.")


            # if input(f"Lugar de destino: ")
        elif opcion.upper() == "Q":
            ## Salir
            if input("¿Estás seguro que quieres salir? Perderás el progreso no guardado.? (S/N): ").upper() == 'S':
                break
            else:
                pass