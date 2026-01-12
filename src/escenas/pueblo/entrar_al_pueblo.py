from src.escenas.pueblo.locales.tienda_de_items import *


def entrar_al_pueblo(arrChar, location, estado_de_juego, inventory, gil):
    estado_de_juego = "Pueblo"
    while True:
        print("\n=== Pueblo ===")
        print("1. Entrar a una tienda de Items")
        print("2. Entrar a una tienda de Armas")
        print("3. Entrar a una tienda de Armaduras")
        print("4. Entrar a una tienda de Magia Blanca")
        print("5. Entrar a una tienda de Magia Negra")
        print("6. Entrar a una Posada")
        print("Q. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ## Entrar a una tienda de Items
            arrChar, location, estado_de_juego, inventory, gil = tienda_de_items(arrChar, location, estado_de_juego, inventory, gil)
        elif opcion == "2":
            ## Entrar a una Armería

            pass
        elif opcion == "3":
            ## Entrar a una tienda de Armaduras

            pass
        elif opcion == "4":
            ## Entrar a una tienda de Magia Blanca

            pass
        elif opcion == "5":
            ## Entrar a una tienda de Magia Negra

            pass
        elif opcion == "6":
            ## Entrar a una Posada

            pass
        elif opcion.upper() == "Q":
            ## Salir
            estado_de_juego = "Mundo Abierto"
            return arrChar, location, estado_de_juego, inventory, gil