from src.utils.constantes import ITEMS, ITEMS_OPEN_WORLD, ITEMS_TOWN, ITEMS_DUNGEON, ITEMS_BATTLE
from src.utils.constantes import ITEMS_OPEN_WORLD_ONE_ALLY, ITEMS_OPEN_WORLD_ALL_ALLIES, ITEMS_TOWN_ONE_ALLY, \
    ITEMS_TOWN_ALL_ALLIES, ITEMS_DUNGEON_ONE_ALLY, ITEMS_DUNGEON_ALL_ALLIES, ITEMS_BATTLE_ONE_ALLY, \
    ITEMS_BATTLE_ALL_ALLIES, ITEMS_BATTLE_ONE_ENEMY, ITEMS_BATTLE_ALL_ENEMIES
from src.utils.constantes import VERDE, ROJO, AZUL, RESET


def mostrar_items_y_cantidad(inventory):
    # Mostrar los items del inventario y su cantidad correctamente espaciado
    print(f"\n\t\t{'Entidad':<20}Cantidad")
    for item_name, item_quant in inventory.items():
        print(f"\t\t- {item_name:<18}{item_quant:>6}")
    print()

def se_tiene_este_item(key, dictionary):
    """
    Valida si una key existe en un diccionario y su valor es mayor o igual a 1.

    Args:
        key (str): La clave a buscar en el diccionario
        dictionary (dict): El diccionario a verificar

    Returns:
        bool: True si la key existe y su valor >= 1, False en caso contrario
    """
    return key in dictionary and dictionary[key] >= 1


def elementos_permitidos(estado_de_juego):
    # Puede ser: Mundo Abierto, Pueblo, Dungeon, Batalla
    if estado_de_juego == "Mundo Abierto":
        return ITEMS_OPEN_WORLD
    elif estado_de_juego == "Pueblo":
        return ITEMS_TOWN
    elif estado_de_juego == "Dungeon":
        return ITEMS_DUNGEON
    elif estado_de_juego == "Batalla":
        return ITEMS_BATTLE
    else:
        return []


def healing(pj, healing_HP, healing_MP, augment_HP, augment_MP):
    """
    Cura o eleva los puntos de HP o MP.
    Args:
        pj (object): Personaje Jugador (PJ)
        healing_HP (bool): Determina si se elevará el HP
        healing_MP (bool): Determina si se elevará el MP
        augment_HP (int): Cantidad en la que elevará el HP
        augment_MP (int): Cantidad en la que elevará el MP
    """
    # print(f"{pj.name}: HP: {pj.HP} + {VERDE}50{RESET}", end=" = ")
    # pj.up_or_down_HP(50)
    # print(f"{pj.HP} / {pj.HP_MAX}")
    hp_antes = 0
    hp_despues = 0
    mp_antes = 0
    mp_despues = 0
    print(f"*" * 10, f"{pj.name}", f"*" * 10)
    if healing_HP:
        hp_antes = pj.HP
        pj.up_or_down_HP(augment_HP)
        hp_despues = pj.HP
        print(f"HP: {hp_antes} + {VERDE}{hp_despues - hp_antes}{RESET} = {hp_despues} / {pj.HP_MAX}")
    if healing_MP:
        mp_antes = pj.MP
        pj.up_or_down_MP(augment_MP)
        mp_despues = pj.MP
        print(f"MP: {mp_antes} + {VERDE}{mp_despues - mp_antes}{RESET} = {mp_despues} / {pj.MP_MAX}")


def usar_elemento_en_pj(elem_text, pj):
    healing_HP, healing_MP, augment_HP, augment_MP = False, False, 0, 0
    if pj.alive:
        if elem_text == "Potion":
            # print(f"{pj.name}: HP: {pj.HP} + {VERDE}50{RESET}", end=" = ")
            # pj.up_or_down_HP(50)
            # print(f"{pj.HP} / {pj.HP_MAX}")
            healing_HP, augment_HP = True, 50
            healing(pj, healing_HP, healing_MP, augment_HP, augment_MP)
            return True
        elif elem_text == "Hi-Potion":
            # pj.up_or_down_HP(150)
            healing_HP, augment_HP = True, 150
            healing(pj, healing_HP, healing_MP, augment_HP, augment_MP)
            return True
        elif elem_text == "X-Potion":
            # pj.up_or_down_HP(pj.HP_MAX - pj.HP)
            healing_HP, augment_HP = True, pj.HP_MAX
            healing(pj, healing_HP, healing_MP, augment_HP, augment_MP)
            return True
        elif elem_text == "Ether":
            # pj.up_or_down_MP(50)
            healing_MP, augment_MP = True, 50
            healing(pj, healing_HP, healing_MP, augment_HP, augment_MP)
            return True
        elif elem_text == "Turbo Ether":
            # pj.up_or_down_MP(150)
            healing_MP, augment_MP = True, 150
            healing(pj, healing_HP, healing_MP, augment_HP, augment_MP)
            return True
        elif elem_text == "Dry Ether":
            # pj.up_or_down_MP(pj.MP_MAX - pj.MP)
            healing_MP, augment_MP = True, pj.MP_MAX
            healing(pj, healing_HP, healing_MP, augment_HP, augment_MP)
            return True
        elif elem_text == "Elixir":
            # pj.up_or_down_HP(pj.HP_MAX - pj.HP)
            # pj.up_or_down_MP(pj.MP_MAX - pj.MP)
            healing_HP, healing_MP, augment_HP, augment_MP = True, True, pj.HP_MAX, pj.MP_MAX
            healing(pj, healing_HP, healing_MP, augment_HP, augment_MP)
            return True
        elif elem_text == "Phoenix Down":
            print(f"{VERDE}Phoenix Down{RESET} no se puede usar sobre un pj con vida.")
            return False
        else:
            print(f"Valor extraño o inválido: {elem_text}")
            return False
    else:  # not pj.alive
        if elem_text == "Phoenix Down":
            pj.up_or_down_HP(pj.HP_MAX // 10)
            pj.alive = True
            return True
        elif elem_text in ["Potion", "Hi-Potion", "X-Potion", "Ether", "Turbo Ether", "Dry Ether", "Elixir"]:
            print(f"Debes revivir al pj primero antes de usar el elemento {elem_text} en él.")
            return False
        else:
            print(f"El pj debe estar vivo.")
            return False


def inventario(arrChar, estado_de_juego, inventory):
    while True:
        print("=== Elementos ===")
        print("1. Ver lista de elementos")
        print("2. Usar algún elemento")
        print("Q. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ## Ver lista de elementos
            print(f"***** inventory *****")
            # print(inventory)
            mostrar_items_y_cantidad(inventory)
            print(f"*****************")
            print()
        if opcion == "2":
            print(f"***** inventory *****")
            # print(inventory)
            mostrar_items_y_cantidad(inventory)
            print(f"*****************")
            print()
            while True:
                ## Usar algún elemento
                texto = input("Escriba el nombre del elemento (q: Salir): ")
                if texto.upper() == "Q":
                    break
                elif se_tiene_este_item(texto, inventory):
                    if texto in elementos_permitidos(estado_de_juego):
                        if ITEMS[texto]["affects"] == "one ally":
                            while True:
                                print(f"Usarás el elemento {VERDE}{texto}{RESET} en:")
                                for pj in arrChar.arr:
                                    pj.mostrar_datos_3()
                                # Input
                                try:
                                    opc_a = input(f"Ingresa un indice de aliado entre 1 y {arrChar.get_n()} (q: Salir): ")
                                    if opc_a.upper() == "Q":
                                        break
                                    index = int(opc_a)
                                    if 0 <= index - 1 < arrChar.get_n():
                                        # Ejecutar el efecto en el pj seleccionado
                                        pj = arrChar.get_char(index - 1)
                                        exitoso = usar_elemento_en_pj(texto, pj)
                                        # Disminuir en 1 el elemento en inventory
                                        if exitoso:
                                            inventory[texto] = inventory[texto] - 1
                                except ValueError:
                                    print("Valor inválido.")

                        else:  # all allies
                            print(f"Usarás el elemento {VERDE}{texto}{RESET} en todo el grupo.")
                            print("1. Usar")
                            print("2. Volver")

                            opc_b = input("Seleccione una opción: ")

                            if opc_b == "1":
                                ## Usar el elemento en todos los aliados (Megalixir, etc.)
                                if texto == "Megalixir":
                                    for pj in arrChar.arr:
                                        usar_elemento_en_pj("Elixir", pj)
                                else:
                                    print(f"Aún no se tiene registro.")
                            elif opc_b == "2":
                                break
                            else:
                                print(f"Inválido.")

                    else:
                        print(f"El elemento {texto} no se puede usar en el estado de juego {estado_de_juego}.")
                        break
                # elif texto.upper() == "Q":
                #     break
                else:
                    print(f"No se posee el elemento {texto}.")
                    break
            # while True:
            #     ## Usar algún elemento
            #     texto = input("Escriba el nombre del elemento (q: Salir): ")
            #     if texto.upper() == "Q":
            #         break
            #     while True:
            #         if se_tiene_este_item(texto, inventory):
            #             if texto in elementos_permitidos(estado_de_juego):
            #                 if ITEMS[texto]["affects"] == "one ally":
            #                     print(f"Usarás el elemento {VERDE}{texto}{RESET} en:")
            #                     for pj in arrChar.arr:
            #                         pj.mostrar_datos_3()
            #                     # Input
            #                     try:
            #                         opc = input(f"Ingresa un indice de aliado entre 1 y {arrChar.get_n()} (q: Salir): ")
            #                         if opc.upper() == "Q":
            #                             break
            #                         index = int(opc)
            #                         if 0 <= index - 1 < arrChar.get_n():
            #                             # Ejecutar el efecto en el pj seleccionado
            #                             pj = arrChar.get_char(index - 1)
            #                             exitoso = usar_elemento_en_pj(texto, pj)
            #                             # Disminuir en 1 el elemento en inventory
            #                             if exitoso:
            #                                 inventory[texto] = inventory[texto] - 1
            #                             break
            #                     except ValueError:
            #                         print("Valor inválido.")
            #                 else:  # all allies
            #                     while True:
            #                         print(f"Usarás el elemento {VERDE}{texto}{RESET} en todo el grupo.")
            #                         print("1. Usar")
            #                         print("2. Volver")
            #
            #                         opc_b = input("Seleccione una opción: ")
            #
            #                         if opc_b == "1":
            #                             ## Usar el elemento en todos los aliados (Megalixir, etc.)
            #                             if texto == "Megalixir":
            #                                 for pj in arrChar.arr:
            #                                     usar_elemento_en_pj("Elixir", pj)
            #                             else:
            #                                 print(f"Aún no se tiene registro.")
            #                         elif opc_b == "2":
            #                             break
            #                         else:
            #                             print(f"Inválido.")
            #
            #             else:
            #                 print(f"El elemento {texto} no se puede usar en el estado de juego {estado_de_juego}.")
            #                 break
            #         # elif texto.upper() == "Q":
            #         #     break
            #         else:
            #             print(f"No se posee el elemento {texto}.")
            #             break

        # # Ejemplo de uso
        # print(f"{VERDE}¡Victoria!{RESET}")
        # print(f"{ROJO}¡Derrota!{RESET}")
        # print(f"{AZUL}Estado del juego:{RESET} {VERDE}100{RESET} oro")

        elif opcion.upper() == "Q":
            ## Volver
            return arrChar, estado_de_juego, inventory
