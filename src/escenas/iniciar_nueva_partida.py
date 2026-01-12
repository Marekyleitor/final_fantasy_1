from src.clases.arrCharacter import ArrCharacter
from src.clases.pj import PJ
from src.escenas.juego import start_game


def iniciar_nueva_partida():
    while True:
        print("\n=== Iniciar Nueva Partida ===")
        print("1. Crear Personajes")
        print("Q. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
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
            nivel_objetivo = 1 # 30 # 83
            for i in range(nivel_objetivo - 1):
                for pj in [pj_1, pj_2, pj_3, pj_4]:
                    pj.Lv1UP()
                    pj.HP = pj.HP_MAX
                    # pj.MP = pj.MP_MAX

            # Start the Game
            start_game(arrChar)
        elif opcion.upper() == "Q":
            # Salir
            break