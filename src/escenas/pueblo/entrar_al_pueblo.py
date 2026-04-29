from src.escenas.pueblo.locales.tienda_de_items import *


# def entrar_al_pueblo(arrChar, location, estado_de_juego, inventory, gil):
def entrar_al_pueblo(partida):
    partida.estado_de_juego = "Pueblo"
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
        # No es necesario el return en cada opción, lo que se quiere es que al volver a este punto se te vuelva a preguntar que quieres hasta que quieras salir.
        if opcion == "1":
            ## Entrar a una tienda de Items
            # arrChar, location, estado_de_juego, inventory, gil = tienda_de_items(arrChar, location, estado_de_juego, inventory, gil)
            partida = tienda_de_items(partida)
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
            partida.estado_de_juego = "Mundo Abierto"
            # return arrChar, location, estado_de_juego, inventory, gil
            return partida