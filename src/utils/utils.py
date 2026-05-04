from src.utils.constantes import ITEMS, ITEMS_OPEN_WORLD, ITEMS_TOWN, ITEMS_DUNGEON, ITEMS_BATTLE
from src.utils.constantes import ITEMS_OPEN_WORLD_ONE_ALLY, ITEMS_OPEN_WORLD_ALL_ALLIES, ITEMS_TOWN_ONE_ALLY, \
    ITEMS_TOWN_ALL_ALLIES, ITEMS_DUNGEON_ONE_ALLY, ITEMS_DUNGEON_ALL_ALLIES, ITEMS_BATTLE_ONE_ALLY, \
    ITEMS_BATTLE_ALL_ALLIES, ITEMS_BATTLE_ONE_ENEMY, ITEMS_BATTLE_ALL_ENEMIES
from src.utils.constantes import VERDE, ROJO, AZUL, RESET
from src.utils.constantes import ARMAS, ARMADURAS
from src.clases.arma import Arma
from src.clases.armadura import Armadura
from src.utils.constantes import ARMAS, ARMADURAS
import re
import copy


ansi_pattern = re.compile(r'\x1b\[[0-9;]*m')


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

def get_only_entity_compound(possibly_decored_name):
    limpio = re.sub(r'\x1b\[[0-9;]*m', '', possibly_decored_name)  # eliminar ANSI
    return limpio

def get_entity_decored(possibly_compound_name):
    nombre = get_only_entity_name(possibly_compound_name)
    mult = get_only_entity_mult(possibly_compound_name)
    decored_name = Arma(nombre, mult).decored_name
    return decored_name

def arma_usable_en_batalla(texto):
    nombre = get_only_entity_name(texto)
    if nombre in ARMAS:
        text_in_used_as_item = ARMAS[nombre]['used_as_item']
        if "-" == text_in_used_as_item:
            return True
    else:
        return False

def armadura_usable_en_batalla(texto):
    nombre = get_only_entity_name(texto)
    if nombre in ARMADURAS:
        text_in_used_as_item = ARMADURAS[nombre]['used_as_item']
        if "-" == text_in_used_as_item:
            return True
    else:
        return False

def arma_armadura_usable_en_batalla(texto):
    nombre = get_only_entity_name(texto)
    if arma_usable_en_batalla(texto) or armadura_usable_en_batalla(texto):
        return True
    else:
        return False