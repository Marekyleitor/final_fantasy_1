from src.clases.arrCharacter import ArrCharacter
from src.clases.partida import Partida
# from src.clases.game_state import GameState
from src.clases.pj import PJ
from src.escenas.juego import continue_game


def iniciar_nueva_partida():
    while True:
        print("\n=== Iniciar Nueva Partida ===")
        print("1. Crear Personajes")
        print("Q. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crearPersonajes()
        elif opcion.upper() == "Q":
            # Salir
            break

def crearPersonajes():
    # Crear Personajes
    # 1. Iniciar Nueva Partida (Crear Party)
    # pj_1 = PJ('Monk', 'Fritz')  # pj_1 = PJ('Warrior', 'Escanor') # pj_1 = PJ('B. Wizard', 'Morthos')
    # pj_2 = PJ('Monk', 'Yatzo')  # pj_2 = PJ('Warrior', 'Arturo')
    # pj_3 = PJ('Monk', 'Zest')  # pj_3 = PJ('Thief', 'Robin Hood')
    # pj_4 = PJ('Monk', 'Eremita')
    pj_1 = PJ('Warrior', 'WA1')
    pj_2 = PJ('Warrior', 'WA2')
    pj_3 = PJ('Warrior', 'WA3')
    pj_4 = PJ('Warrior', 'WA4')
    ## Quitar armaduras si son Monks o Masters
    # pj_1.reemplazar_armadura('body_armor', '')
    # pj_2.reemplazar_armadura('body_armor', '')
    # pj_3.reemplazar_armadura('body_armor', '')
    # pj_4.reemplazar_armadura('body_armor', '')
    ## Equipar arma
    # pj_1.cambiar_arma('Ultima weapon')
    ## Crear el Arreglo de Personajes
    arrChar = ArrCharacter()
    arrChar.addArrChar([pj_1, pj_2, pj_3, pj_4])

    # 1.5. Leveleo y descansados
    nivel_objetivo = 1  # 30 # 83
    for i in range(nivel_objetivo - 1):
        for pj in [pj_1, pj_2, pj_3, pj_4]:
            pj.Lv1UP()
            pj.HP = pj.HP_MAX
            pj.MP = pj.MP_MAX

    # Dar valores base a "location", "estado_de_juego", "inventory" y "gil"
    # darValoresBaseALosGameState(arrChar)
    darValoresBaseALaPartida(arrChar)

# def darValoresBaseALosGameState(arrChar):
def darValoresBaseALaPartida(arrChar):
    # Seleccionar Location Inicial ("Cornelia")
    location = "Cornelia"
    estado_de_juego = "Mundo Abierto" # Puede ser: Mundo Abierto, Town, Dungeon, Batalla
    inventory = {"Potion": 10, "Hi-Potion": 8, "X-Potion": 5, "Ether": 10, "Turbo Ether": 8, "Dry Ether": 5,
                 "Elixir": 7, "Megalixir": 5, "Phoenix Down": 6, "\x1b[95mKnife | Legendary | 1.6\x1b[0m": 1,
                 "\x1b[90mKnife | Regular | 1.0\x1b[0m": 1, "\x1b[92mKnife | Superior | 1.25\x1b[0m": 1}
    gil = 500

    # # Mandar a Continuar el juego con los valores base
    # continue_game(arrChar, location, estado_de_juego, inventory, gil)

    # Crear objeto Partida con todos los valores
    partida = Partida(
        arrChar=arrChar,
        location=location,
        estado_de_juego=estado_de_juego,
        inventory=inventory,
        gil=gil
    )

    # Mandar a continuar el juego con la Partida
    continue_game(partida)