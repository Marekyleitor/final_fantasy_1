from src.clases.arrCharacter import ArrCharacter
from src.escenas.batalla.batalla import batalla
from src.escenas.menu_de_la_party.menu_de_la_party import menu_de_la_party
from src.escenas.pueblo.entrar_al_pueblo import entrar_al_pueblo
from src.utils.constantes import all_armas_locations, all_armaduras_locations, all_items_locations, all_locations
from src.utils.constantes import VERDE, ROJO, AZUL, RESET


# def continue_game(arrChar, location, estado_de_juego, inventory, gil):
def continue_game(partida):
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
            partida = entrar_al_pueblo(partida)
        elif opcion == "2":
            ## Buscar batalla
            ultimo_estado_de_juego = partida.estado_de_juego  # guarda el último estado_de_juego
            partida = batalla(partida)
            if partida.estado_de_juego == "Batalla":
                partida.estado_de_juego = ultimo_estado_de_juego
        elif opcion == "3":
            ## Menu de la Party
            partida = menu_de_la_party(partida)
        elif opcion == "4":
            ## Viajar
            while True:
                print(f"\n=== Viajar === Actualmente en {AZUL}{partida.location}{RESET}")
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
                        for indice, place in enumerate(all_locations):
                            print(f"  {indice}) {place}")
                    elif opcion_de_viaje == 2:
                        for indice, place in enumerate(all_armas_locations):
                            print(f"  {indice}) {place}")
                    elif opcion_de_viaje == 3:
                        for indice, place in enumerate(all_armaduras_locations):
                            print(f"  {indice}) {place}")
                    elif opcion_de_viaje == 4:
                        for indice, place in enumerate(all_items_locations):
                            print(f"  {indice}) {place}")
                    elif opcion_de_viaje == 5:
                        while True:
                            destino_de_viaje = input("Lugar de destino (q: Salir): ")
                            if destino_de_viaje.upper() == "Q":
                                break
                            elif destino_de_viaje in all_locations:
                                partida.location  = destino_de_viaje
                                print(f"Location ahora es {AZUL}{partida.location}{RESET}")

                except ValueError:
                    print("Valor inválido.")


        elif opcion.upper() == "Q":
            ## Salir
            if input("¿Estás seguro que quieres salir? Perderás el progreso no guardado.? (S/N): ").upper() == 'S':
                break
            else:
                pass