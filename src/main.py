from src.escenas.iniciar_nueva_partida import iniciar_nueva_partida

def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Iniciar Nueva Partida")
        print("2. Continuar")
        print("3. Opciones")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ## Inicializar nueva partida
            iniciar_nueva_partida()
        elif opcion == "2":
            ## Continuar partida guardada
            # cargar_partida()
            pass
        elif opcion == "3":
            ## Menú de opciones
            # menu_opciones()
            pass
        elif opcion == "4":
            break


if __name__ == "__main__":
    main()