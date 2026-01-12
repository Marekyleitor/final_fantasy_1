from src.escenas.iniciar_nueva_partida import iniciar_nueva_partida
from src.escenas.continuar_partida import continuar_partida, mostrar_partidas_en_paquete_saves
from src.clases.partida import Partida
import os.path

def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Iniciar Nueva Partida")
        print("2. Continuar")
        print("3. Opciones")
        print("Q. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ## Inicializar nueva partida
            iniciar_nueva_partida()
        elif opcion == "2":
            ## Continuar partida guardada
            while True:
                try:
                    mostrar_partidas_en_paquete_saves()
                    ranura = int(input(f"Cargar Partida de la Ranura (1 - 10): "))
                    if 1 <= ranura <= 10:
                        if os.path.exists(f"./saves/FF1-save {ranura}"):
                            partida = Partida()
                            partida = partida.cargar_partida(str(ranura))
                            break
                        else:
                            print(f"Esta Partida no existe, elige otra.")
                except ValueError:
                    print("Valor inválido.")
            continuar_partida(partida)
        elif opcion == "3":
            ## Menú de opciones
            # menu_opciones()
            pass
        elif opcion.upper() == "Q":
            break


if __name__ == "__main__":
    main()