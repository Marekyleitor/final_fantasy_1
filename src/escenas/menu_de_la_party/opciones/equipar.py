import re
import copy

from src.clases.arma import Arma
from src.utils.constantes import ARMAS


def equipar(arrChar, inventory):
    while True:
        print("\n=== Equipar ===")
        print("1. Seleccionar un PJ")
        print("Q. Salir")

        opcion = input("Seleccione una opción: ")
        print()

        if opcion == "1":
            ## Seleccionar un PJ
            while True:
                mostrar_PJs(arrChar)
                try:
                    text = input(f"Ingresa un PJ entre 1 y {arrChar.get_n()}: ")
                    if text.upper() == "Q":
                        break
                    index = int(text)
                    if 0 <= index - 1 < arrChar.get_n():
                        arrChar, inventory = equipar_un_pj(arrChar, inventory, index - 1)
                except ValueError:
                    print("Valor inválido.")
        elif opcion.upper() == "Q":
            ## Salir
            return arrChar, inventory

def equipar_un_pj(arrChar, inventory, index):
    pj = arrChar.get_char(index)
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
            arrChar, inventory = equipar_2_un_pj(arrChar, inventory, index)
        elif opcion == "2":
            ## Óptimo
            pass
        elif opcion == "3":
            ## Quitar
            pass
        elif opcion.upper() == "Q":
            ## Salir
            return arrChar, inventory

def equipar_2_un_pj(arrChar, inventory, index):
    pj = arrChar.get_char(index)
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
            lista_de_nombres_de_armas_limpios = mostrar_y_obtener_armas_del_inventario_que_puede_usar(arrChar, inventory, index)
            ### Obtener el String del arma en cuentión (ej.: Knife | Legendary | 1.6) o Q para Salir.
            nombre_arma_en_inventario = get_nombre_arma_o_armadura_en_inventario(lista_de_nombres_de_armas_limpios)
            ### Validar condición
            if nombre_arma_en_inventario.upper() == "Q":
                # return arrChar, inventory # esto me retrocede a "Equipar_un_pj"
                pass # Esto me permite volver a "Equipar_2_un_pj"
            else: # cualquier nombre dentro de la lista de nombres válidos
                # Obtenemos el "nombre" (only_name) del arma y su "mult"
                nombre = get_only_entity_name(nombre_arma_en_inventario)
                mult = get_only_entity_mult(nombre_arma_en_inventario)
                # Se muestra la comparación entre los stats del PJ con el arma actual y la seleccionada
                pj_temp = copy.deepcopy(pj)
                pj_temp.cambiar_arma(nombre, mult)
                print(f"Ahora: {pj.arma.decored_name}")
                print(f"ATK: {pj.get_ATK_actualizado()}")
                print(f"ACC: {pj.get_ACC_actualizado()}")
                print(f"CRIT: {pj.get_CRIT_actualizado()}")
                print(f"Después: {pj_temp.arma.decored_name}")
                print(f"ATK: {pj_temp.get_ATK_actualizado()}")
                print(f"ACC: {pj_temp.get_ACC_actualizado()}")
                print(f"CRIT: {pj_temp.get_CRIT_actualizado()}")
                # copy.deepcopy()
                # 1. Reemplazar
                # Q. Salir
                while True:
                    print("\n=== Confirmación de reemplazo de Arma ===")
                    print("1. Reemplazar")
                    print("Q. Salir")

                    confirmacion = input("Seleccione una opción: ")

                    if confirmacion == "1":
                        arma_previa_decored_name = pj.arma.decored_name
                        pj.cambiar_arma(nombre, mult)
                        # Sumar (+1) el arma que desequipo en el inventario
                        sumar_al_inventario(1,arma_previa_decored_name, inventory)
                        # Restar (-1) el arma que equipo en el inventario
                        restar_al_inventario(1, pj.arma.decored_name, inventory)
                        return arrChar, inventory
                    elif confirmacion.upper() == "Q":
                        return arrChar, inventory

        elif opcion == "2":
            ## Shield
            pass
        elif opcion == "3":
            ## Helmet
            pass
        elif opcion == "4":
            ## Body_armor
            pass
        elif opcion == "5":
            ## Gloves
            pass
        elif opcion.upper() == "Q":
            ## Salir
            return arrChar, inventory

def mostrar_y_obtener_armas_del_inventario_que_puede_usar(arrChar, inventory, index):
    """
    Muestra las armas del inventario compatibles con el PJ en el índice recibido.

    Args:
        arrChar (ArrChar): Arreglo de Characteres, en este caso solo PJs
        inventory (dict[str: int]): El inventario.
        index (int): Index del PJ en arrChar que estamos tratando. arrChar.get_char(index).

    Returns:
        None: Solo se muestra información
    """
    pj = arrChar.get_char(index)
    armas_en_inventario = {}
    armas_que_puede_usar_en_inventario = {}
    # Recorro mi inventario
    for entity_name, quant in inventory.items():
        ## Variable para guardar solo el nombre del entity (recordar que hay decored_names)
        only_entity_name = get_only_entity_name(entity_name)
        ## Saco solo las que son armas (if ARMAS[entity_name] )
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
    mostrar_diccionario_entidad_cantidad(armas_que_puede_usar_en_inventario)
    return obtener_lista_nombres_limpios(armas_que_puede_usar_en_inventario)

def mostrar_diccionario_entidad_cantidad(dic:dict):
    # Espaciado para el nombre
    esp = 30
    print(f"\n\t{'Entity':<{esp}}Precio")
    for indice, (entity_name, quant) in enumerate(dic.items()):
        print(f"\t{indice+1}. {entity_name:<{esp-2+9}}{quant:>6}") # El +9 es por los caracteres ANSI

def obtener_lista_nombres_limpios(armas_que_puede_usar_en_inventario):
    nombres_limpios = []
    for decored_name in armas_que_puede_usar_en_inventario:
        compund_name = re.sub(r'\x1b\[[0-9;]*m', '', decored_name)  # eliminar ANSI
        nombres_limpios.append(compund_name)
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
        if nombre.upper() == "Q" or nombre in nombres_validos:
            return nombre
        try:
            indice = int(nombre) - 1
            nombre = nombres_validos[indice]
            return nombre
        except ValueError:
            pass

def sumar_al_inventario(cant, arma_decored_name, inventory):
    if arma_decored_name in inventory:
        inventory[arma_decored_name] += 1
    else:
        inventory[arma_decored_name] = 1

def restar_al_inventario(cant, arma_decored_name, inventory):
    if arma_decored_name in inventory:
        inventory[arma_decored_name] -= 1
    # else:
    #     inventory[text_entity] = 1