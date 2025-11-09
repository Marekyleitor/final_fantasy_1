from src.clases.arrCharacter import ArrCharacter
from src.escenas.batalla.batalla import batalla

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
    escena_de_juego = "Mundo Abierto"

    while True:
        print("\n=== ¿Qué deseas hacer? ===")
        print("1. Entrar al Pueblo")
        print("2. Buscar batalla")
        print("3. Menu de la Party")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ## Entrar al Pueblo
            # entrar_al_pueblo()
            pass
        elif opcion == "2":
            ## Buscar batalla
            escena_de_juego = "Batalla"
            batalla(arrChar, location)
            escena_de_juego = "Mundo Abierto"
            pass
        elif opcion == "3":
            ## Menu de la Party
            # menu_de_la_party()
            pass
        elif opcion == "4":
            ## Salir
            if input("¿Estás seguro que quieres salir? Perderás el progreso no guardado.? (S/N): ").upper() == 'S':
                break
            else:
                pass
