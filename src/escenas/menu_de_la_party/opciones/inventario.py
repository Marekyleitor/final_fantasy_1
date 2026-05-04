from src.utils.constantes import ITEMS, ITEMS_OPEN_WORLD, ITEMS_TOWN, ITEMS_DUNGEON, ITEMS_BATTLE
from src.utils.constantes import ITEMS_OPEN_WORLD_ONE_ALLY, ITEMS_OPEN_WORLD_ALL_ALLIES, ITEMS_TOWN_ONE_ALLY, \
    ITEMS_TOWN_ALL_ALLIES, ITEMS_DUNGEON_ONE_ALLY, ITEMS_DUNGEON_ALL_ALLIES, ITEMS_BATTLE_ONE_ALLY, \
    ITEMS_BATTLE_ALL_ALLIES, ITEMS_BATTLE_ONE_ENEMY, ITEMS_BATTLE_ALL_ENEMIES
from src.utils.constantes import VERDE, ROJO, AZUL, RESET
from src.utils.constantes import ARMAS, ARMADURAS
from src.utils.utils import get_only_entity_name, get_only_entity_compound, get_entity_decored, \
    arma_armadura_usable_en_batalla, arma_usable_en_batalla, armadura_usable_en_batalla
import re

ansi_pattern = re.compile(r'\x1b\[[0-9;]*m')


def mostrar_items_y_cantidad(inventory):
    # Mostrar los items del inventario y su cantidad correctamente espaciado
    Entidad_space = 35
    Cantidad_space = 6

    print(f"\n\t\t{'Entidad':<{Entidad_space}}Cantidad")
    for item_name, item_quant in inventory.items():
        if item_quant > 0:
            name_aligned = ljust_ansi(item_name, Entidad_space-2)
            print(f"\t\t- {name_aligned}{item_quant:>{Cantidad_space}}")
            # print(f"\t\t- {item_name:<{Entidad_space-2}}{item_quant:>{Cantidad_space}}")
    print()

def mostrar_items_y_cantidad_en_batalla(inventory):
    # Mostrar los items del inventario y su cantidad correctamente espaciado
    Entidad_space = 35
    Cantidad_space = 10
    Tipo_space = 10  # Textos: "elemento", "armadura", "arma"

    print(f"\n\t\t{'Entidad':<{Entidad_space}}{'Cantidad':<{Cantidad_space}}{'Tipo':<{Cantidad_space}}Descripción")
    for item_name, item_quant in inventory.items():
        # es_elemento = False
        # es_arma = False
        # es_armadura = False
        tipo = ""
        descripcion = ""
        only_name = get_only_entity_name(item_name)
        if only_name in ITEMS:
            # es_elemento = True
            tipo = "elemento"
            descripcion = ITEMS[only_name]["description"]
        elif only_name in ARMAS:
            if ARMAS[only_name]["used_as_item"] == "-":
                continue
            else:
                # es_arma = True
                tipo = "arma"
                descripcion = f"Casts {ARMAS[only_name]["used_as_item"]}."
        elif only_name in ARMADURAS:
            if ARMADURAS[only_name]["used_as_item"] == "-":
                continue
            else:
                # es_armadura = True
                tipo = "armadura"
                descripcion = f"Casts {ARMADURAS[only_name]["used_as_item"]}."
        else:
            # Entidad desconocida, no se puede usar.
            continue

        if item_quant > 0:
            name_aligned = ljust_ansi(item_name, Entidad_space-2)
            cantidad_aligned = ljust_ansi(str(item_quant), Cantidad_space)
            tipo_aligned = ljust_ansi(tipo, Tipo_space)
            # print(f"\t\t- {name_aligned}{item_quant:>{Cantidad_space}}")
            print(f"\t\t- {name_aligned}{cantidad_aligned}{tipo_aligned}{descripcion}")
            # print(f"\t\t- {item_name:<{Entidad_space-2}}{item_quant:>{Cantidad_space}}")
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
    # Validar si key es un compound_name
    if " | " in key:
        key = get_entity_decored(key)  # Ahora "key" es un decored_name, ahora sí puede ser encontrado en el inventario
    # if key in dictionary:
    #     print(f"Cantidad de {VERDE}{key}{RESET} en inventario: {dictionary[key]}")
    return key in dictionary and dictionary[key] >= 1

def elementos_permitidos(partida_estado_de_juego):
    # Puede ser: Mundo Abierto, Pueblo, Dungeon, Batalla
    if partida_estado_de_juego == "Mundo Abierto":
        return ITEMS_OPEN_WORLD
    elif partida_estado_de_juego == "Pueblo":
        return ITEMS_TOWN
    elif partida_estado_de_juego == "Dungeon":
        return ITEMS_DUNGEON
    elif partida_estado_de_juego == "Batalla":
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

def has_ansi(text):
    return bool(ansi_pattern.search(text))

def strip_ansi(text):
    return ansi_pattern.sub('', text)

def parse_item(text):
    clean = strip_ansi(text)
    name, gear, mult = clean.split(' | ')
    return name, float(mult)

def inventory_sort_key(item):
    key_text = item[0]

    if not has_ansi(key_text):
        # (grupo, nombre, mult dummy)
        return (0, key_text, 0)

    name, mult = parse_item(key_text)
    return (1, name, mult)

def ljust_ansi(text, width):
    visible_len = len(strip_ansi(text))
    padding = max(0, width - visible_len)
    return text + ' ' * padding

# def inventario(arrChar, estado_de_juego, inventory):
def inventario(partida):
    while True:
        print("=== Elementos ===")
        print("1. Ver inventario")
        print("2. Usar algún elemento")
        print("3. Ordenar inventario")
        print("Q. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ## Ver inventario
            print(f"***** inventory *****")
            # print(inventory)
            mostrar_items_y_cantidad(partida.inventory)
            print(f"*****************")
            print()
        elif opcion == "2":
            print(f"***** inventory *****")
            # print(inventory)
            mostrar_items_y_cantidad(partida.inventory)
            print(f"*****************")
            print()
            while True:
                ## Usar algún elemento
                texto = input("Escriba el nombre del elemento (q: Salir): ")
                if texto.upper() == "Q":
                    break
                elif se_tiene_este_item(texto, partida.inventory):
                    if texto in elementos_permitidos(partida.estado_de_juego):
                        if ITEMS[texto]["affects"] == "one ally":
                            while True:
                                print(f"Usarás el elemento {VERDE}{texto}{RESET} en:")
                                for pj in partida.arrChar.arr:
                                    pj.mostrar_datos_3()
                                # Input
                                try:
                                    opc_a = input(f"Ingresa un indice de aliado entre 1 y {partida.arrChar.get_n()} (q: Salir): ")
                                    if opc_a.upper() == "Q":
                                        break
                                    index = int(opc_a)
                                    if 0 <= index - 1 < partida.arrChar.get_n():
                                        # Ejecutar el efecto en el pj seleccionado
                                        pj = partida.arrChar.get_char(index - 1)
                                        exitoso = usar_elemento_en_pj(texto, pj)
                                        # Disminuir en 1 el elemento en inventory
                                        if exitoso:
                                            partida.inventory[texto] = partida.inventory[texto] - 1
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
                                    for pj in partida.arrChar.arr:
                                        usar_elemento_en_pj("Elixir", pj)
                                else:
                                    print(f"Aún no se tiene registro.")
                            elif opc_b == "2":
                                break
                            else:
                                print(f"Inválido.")

                    else:
                        print(f"El elemento {texto} no se puede usar en el estado de juego {partida.estado_de_juego}.")
                        break
                # elif texto.upper() == "Q":
                #     break
                else:
                    print(f"No se posee el elemento {texto}.")
                    break
        elif opcion == "3":
            print("=== Ordenar Inventario ===")
            print("1. Alfabéticamente, armas y armaduras al final")
            print("Q. Volver")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                ## Alfabéticamente, armas y armaduras al final
                inventory_sorted = dict(
                    sorted(partida.inventory.items(), key=inventory_sort_key)
                )
                partida.inventory = inventory_sorted
                ## Ver inventario
                print(f"***** inventory *****")
                mostrar_items_y_cantidad(partida.inventory)
                print(f"*****************")
                print()
            elif opcion.upper() == "Q":
                ## Volver
                # return arrChar, estado_de_juego, inventory
                return partida

        # # Ejemplo de uso
        # print(f"{VERDE}¡Victoria!{RESET}")
        # print(f"{ROJO}¡Derrota!{RESET}")
        # print(f"{AZUL}Estado del juego:{RESET} {VERDE}100{RESET} oro")

        elif opcion.upper() == "Q":
            ## Volver
            # return arrChar, estado_de_juego, inventory
            return partida
        else:
            print(f"Opcion invalida.")

def inventario_en_batalla(partida, pj_en_turno):
    """
    Similar a inventario(), pero con la diferencia que solo se pueden usar los elementos permitidos en batalla y no se puede ordenar el inventario.
    """
    pasar_turno = False
    bool_bucle_01 = True
    bool_bucle_02 = True
    while bool_bucle_01:
        print("=== Elementos en Batalla ===")
        print("1. Ver inventario en batalla")
        print("2. Usar algún elemento en batalla")
        print("Q. Volver")

        # Si usas 1 puedes ver inventario cuantas veces quieras, al salir ('Q') no perderás el turno.
        # Si usas el 2, puedes entrar y retroceder cuantas veces quieras, pero solo si usas un elemento perderás el turno.

        opcion = input("Digita tu opción o 'Q' para Volver: ")

        if opcion == "1":
            ## Ver inventario
            print(f"***** inventory *****")
            mostrar_items_y_cantidad_en_batalla(partida.inventory)
            print(f"*****************")
            print()
            pasar_turno = False
        elif opcion == "2":
            print(f"***** inventory *****")
            mostrar_items_y_cantidad_en_batalla(partida.inventory)
            print(f"*****************")
            print()
            while bool_bucle_02:
                ## Usar algún elemento
                texto = input("Escriba el nombre del elemento (q: Salir): ")
                if texto.upper() == "Q":
                    pasar_turno = False
                    break
                elif se_tiene_este_item(texto, partida.inventory):
                    if texto in elementos_permitidos(partida.estado_de_juego):
                        # if ITEMS[texto]["affects"] == "one ally":
                        #     while True:
                        #         print(f"Usarás el elemento {VERDE}{texto}{RESET} en:")
                        #         for pj in partida.arrChar.arr:
                        #             pj.mostrar_datos_3()
                        #         # Input
                        #         try:
                        #             opc_a = input(
                        #                 f"Ingresa un indice de aliado entre 1 y {partida.arrChar.get_n()} (q: Salir): ")
                        #             if opc_a.upper() == "Q":
                        #                 break
                        #             index = int(opc_a)
                        #             if 0 <= index - 1 < partida.arrChar.get_n():
                        #                 # Ejecutar el efecto en el pj seleccionado
                        #                 pj = partida.arrChar.get_char(index - 1)
                        #                 exitoso = usar_elemento_en_pj(texto, pj)
                        #                 # Disminuir en 1 el elemento en inventory
                        #                 if exitoso:
                        #                     partida.inventory[texto] = partida.inventory[texto] - 1
                        #         except ValueError:
                        #             print("Valor inválido.")
                        partida, pasar_turno = posible_uso_de_elemento_en_batalla(partida, pj_en_turno, texto)
                        if pasar_turno:
                            bool_bucle_01 = False
                            bool_bucle_02 = False   # es lo mismo que break
                    elif arma_usable_en_batalla(texto):
                        print(f"No estan implementados los casts o magias, elige otro elemento del inventario.")
                        pasar_turno = False
                        pass
                    elif armadura_usable_en_batalla(texto):
                        print(f"No estan implementados los casts o magias, elige otro elemento del inventario.")
                        pasar_turno = False
                        pass


                    else:
                        print(f"El elemento {texto} no existe o no se puede usar en el estado de juego {partida.estado_de_juego}.")
                        break
                else:
                    print(f"No se posee el elemento {texto}.")
                    # break
        elif opcion.upper() == "Q":
            ## Volver
            bool_bucle_01 = False
        else:
            print(f"Opcion invalida.")

    return partida, pasar_turno

def posible_uso_de_elemento_en_batalla(partida, pj_en_turno, texto):
    pasar_turno = False
    if ITEMS[texto]["affects"] == "one ally":
        partida, pasar_turno = posible_uso_de_elemento_one_ally_en_batalla(partida, pj_en_turno, texto)
    elif ITEMS[texto]["affects"] == "all allies":
        partida, pasar_turno = posible_uso_de_elemento_all_allies_en_batalla(partida, pj_en_turno, texto)
    elif ITEMS[texto]["affects"] == "one enemy":
        partida, pasar_turno = posible_uso_de_elemento_one_enemy_en_batalla(partida, pj_en_turno, texto)
    elif ITEMS[texto]["affects"] == "all enemies":
        partida, pasar_turno = posible_uso_de_elemento_all_enemies_en_batalla(partida, pj_en_turno, texto)
    else:
        print(f"No se posee el elemento {texto}.")
    return partida, pasar_turno

def posible_uso_de_elemento_one_ally_en_batalla(partida, pj_en_turno, texto):
    pasar_turno = False
    # partida.arrChar: objecto arrCharacter, incluye PJs y Enemies
    obj_arrChar_per = partida.arrChar.arrPer()  # objeto arrCharacter con solo PJs
    arrPer = obj_arrChar_per.arr   # solo el []
    while True:
        print(f"{pj_en_turno.name} usará el elemento {VERDE}{texto}{RESET} en:")
        for pj in arrPer:
            pj.mostrar_datos_3()
        # Input
        try:
            opc_a = input(f"Ingresa un indice de aliado entre 1 y {obj_arrChar_per.get_n()} (q: Salir): ")
            if opc_a.upper() == "Q":
                pasar_turno = False
                break
            index = int(opc_a)
            if 0 <= index - 1 < obj_arrChar_per.get_n():
                # Ejecutar el efecto en el pj seleccionado
                pj = obj_arrChar_per.get_char(index - 1)
                exitoso = usar_elemento_en_pj(texto, pj)
                # Disminuir en 1 el elemento en inventory
                if exitoso:
                    partida.inventory[texto] = partida.inventory[texto] - 1
                    # Se usó el item, así que pasar_turno = True y sale del bucle while
                    pasar_turno = True
                    break
        except ValueError:
            print("Valor inválido.")
    return partida, pasar_turno

def posible_uso_de_elemento_all_allies_en_batalla(partida, pj_en_turno, texto):
    # partida.arrChar incluye en este momento PJs y Enemigos
    arrPer = partida.arrChar.arrPer().arr
    while True:
        pass
    pass

def posible_uso_de_elemento_one_enemy_en_batalla(partida, pj_en_turno, texto):
    # partida.arrChar incluye en este momento PJs y Enemigos
    arrEne = partida.arrChar.arrEne().arr
    while True:
        pass
    pass

def posible_uso_de_elemento_all_enemies_en_batalla(partida, pj_en_turno, texto):
    # partida.arrChar incluye en este momento PJs y Enemigos
    arrEne = partida.arrChar.arrEne().arr
    while True:
        pass
    pass

