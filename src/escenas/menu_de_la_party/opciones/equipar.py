import re
import copy

from src.clases.arma import Arma
from src.clases.armadura import Armadura
from src.utils.constantes import ARMAS, ARMADURAS


# def equipar(arrChar, inventory):
def equipar(partida):
    while True:
        print("\n=== Equipar ===")
        print("1. Seleccionar un PJ")
        print("Q. Salir")

        opcion = input("Seleccione una opción: ")
        print()

        if opcion == "1":
            ## Seleccionar un PJ
            while True:
                mostrar_PJs(partida.arrChar)
                try:
                    text = input(f"Ingresa un PJ entre 1 y {partida.arrChar.get_n()}: ")
                    if text.upper() == "Q":
                        break
                    index = int(text)
                    if 0 <= index - 1 < partida.arrChar.get_n():
                        # arrChar, inventory = equipar_un_pj(arrChar, inventory, index - 1)
                        partida = equipar_un_pj(partida, index - 1)
                except ValueError:
                    print("Valor inválido.")
        elif opcion.upper() == "Q":
            ## Salir
            # return arrChar, inventory
            return partida

# def equipar_un_pj(arrChar, inventory, index):
def equipar_un_pj(partida, index):
    pj = partida.arrChar.get_char(index)
    pj.mostrar_datos_5()
    while True:
        print(f"\n=== Equipar_un_pj - {pj.name} - {pj.clase} ===")
        print("1. Equipar")
        print("2. Óptimo")
        print("3. Quitar")
        print("Q. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ## Equipar
            # arrChar, inventory = equipar_2_un_pj(arrChar, inventory, index)
            partida = equipar_2_un_pj(partida, index)
        elif opcion == "2":
            ## Óptimo
            pass
        elif opcion == "3":
            ## Quitar
            pass
        elif opcion.upper() == "Q":
            ## Salir
            # return arrChar, inventory
            return partida

# def equipar_2_un_pj(arrChar, inventory, index):
def equipar_2_un_pj(partida, index):
    pj = partida.arrChar.get_char(index)
    while True:
        print(f"\n=== Equipar_2_un_pj - {pj.name} - {pj.clase} ===")
        print("1. Arma")
        print("2. Shield")
        print("3. Helmet")
        print("4. Body_armor")
        print("5. Gloves")
        print("Q. Salir")

        opcion = input("Seleccione un arma o armadura a cambiar: ")

        if opcion == "1":
            ## Arma
            partida = equipar_arma(partida, index)
        elif opcion == "2":
            ## Shield
            partida = equipar_armadura(partida, index, 'shield')
        elif opcion == "3":
            ## Helmet
            partida = equipar_armadura(partida, index, 'helmet')
        elif opcion == "4":
            ## Body_armor
            partida = equipar_armadura(partida, index, 'body_armor')
        elif opcion == "5":
            ## Gloves
            partida = equipar_armadura(partida, index, 'gloves')
        elif opcion.upper() == "Q":
            ## Salir
            # return arrChar, inventory
            return partida

def equipar_arma(partida, index):
    pj = partida.arrChar.get_char(index)
    lista_de_nombres_de_armas_limpios = mostrar_y_obtener_armas_del_inventario_que_puede_usar(partida, index)
    ### Obtener el String del arma en cuestión (ej.: Knife | Legendary | 1.6) o Q para Salir.
    nombre_arma_en_inventario = get_nombre_arma_o_armadura_en_inventario(lista_de_nombres_de_armas_limpios)
    cambio_realizado = False
    salir_while_principal = False
    ### Validar condición
    while True:
        ### Si el cambio ya se ha realizado, break
        if cambio_realizado or salir_while_principal:
            break
        ### Validar condición
        #### En esta parte se ha mostrado las armaduras que puedo usar, sus stats y me pide ingresar el nombre o índice.
        if nombre_arma_en_inventario.upper() == "Q":
            break  # Esto me permite volver a "Equipar_2_un_pj"
        else:  # cualquier nombre dentro de la lista de nombres válidos
            # Obtenemos el "nombre" (only_name) del arma y su "mult"
            nombre = get_only_entity_name(nombre_arma_en_inventario)
            mult = get_only_entity_mult(nombre_arma_en_inventario)
            # Se muestra la comparación entre los stats del PJ con el arma actual y la seleccionada
            pj_temp = copy.deepcopy(pj)
            pj_temp.cambiar_arma(nombre, mult)
            print(f"Comparativa de stats del PJ antes y después del cambio.")
            print(f"Ahora: {pj.arma.decored_name}")
            print(f"ATK: {pj.get_ATK_actualizado()}")
            print(f"ACC: {pj.get_ACC_actualizado()}")
            print(f"CRIT: {pj.get_CRIT_actualizado()}")
            print(f"Después: {pj_temp.arma.decored_name}")
            print(f"ATK: {pj_temp.get_ATK_actualizado()}")
            print(f"ACC: {pj_temp.get_ACC_actualizado()}")
            print(f"CRIT: {pj_temp.get_CRIT_actualizado()}")
            while True:
                print("\n=== Confirmación de reemplazo de Arma ===")
                print("1. Reemplazar")
                print("Q. Salir")

                confirmacion = input("Seleccione una opción: ")

                if confirmacion == "1":
                    arma_previa_decored_name = pj.arma.decored_name
                    pj.cambiar_arma(nombre, mult)
                    # Si el arma no es "Hands", Sumar (+1) el arma que desequipó en el inventario
                    nombre_arma_previa = get_only_entity_name(arma_previa_decored_name)
                    print(f"Nombre del arma previa: {nombre_arma_previa}")
                    if nombre_arma_previa != "Hands":
                        print(f"{arma_previa_decored_name} se guardará en el inventario.")
                        sumar_al_inventario(1, arma_previa_decored_name, partida.inventory)
                    else:
                        print(f"No poseías arma anteriormente, nada se guardará en el inventario.")
                    # Restar (-1) el arma que equipó en el inventario
                    restar_al_inventario(1, pj.arma.decored_name, partida.inventory)
                    # Cambio ya ha sido realizado, para que no muestre cambiar una armadura por la misma.
                    cambio_realizado = True
                    break
                elif confirmacion.upper() == "Q":
                    # Salir del while principal aunque no haya habido cambio
                    salir_while_principal = True
                    break
    return partida

# def mostrar_y_obtener_armas_del_inventario_que_puede_usar(arrChar, inventory, index):
def mostrar_y_obtener_armas_del_inventario_que_puede_usar(partida, index):
    """
    Muestra las armas del inventario compatibles con el PJ en el índice recibido.

    Args:
        partida (Partida): El estado del juego.
            .arrChar (ArrChar): Arreglo de Characteres, en este caso solo PJs
            .inventory (dict[str: int]): El inventario.
        index (int): Index del PJ en arrChar que estamos tratando. arrChar.get_char(index).

    Returns:
        None: Solo se muestra información
    """
    pj = partida.arrChar.get_char(index)
    armas_en_inventario = {}
    armas_que_puede_usar_en_inventario = {}
    # Recorro mi inventario
    for entity_name, quant in partida.inventory.items():
        ## Variable para guardar solo el nombre del entity (recordar que hay decored_names)
        only_entity_name = get_only_entity_name(entity_name)
        ## Saco solo las que son armas
        if only_entity_name in ARMAS and quant > 0:
            armas_en_inventario[entity_name] = quant
    # Recorro armas_en_inventario
    for arma_name, quant in armas_en_inventario.items():
        ## Variable para guardar solo el nombre del arma
        only_arma_name = get_only_entity_name(arma_name)
        ## Variable para guardar solo el mult del arma (si no tiene, 1.0)
        only_arma_mult = get_only_entity_mult(arma_name)
        ## Filtro las que pueda usar esta clase
        clases_que_pueden_usar_esta_arma = Arma(only_arma_name, only_arma_mult).equip_by
        if pj.clase in clases_que_pueden_usar_esta_arma and quant > 0:
            armas_que_puede_usar_en_inventario[arma_name] = quant
    mostrar_diccionario_entidad_cantidad_atk_acc_crit(armas_que_puede_usar_en_inventario)
    return obtener_lista_nombres_limpios(armas_que_puede_usar_en_inventario)

def mostrar_diccionario_entidad_cantidad_atk_acc_crit(dic:dict):
    # # Espaciado para el nombre
    # esp = 30
    # print(f"\n\t{'Entity':<{esp}}Precio")
    # for indice, (entity_name, quant) in enumerate(dic.items()):
    #     print(f"\t{indice+1}. {entity_name:<{esp-2+9}}{quant:>6}") # El +9 es por los caracteres ANSI

    # Espaciado para el nombre
    esp = 40
    print(f"\n\t{'Entity':<{esp}}Quant\tAtk\tAcc\tCrit")
    for indice, (entity_name, quant) in enumerate(dic.items()):
        # Separar el decored_name en "nombre" y "mult".
        nombre = get_only_entity_name(entity_name)
        mult = get_only_entity_mult(entity_name)
        # Crear un arma temporal con ese nombre y mult
        weapon_temp = Arma(nombre, mult)
        atk_temp = weapon_temp.atk  # Ya está multiplicado con su mult
        acc_temp = weapon_temp.acc  # Ya está multiplicado con su mult
        crit_temp = weapon_temp.crit  # Ya está multiplicado con su mult
        # print(f"\t{indice + 1}. {entity_name:<{esp - 3 + 9}}\033[41m{quant:>5}\033[0m\t{atk_temp}\t{acc_temp}\t{crit_temp}")  # El +9 es por los caracteres ANSI
        print(f"\t{indice + 1}. {entity_name:<{esp - 3 + 9}}{quant:>5}\t{atk_temp}\t{acc_temp}\t{crit_temp}")  # El +9 es por los caracteres ANSI

def equipar_armadura(partida, index, slot_armor_str):
    pj = partida.arrChar.get_char(index)
    lista_de_nombres_de_armaduras_limpios = mostrar_y_obtener_armaduras_del_inventario_que_puede_usar(partida, index, slot_armor_str)
    ### Obtener el String de la armadura en cuestión (ej.: Knife | Legendary | 1.6) o Q para Salir.
    nombre_armadura_en_inventario = get_nombre_arma_o_armadura_en_inventario(lista_de_nombres_de_armaduras_limpios)
    cambio_realizado = False
    salir_while_principal = False
    while True:
        ### Si el cambio ya se ha realizado, break
        if cambio_realizado or salir_while_principal:
            break
        ### Validar condición
        #### En esta parte se ha mostrado las armaduras que puedo usar, sus stats y me pide ingresar el nombre o índice.
        if nombre_armadura_en_inventario.upper() == "Q":
            break  # Esto me permite volver a "Equipar_2_un_pj"
        else:  # cualquier nombre dentro de la lista de nombres válidos
            # Obtenemos el "nombre" (only_name) de la armadura y su "mult"
            nombre = get_only_entity_name(nombre_armadura_en_inventario)
            mult = get_only_entity_mult(nombre_armadura_en_inventario)
            # Se muestra la comparación entre los stats del PJ con la armadura actual y la seleccionada
            pj_temp = copy.deepcopy(pj)
            pj_temp.cambiar_armadura(slot_armor_str, nombre, mult)
            print(f"Comparativa de stats del PJ antes y después del cambio.")
            print(f"Ahora: {getattr(pj, slot_armor_str).decored_name}")
            print(f"DEF: {pj.get_DEF_actualizado()}")
            print(f"EVA: {pj.get_EVA_actualizado()}")
            print(f"WEI: {pj.get_WEI_actualizado()}")
            print(f"Después: {getattr(pj_temp, slot_armor_str).decored_name}")
            print(f"DEF: {pj_temp.get_DEF_actualizado()}")
            print(f"EVA: {pj_temp.get_EVA_actualizado()}")
            print(f"WEI: {pj_temp.get_WEI_actualizado()}")
            while True:
                print("\n=== Confirmación de reemplazo de Armadura ===")
                print("1. Reemplazar")
                print("Q. Salir")

                confirmacion = input("Seleccione una opción: ")

                if confirmacion == "1":
                    armadura_previa_decored_name = getattr(pj, slot_armor_str).decored_name
                    pj.cambiar_armadura(slot_armor_str, nombre, mult)
                    # Si la armadura no es "", Sumar (+1) la armadura que desequipó en el inventario
                    nombre_armadura_previa = get_only_entity_name(armadura_previa_decored_name)
                    print(f"Nombre de la armadura previa: {nombre_armadura_previa}")
                    if nombre_armadura_previa != "":
                        print(f"{armadura_previa_decored_name} se guardará en el inventario.")
                        sumar_al_inventario(1, armadura_previa_decored_name, partida.inventory)
                    else:
                        print(f"No poseías armadura anteriormente, nada se guardará en el inventario.")
                    # Restar (-1) la armadura que equipó en el inventario
                    restar_al_inventario(1, getattr(pj, slot_armor_str).decored_name, partida.inventory)
                    # Cambio ya ha sido realizado, para que no muestre cambiar una armadura por la misma.
                    cambio_realizado = True
                    break
                elif confirmacion.upper() == "Q":
                    # Salir del while principal aunque no haya habido cambio
                    salir_while_principal = True
                    break
    return partida

def mostrar_y_obtener_armaduras_del_inventario_que_puede_usar(partida, index, slot_armor_str):
    """
        Muestra las armaduras del inventario de tipo slot_armor_str compatibles con el PJ en el índice recibido.

        Args:
            partida (Partida): El estado del juego.
                .arrChar (ArrChar): Arreglo de Characteres, en este caso solo PJs
                .inventory (dict[str: int]): El inventario.
            index (int): Index del PJ en arrChar que estamos tratando. arrChar.get_char(index).

        Returns:
            None: Solo se muestra información
        """
    pj = partida.arrChar.get_char(index)
    armaduras_en_inventario = {}
    armaduras_que_puede_usar_en_inventario = {}
    # Recorro mi inventario
    for entity_name, quant in partida.inventory.items():
        ## Variable para guardar solo el nombre del entity (recordar que hay decored_names)
        only_entity_name = get_only_entity_name(entity_name)
        ## Saco solo las que son armaduras
        if only_entity_name in ARMADURAS and quant:
            armaduras_en_inventario[entity_name] = quant
    # Recorro armaduras_en_inventario
    for armadura_name, quant in armaduras_en_inventario.items():
        ## Variable para guardar solo el nombre de la armadura
        only_armadura_name = get_only_entity_name(armadura_name)
        ## Variable para guardar solo el mult del armadura (si no tiene, 1.0)
        only_armadura_mult = get_only_entity_mult(armadura_name)
        ## Filtro las que pueda usar esta clase y tipo de armadura slot_armor_str
        armadura_temp = Armadura(only_armadura_name, only_armadura_mult)
        ### En cada armadura se verá qué clases la pueden usar
        clases_que_pueden_usar_esta_armadura = armadura_temp.equip_by
        ### Un booleano que servirá para filtrar por slot_armor_str
        slot_de_armadura_correcta = armadura_temp.type == slot_armor_str.replace("_", " ")
        if slot_de_armadura_correcta and pj.clase in clases_que_pueden_usar_esta_armadura and quant > 0:
            armaduras_que_puede_usar_en_inventario[armadura_name] = quant
    mostrar_diccionario_entidad_cantidad_def_eva_wei(armaduras_que_puede_usar_en_inventario)
    return obtener_lista_nombres_limpios(armaduras_que_puede_usar_en_inventario)

def mostrar_diccionario_entidad_cantidad_def_eva_wei(dic:dict):
    # Espaciado para el nombre
    esp = 40
    print(f"\n\t{'Entity':<{esp}}Quant\tDEF\tEVA\tWEI")
    for indice, (entity_name, quant) in enumerate(dic.items()):
        # Separar el decored_name en "nombre" y "mult".
        nombre = get_only_entity_name(entity_name)
        mult = get_only_entity_mult(entity_name)
        # Crear un arma temporal con ese nombre y mult
        armor_temp = Armadura(nombre, mult)
        DEF_temp = armor_temp.DEF  # Ya está multiplicado con su mult
        EVA_temp = armor_temp.EVA  # Ya está multiplicado con su mult
        WEI_temp = armor_temp.WEI  # Ya está multiplicado con su mult
        print(f"\t{indice + 1}. {entity_name:<{esp - 3 + 9}}{quant:>5}\t{DEF_temp}\t{EVA_temp}\t{WEI_temp}")  # El +9 es por los caracteres ANSI

def obtener_lista_nombres_limpios(armas_que_puede_usar_en_inventario):
    nombres_limpios = []
    for decored_name in armas_que_puede_usar_en_inventario:
        compound_name = re.sub(r'\x1b\[[0-9;]*m', '', decored_name)  # eliminar ANSI
        nombres_limpios.append(compound_name)
    return nombres_limpios

def get_only_entity_name(possibly_decored_name):
    limpio = re.sub(r'\x1b\[[0-9;]*m', '', possibly_decored_name)  # eliminar ANSI
    nombre = limpio.split(" | ")[0]  # obtener solo el nombre
    return nombre

def get_only_entity_mult(possibly_decored_name):
    limpio = re.sub(r'\x1b\[[0-9;]*m', '', possibly_decored_name)  # eliminar ANSI
    mult = 1.0
    if " | " in limpio:
        mult = float(limpio.split(" | ")[2])  # obtener solo el mult
    return mult

def mostrar_PJs(arrChar):
    esp = [12, 12, 8]
    for indice, pj in enumerate(arrChar.arr):
        nombre = pj.name
        clase = pj.clase
        nivel = f"LV. {pj.LV}"
        print(f"{indice+1}. {nombre:<{esp[0]}}{clase:<{esp[1]}}{nivel:<{esp[2]}}")

def get_nombre_arma_o_armadura_en_inventario(nombres_validos):
    """
    Se requiere que se escriba el nombre del arma o armadura a la cual quieres visualizar el cambio de stats
    Args:
        nombres_validos (dict[str: int]): El inventario.
    Returns:
        nombre (str): Nombre del arma, armadura o una "Q".
    """
    while True:
        nombre = input("\nEscriba el nombre o índice: ")
        if nombre.upper() == "Q":
            return nombre
        if nombre in nombres_validos:
            return nombre
        # Intentar como índice numérico
        try:
            indice = int(nombre) - 1  # Convertir a 0-based
            if 0 <= indice < len(nombres_validos):
                return nombres_validos[indice]
            else:
                if len(nombres_validos) == 0:
                    print(f"La lista está vacía, retorne con la letra 'Q'.")
                elif len(nombres_validos) == 1:
                    print(f"Índice fuera de rango. Solo hay 1 opción disponible.")
                else:
                    print(f"Índice fuera de rango. Debe ser entre 1 y {len(nombres_validos)}.")
            # nombre = nombres_validos[indice]
            # return nombre
        except ValueError:
            print("Entrada inválida. Escribe un nombre o un número válido.")

def sumar_al_inventario(cant, arma_decored_name, inventory):
    if arma_decored_name in inventory:
        inventory[arma_decored_name] += cant
    else:
        inventory[arma_decored_name] = cant

def restar_al_inventario(cant, arma_decored_name, inventory):
    if arma_decored_name in inventory:
        inventory[arma_decored_name] -= cant
    # No puedes restar un objeto que no está en tu inventario
    # else:
    #     inventory[text_entity] = cant