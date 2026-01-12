# utils/constantes.py
import csv
import os

# Definir colores
VERDE = '\033[32m'
ROJO = '\033[31m'
AZUL = '\033[34m'
# RESET = '\033[0m'

# Carácter de escape ANSI (ESC)
ESC = '\033'

# Códigos de estilo/formato
RESET = f'{ESC}[0m'
BOLD = f'{ESC}[1m'
ITALICS = f'{ESC}[1m'
UNDERLINE = f'{ESC}[4m'
INVERSE = f'{ESC}[7m' # Invierte foreground y background
CROSSEDOUT = STRIKETHROUGH = f'{ESC}[9m' # Crossed-out on
FORTUNDERLINE = f'{ESC}[21m'

# Colores de primer plano (Foreground) estándar
FG_BLACK = f'{ESC}[30m'
FG_RED = f'{ESC}[31m'
FG_GREEN = f'{ESC}[32m'
FG_YELLOW = f'{ESC}[33m'
FG_BLUE = f'{ESC}[34m'
FG_MAGENTA = f'{ESC}[35m'
FG_CYAN = f'{ESC}[36m'
FG_LIGHT_GRAY = f'{ESC}[37m' # Alias para blanco/gris claro
#FG_WHITE = f'{ESC}[38m' # Default Foreground color (Light-Light gray)

# Colores de fondo (Background) estándar
BG_BLACK = f'{ESC}[40m'
BG_RED = f'{ESC}[41m'
BG_GREEN = f'{ESC}[42m'
BG_YELLOW = f'{ESC}[43m'
BG_BLUE = f'{ESC}[44m'
BG_MAGENTA = f'{ESC}[45m'
BG_CYAN = f'{ESC}[46m'
BG_LIGHT_GRAY = f'{ESC}[47m' # Alias para blanco/gris claro
#BG_WHITE = f'{ESC}[47m' # El 47 es gris claro, pero el 107 si es fondo blanco.

# Colores de primer plano (Foreground) brillantes (brighter/bold version)
FG_BRIGHT_BLACK = f'{ESC}[90m'
FG_BRIGHT_RED = f'{ESC}[91m'
FG_BRIGHT_GREEN = f'{ESC}[92m'
FG_BRIGHT_YELLOW = f'{ESC}[93m'
FG_BRIGHT_BLUE = f'{ESC}[94m'
FG_BRIGHT_MAGENTA = f'{ESC}[95m'
FG_BRIGHT_CYAN = f'{ESC}[96m'
FG_BRIGHT_WHITE = f'{ESC}[97m'

# Colores de fondo (Background) brillantes
BG_BRIGHT_BLACK = f'{ESC}[100m'
BG_BRIGHT_RED = f'{ESC}[101m'
BG_BRIGHT_GREEN = f'{ESC}[102m'
BG_BRIGHT_YELLOW = f'{ESC}[103m'
BG_BRIGHT_BLUE = f'{ESC}[104m'
BG_BRIGHT_MAGENTA = f'{ESC}[105m'
BG_BRIGHT_CYAN = f'{ESC}[106m'
BG_BRIGHT_WHITE = f'{ESC}[107m'

def cargar_xp_tabla():
    # Obtener la ruta absoluta del archivo
    ruta_archivo = os.path.join(os.path.dirname(__file__), '../data/XP_Solo_Table.csv')

    xp_tabla = {}
    with open(ruta_archivo, 'r', newline='') as archivo:
        lector = csv.reader(archivo, delimiter=';')
        next(lector)  # Salta encabezados
        for nivel, xp in lector:
            xp_tabla[int(nivel)] = int(xp)
    return xp_tabla

def cargar_estadisticas_crecimiento():
    # Obtener la ruta absoluta del archivo
    ruta_archivo = os.path.join(os.path.dirname(__file__), '../data/Guaranteed_stat_growth.csv')

    estadisticas = {}
    with open(ruta_archivo, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            nivel = int(fila['Lv'])
            estadisticas[nivel] = {
                clase: valor.strip()# if valor != '-' else None
                for clase, valor in fila.items()
                if clase != 'Lv'
            }
    return estadisticas

def cargar_armas():
    # Obtener la ruta absoluta del archivo
    ruta_archivo = os.path.join(os.path.dirname(__file__), '../data/FFI_BD_Weapons.csv')

    armas = {}
    with open(ruta_archivo, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo, delimiter=';')
        for fila in lector:
            nombre = fila['New Name']
            armas[nombre] = {
                'old_name_2': fila['Old Name 2'],
                'old_name': fila['Old Name'],
                'price': fila['Price'], # Price (Normal)
                'price_(easy)': fila['Price (Easy)'],
                'value': int(fila['Value']),
                'atk': fila['Atk'],
                'acc': fila['Acc'],
                'crit': fila['Crit'],
                'equip_by': [x.strip() for x in fila['Equipped by'].split(',') if x.strip()],
                'buy': [x.strip() for x in fila['Buy'].split(',') if x.strip()], # fila['Buy'],# == 'True',
                'find': [x.strip() for x in fila['Find'].split(',') if x.strip()], # fila['Find'],# == 'True',
                'drop': [x.strip() for x in fila['Drop'].split(',') if x.strip()], # fila['Drop'],# == 'True',
                'gift': [x.strip() for x in fila['Gift'].split(',') if x.strip()], # fila['Drop'],# == 'True',
                'special': fila['Special'],# == 'True',
                'type': fila['Type'],
                'str_vs': fila['Strong vs'],
                'elemental': fila['Element'],
                'used_as_item': fila['Used as item'],
                'inflicts': fila['Inflicts'],
                'stats': fila['Stats'],
                'seba': fila['Special Effect Before Attack'],
                'seaa': fila['Special Effect After Attack'],
                'description': fila['Description']
            }
    return armas

def cargar_estadisticas_enemigos():
    # Obtener la ruta absoluta del archivo
    ruta_archivo = os.path.join(os.path.dirname(__file__), '../data/Enemy_stats.csv')

    enemigos = {}
    with open(ruta_archivo, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo, delimiter=';')
        for fila in lector:
            nombre = fila['Name']
            enemigos[nombre] = {
                'background': fila['Background'],
                'HP': int(fila['HP']),
                'ATK': int(fila['ATK']),
                'DEF': int(fila['DEF']),
                'MD': int(fila['MD']),
                'WEAK': [x.strip() for x in fila['WEAK'].split(',') if x.strip()],
                'RESI': [x.strip() for x in fila['RESI'].split(',') if x.strip()],
                'gil': int(fila['Gil']),
                'XP': int(fila['EXP']),
                'Hits': int(fila['Hits']),
                'ACC': int(fila['ACC']),
                # 'acc_2': int(fila['ACC_2']) if fila['ACC_2'] != '-' else None,
                'status': fila['Status'],
                'CRIT': int(fila['CRIT']),
                'EVA': int(fila['EVA']),
                # 'eva_2': int(fila['Eva_2']) if fila['Eva_2'] != '-' else None,
                'run_level': fila['Run Lev.'],
                'magic': fila['Magic'],
                'sp_atk': fila['Sp. Att'],
                'family': fila['Family'],
                'AGL': int(fila['AGL']),
                'drop': str(fila['Drop']) # Item (porcentage)
            }
    return enemigos

def cargar_formacion_enemigos():
    # Obtener la ruta absoluta del archivo
    ruta_archivo = os.path.join(os.path.dirname(__file__), '../data/Enemy_Formation.csv')

    formacion = {}
    with open(ruta_archivo, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo, delimiter=';')
        for fila in lector:
            numero = fila['Number']
            formacion[numero] = {
                'Enemies': [x.strip() for x in fila['Enemies'].split(',') if x.strip()],
                'Maximum': str(fila['Maximum']),
                'Can flee?': bool(fila['Can flee?']),
                'Ambush%': int(fila['Ambush%']),
                'Musical theme': str(fila['Musical theme']),
                'Location': [x.strip() for x in fila['Location'].split(',') if x.strip()]
            }
    return formacion

def cargar_armaduras():
    # Obtener la ruta absoluta del archivo
    ruta_archivo = os.path.join(os.path.dirname(__file__), '../data/FFI_BD_Armors.csv')

    armaduras = {}
    with open(ruta_archivo, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo, delimiter=';')
        for fila in lector:
            nombre = fila['Name']


            # Si el nombre tiene paréntesis, tomar solo lo que está antes
            if '(' in nombre:
                nombre = nombre.split('(')[0].strip()
            # Procesar la columna 'Find'
            ubicaciones_find = []
            for ubicacion_find in fila['Find'].split(','):
                ubicacion_find = ubicacion_find.strip()
                # Si la ubicación tiene "(x", eliminarlo
                if '(x' in ubicacion_find:
                    ubicacion_find = ubicacion_find.split('(x')[0].strip()
                ubicaciones_find.append(ubicacion_find)


            armaduras[nombre] = {
                'equip_by': [x.strip() for x in fila['Equipped by'].split(',') if x.strip()],
                'price': fila['Price'], # int y '?'
                'value': int(fila['Value']),
                'DEF': int(fila['Defense']),
                'EVA': int(fila['Evasion']),
                'WEI': int(fila['Weight']),
                'buy': [x.strip() for x in fila['Buy'].split(',') if x.strip()], # str(fila['Buy']),
                'find': ubicaciones_find, # [x.strip() for x in fila['Find'].split(',') if x.strip()], # str(fila['Find']),
                'drop': [x.strip() for x in fila['Drop'].split(',') if x.strip()], # str(fila['Drop']),
                'type': str(fila['Type']),
                'stats': str(fila['Stats']),
                'resistance': str(fila['Resistance']),
                'description': str(fila['Description']),
                'used_as_item': str(fila['Used as item']),
                'end_of_turn': str(fila['End of turn'])
            }
    return armaduras

def quitar_elementos(lista_principal, elementos_a_quitar):
    """
    Devuelve una nueva lista con los elementos de lista_principal que no están
    en elementos_a_quitar.
    """
    return [elemento for elemento in lista_principal if elemento not in elementos_a_quitar]

def cargar_items():
    # Obtener la ruta absoluta del archivo
    ruta_archivo = os.path.join(os.path.dirname(__file__), '../data/Items.csv')

    items = {}
    with open(ruta_archivo, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo, delimiter=';')
        for fila in lector:
            nombre = fila['Name']
            # Si el nombre tiene paréntesis, tomar solo lo que está antes
            if '(' in nombre:
                nombre = nombre.split('(')[0].strip()
            # Procesar la columna 'Find'
            ubicaciones_find = []
            for ubicacion_find in fila['Find'].split(','):
                ubicacion_find = ubicacion_find.strip()
                # Si la ubicación tiene "(x", eliminarlo
                if '(x' in ubicacion_find:
                    ubicacion_find = ubicacion_find.split('(x')[0].strip()
                ubicaciones_find.append(ubicacion_find)

            items[nombre] = {
                'type': str(fila['Type']),
                'subtype': str(fila['Subtype']),
                'price': int(fila['Price']),
                'value': int(fila['Value']),
                'buy': [x.strip() for x in fila['Buy'].split(',') if x.strip()], # str(fila['Buy']),
                # 'find': str(fila['Find']),
                # 'find': [x.strip() for x in fila['Find'].split(',') if x.strip()],
                'find': ubicaciones_find,
                'drop': [x.strip() for x in fila['Drop'].split(',') if x.strip()], # str(fila['Drop']),
                'effect': str(fila['Effect']),
                'description': str(fila['Description']),
                'affects': str(fila['Affects'])
            }
    return items



# Definimos un diccionario con todas las estadísticas por clase
ESTADISTICAS_BASE = {
    'Warrior': {'HP': 35, 'MP': 0, 'STR': 10, 'AGL': 8, 'INT': 1, 'STA': 15, 'LCK': 8, 'Ini_ACC': 7, 'Mul_ACC': 3, 'Ini_EVA': 45, 'Ini_MD': 13, 'Mul_MD': 2},
    'Thief': {'HP': 30, 'MP': 0, 'STR': 5, 'AGL': 15, 'INT': 1, 'STA': 5, 'LCK': 15, 'Ini_ACC': 10, 'Mul_ACC': 5, 'Ini_EVA': 43, 'Ini_MD': 11, 'Mul_MD': 2},
    'Monk': {'HP': 33, 'MP': 0, 'STR': 13, 'AGL': 5, 'INT': 1, 'STA': 10, 'LCK': 5, 'Ini_ACC': 5, 'Mul_ACC': 3, 'Ini_EVA': 45, 'Ini_MD': 9, 'Mul_MD': 1},
    'W. Mage': {'HP': 33, 'MP': 10, 'STR': 5, 'AGL': 5, 'INT': 15, 'STA': 8, 'LCK': 5, 'Ini_ACC': 4, 'Mul_ACC': 1, 'Ini_EVA': 48, 'Ini_MD': 19, 'Mul_MD': 4},
    'B. Mage': {'HP': 25, 'MP': 10, 'STR': 3, 'AGL': 5, 'INT': 20, 'STA': 2, 'LCK': 10, 'Ini_ACC': 6, 'Mul_ACC': 2, 'Ini_EVA': 48, 'Ini_MD': 19, 'Mul_MD': 4},
    'R. Mage': {'HP': 30, 'MP': 10, 'STR': 5, 'AGL': 10, 'INT': 10, 'STA': 5, 'LCK': 5, 'Ini_ACC': 9, 'Mul_ACC': 3, 'Ini_EVA': 43, 'Ini_MD': 17, 'Mul_MD': 3},
    'Knight': {'HP': 35, 'MP': 0, 'STR': 10, 'AGL': 8, 'INT': 1, 'STA': 15, 'LCK': 8, 'Ini_ACC': 7, 'Mul_ACC': 3, 'Ini_EVA': 45, 'Ini_MD': 13, 'Mul_MD': 3},
    'Ninja': {'HP': 30, 'MP': 0, 'STR': 5, 'AGL': 15, 'INT': 1, 'STA': 5, 'LCK': 15, 'Ini_ACC': 10, 'Mul_ACC': 5, 'Ini_EVA': 43, 'Ini_MD': 11, 'Mul_MD': 3},
    'Master': {'HP': 33, 'MP': 0, 'STR': 13, 'AGL': 5, 'INT': 1, 'STA': 10, 'LCK': 5, 'Ini_ACC': 5, 'Mul_ACC': 3, 'Ini_EVA': 45, 'Ini_MD': 9, 'Mul_MD': 2},
    'W. Wizard': {'HP': 33, 'MP': 10, 'STR': 5, 'AGL': 5, 'INT': 15, 'STA': 8, 'LCK': 5, 'Ini_ACC': 4, 'Mul_ACC': 1, 'Ini_EVA': 48, 'Ini_MD': 19, 'Mul_MD': 5},
    'B. Wizard': {'HP': 25, 'MP': 10, 'STR': 3, 'AGL': 5, 'INT': 20, 'STA': 2, 'LCK': 10, 'Ini_ACC': 6, 'Mul_ACC': 2, 'Ini_EVA': 48, 'Ini_MD': 19, 'Mul_MD': 5},
    'R. Wizard': {'HP': 30, 'MP': 10, 'STR': 5, 'AGL': 10, 'INT': 10, 'STA': 5, 'LCK': 5, 'Ini_ACC': 9, 'Mul_ACC': 3, 'Ini_EVA': 43, 'Ini_MD': 17, 'Mul_MD': 3}
}

# Ahora puedes usarlo en cualquier archivo:
XP_TABLE = cargar_xp_tabla()

# Ejemplo de uso:
CRECIMIENTO_GARANTIZADO = cargar_estadisticas_crecimiento()

# Carga la info de todas las armas
ARMAS = cargar_armas()
# print(ARMAS["Sasuke's Blade"])
# print(ARMAS["Masamune"])

# Ejemplo de uso:
ENEMIGOS = cargar_estadisticas_enemigos()
# Acceder a los datos:
# chaos_dict = ENEMIGOS['Chaos']
# print(f"HP de Chaos: {chaos_dict['HP']}")
# print(f"Debilidades de Chaos: {', '.join(chaos_dict['WEAK'])}")
# print(f"Familia de Chaos: {chaos_dict['family']}")

# Carga la info de todas las Formaciones Enemigas
FORMACION = cargar_formacion_enemigos()

# Carga la info de las armaduras
ARMADURAS = cargar_armaduras()

# print(f"ARMADURAS.keys(): {ARMADURAS.keys()}")
# print(f"ARMADURAS['Genji Helm']: {ARMADURAS['Genji Helm']}")
# print(f"ARMADURAS['Genji Helm']['type']: {ARMADURAS['Genji Helm']['type']}")

# Elementos o Items
#                                            HEALING_ITEMS, FIELD_ITEMS, SUPPORT_ITEMS, ATTACK_ITEMS
## menu_de_la_party_mundo_abierto_elementos        X
## menu_de_la_party_pueblo_elementos               X
## menu_de_la_party_dungeon_elementos              X
## batalla_elementos                               X                           X             X

# HEALING_ITEMS =["Potion","Hi-Potion","X-Potion","Ether","Turbo Ether","Dry Ether","Elixir","Megalixir","Phoenix Down",
#                 "Antidote","Eye Drops","Echo Grass","Gold Needle","Remedy"]
# FIELD_ITEMS = ["Emergency Exit","Sleeping Bag","Tent","Cottage","Golden Apple","Silver Apple","Soma Drop",
#                "Power Plus","Stamina Plus","Mind Plus","Speed Plus","Luck Plus"]
# SUPPORT_ITEMS = ["Light Curtain","Red Curtain","White Curtain","Blue Curtain","Lunar Curtain","Hermes' Shoes",
#                  "Giant's Tonic","Faerie Tonic","Strength Tonic","Protect Drink","Speed Drink"]
# ATTACK_ITEMS = ["Spider's Silk","White Fang","Red Fang","Blue Fang","Vampire Fang","Cockatrice Claw"]
# KEY_ITEMS = ["Lute","Crown","Crystal Eye","Jolt Tonic","Mystic Key","Nitro Powder","Rosetta Stone","Adamantite",
#              "Star Ruby","Earth Rod","Levistone","Chime","Rat's Tail","Warp Cube","Bottled Faerie","Oxyale","Canoe",
#              "Carobo","Ocarina","Cogwheel","Pickaxe","Autograph","Witch's Brew","Smyth's Tools","House Key",
#              "Cat's Whisker","Head Parts","Torso Parts","Shoulder Parts","Arm Parts","Leg Parts","Audio Circuit",
#              "Exoskeleton","A.I Chip","Battery Circuit","Energy Chip"]

# Carga la info de los items
ITEMS = cargar_items()

print(f"ITEMS.keys(): {ITEMS.keys()}")
print(f"ITEMS['Potion']: {ITEMS['Potion']}")
print(f"ITEMS['Potion']['subtype']: {ITEMS['Potion']['subtype']}")
print(f"Potion in ITEMS: {"Potion" in ITEMS}")
print(f"ASD in ITEMS: {"ASD" in ITEMS.keys()}")

HEALING_ITEMS = []
FIELD_ITEMS = []
SUPPORT_ITEMS = []
ATTACK_ITEMS = []
KEY_ITEMS = []
for item in ITEMS:
    if ITEMS[item]["subtype"] == "Healing":
        HEALING_ITEMS.append(item) # print(ITEMS[item]["subtype"])
    elif ITEMS[item]["subtype"] == "Field":
        FIELD_ITEMS.append(item) # print(ITEMS[item]["subtype"])
    elif ITEMS[item]["subtype"] == "Support":
        SUPPORT_ITEMS.append(item) # print(ITEMS[item]["subtype"])
    elif ITEMS[item]["subtype"] == "Attack":
        ATTACK_ITEMS.append(item) # print(ITEMS[item]["subtype"])
    else:
        KEY_ITEMS.append(item) # print(ITEMS[item]["subtype"])
print(f"HEALING_ITEMS")
print(HEALING_ITEMS)
print(f"FIELD_ITEMS")
print(FIELD_ITEMS)
print(f"SUPPORT_ITEMS")
print(SUPPORT_ITEMS)
print(f"ATTACK_ITEMS")
print(ATTACK_ITEMS)
print(f"KEY_ITEMS")
print(KEY_ITEMS)

ITEMS_OPEN_WORLD = HEALING_ITEMS + quitar_elementos(FIELD_ITEMS, ["Emergency Exit"])
ITEMS_TOWN = HEALING_ITEMS + quitar_elementos(FIELD_ITEMS, ["Emergency Exit","Sleeping Bag","Tent","Cottage"])
ITEMS_DUNGEON = HEALING_ITEMS + quitar_elementos(FIELD_ITEMS, ["Sleeping Bag","Tent","Cottage"])
ITEMS_BATTLE = HEALING_ITEMS + SUPPORT_ITEMS + ATTACK_ITEMS # Nunca los FIELD_ITEMS

print(f"ITEMS_OPEN_WORLD")
print(ITEMS_OPEN_WORLD)
print(f"ITEMS_TOWN")
print(ITEMS_TOWN)
print(f"ITEMS_DUNGEON")
print(ITEMS_DUNGEON)
print(f"ITEMS_BATTLE")
print(ITEMS_BATTLE)

ITEMS_OPEN_WORLD_ONE_ALLY = []
ITEMS_OPEN_WORLD_ALL_ALLIES = []
for item in ITEMS_OPEN_WORLD:
    if ITEMS[item]["affects"] == "one ally":
        ITEMS_OPEN_WORLD_ONE_ALLY.append(item)
    if ITEMS[item]["affects"] == "all allies":
        ITEMS_OPEN_WORLD_ALL_ALLIES.append(item)
ITEMS_TOWN_ONE_ALLY = []
ITEMS_TOWN_ALL_ALLIES = []
for item in ITEMS_TOWN:
    if ITEMS[item]["affects"] == "one ally":
        ITEMS_TOWN_ONE_ALLY.append(item)
    if ITEMS[item]["affects"] == "all allies":
        ITEMS_TOWN_ALL_ALLIES.append(item)
ITEMS_DUNGEON_ONE_ALLY = []
ITEMS_DUNGEON_ALL_ALLIES = []
for item in ITEMS_DUNGEON:
    if ITEMS[item]["affects"] == "one ally":
        ITEMS_DUNGEON_ONE_ALLY.append(item)
    if ITEMS[item]["affects"] == "all allies":
        ITEMS_DUNGEON_ALL_ALLIES.append(item)
ITEMS_BATTLE_ONE_ALLY = []
ITEMS_BATTLE_ALL_ALLIES = []
ITEMS_BATTLE_ONE_ENEMY = []
ITEMS_BATTLE_ALL_ENEMIES = []
for item in ITEMS_BATTLE:
    if ITEMS[item]["affects"] == "one ally":
        ITEMS_BATTLE_ONE_ALLY.append(item)
    if ITEMS[item]["affects"] == "all allies":
        ITEMS_BATTLE_ALL_ALLIES.append(item)
    if ITEMS[item]["affects"] == "one enemy":
        ITEMS_BATTLE_ONE_ENEMY.append(item)
    if ITEMS[item]["affects"] == "all enemies":
        ITEMS_BATTLE_ALL_ENEMIES.append(item)

print()
print(f"ITEMS_OPEN_WORLD_ONE_ALLY")
print(ITEMS_OPEN_WORLD_ONE_ALLY)
print(f"ITEMS_OPEN_WORLD_ALL_ALLIES")
print(ITEMS_OPEN_WORLD_ALL_ALLIES)
print()
print(f"ITEMS_TOWN_ONE_ALLY")
print(ITEMS_TOWN_ONE_ALLY)
print(f"ITEMS_TOWN_ALL_ALLIES")
print(ITEMS_TOWN_ALL_ALLIES)
print()
print(f"ITEMS_DUNGEON_ONE_ALLY")
print(ITEMS_DUNGEON_ONE_ALLY)
print(f"ITEMS_DUNGEON_ALL_ALLIES")
print(ITEMS_DUNGEON_ALL_ALLIES)
print()
print(f"ITEMS_BATTLE_ONE_ALLY")
print(ITEMS_BATTLE_ONE_ALLY)
print(f"ITEMS_BATTLE_ALL_ALLIES")
print(ITEMS_BATTLE_ALL_ALLIES)
print(f"ITEMS_BATTLE_ONE_ENEMY")
print(ITEMS_BATTLE_ONE_ENEMY)
print(f"ITEMS_BATTLE_ALL_ENEMIES")
print(ITEMS_BATTLE_ALL_ENEMIES)

# # Elementals
# Fire, Ice, Lightning, Earth, Spirit, Poison, Time, Instant Death, Dia
# # Status
# Silence, Sleep, Paralysis, Darkness, Poison, Stone, Confuse

# ========================================================================================
# # Ejemplo de uso
# print(f"{VERDE}¡Victoria!{RESET}")
# print(f"{ROJO}¡Derrota!{RESET}")
# print(f"{AZUL}Estado del juego:{RESET} {VERDE}100{RESET} oro")

# Nombres para cada clase
BLACK_WIZARD_NAMES = ["Morthos", "Zarthus", "Nox", "Sauron", "Vilgefortz", "Grindelwald"]
# ========================================================================================
print(ITEMS)

# 1) All Locations
## 1.1) Location from FORMACION (Enemy_Formation.csv).       Location
print(f"\nLocations from FORMACION:")
# Primero obtén todas las listas
formacion_locations = [value['Location'] for key, value in FORMACION.items()]
# Juntar todas las listas y eliminar duplicados
all_formacion_locations = list(set([item for sublist in formacion_locations for item in sublist]))
# all_formacion_locations.remove("-")
print(all_formacion_locations)
# for form_loc in all_formacion_locations:
#     print(form_loc)

## 1.2) Location from ARMAS (FFI_BD_Weapons.csv).            buy, find
# Lista para almacenar todos los elementos
print(f"\nLocations from ARMAS:")
all_armas_locations = []
# Iterar sobre cada elemento en ARMAS
for key, value in ARMAS.items():
    for source in ['buy', 'find']:
        if source in value:
            # Agregar cada location si no existe
            for location in value[source]:
                if location not in all_armas_locations:
                    all_armas_locations.append(location)
all_armas_locations.remove("-")
print(all_armas_locations)
# for armas_loc in all_armas_locations:
#     print(armas_loc)

## 1.3) Location from ARMADURAS (FFI_BD_Armors.csv).         buy, find
# Lista para almacenar todos los elementos
print(f"\nLocations from ARMADURAS:")
all_armaduras_locations = []
# Iterar sobre cada elemento en ARMADURAS
for key, value in ARMADURAS.items():
    for source in ['buy', 'find']:
        if source in value:
            # Agregar cada location si no existe
            for location in value[source]:
                if location not in all_armaduras_locations:
                    all_armaduras_locations.append(location)
all_armaduras_locations.remove("-")
print(all_armaduras_locations)
# for armaduras_loc in all_armaduras_locations:
#     print(armaduras_loc)

## 1.4) Location from ITEMS (Items.csv).                     buy, find
# Lista para almacenar todos los elementos
print(f"\nLocations from ITEMS:")
all_items_locations = []
# Iterar sobre cada elemento en ITEMS
for key, value in ITEMS.items():
    for source in ['buy', 'find']:
        if source in value:
            # Agregar cada location si no existe
            for location in value[source]:
                if location not in all_items_locations:
                    all_items_locations.append(location)
all_items_locations.remove("-")
all_items_locations.remove("All shops")
print(all_items_locations)
for items_loc in all_items_locations:
    print(items_loc)

## 2) Todas las listas
# 2.1) Combina todas las listas en una sola lista grande
listas_combinadas = all_formacion_locations + all_armas_locations + all_armaduras_locations + all_items_locations
print(f"Listas combinadas con duplicados: {listas_combinadas}")

# 2.2) Convierte la lista combinada a un conjunto (set) para eliminar duplicados automáticamente
conjunto_sin_duplicados = set(listas_combinadas)
print(f"Conjunto sin duplicados: {conjunto_sin_duplicados}")

# 2.3) (Opcional) Vuelve a convertir el conjunto a una lista si necesitas el tipo de dato lista
all_locations = list(conjunto_sin_duplicados)
print(f"Resultado final como lista: {all_locations}")


# VERDE = '\033[32m'
# ROJO = '\033[31m'
# for i in range(129):
#     color = '\033[' + str(i) + 'm'
#     print(f"{color}Test {i}{RESET}")
#
# print(f"\033[31m\033[101mTest{RESET}")
# print(f"\033[91m\033[41mTest{RESET}")