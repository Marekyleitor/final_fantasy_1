# utils/constantes.py
import csv
import os

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
                'old_name': fila['Old Name'],
                'price': fila['Price'],
                'atk': fila['Atk'],
                'acc': fila['Acc'],
                'crit': fila['Crit'],
                'equip_by': [x.strip() for x in fila['Equipped by'].split(',') if x.strip()],
                'buy': fila['Buy'],# == 'True',
                'find': fila['Find'],# == 'True',
                'win': fila['Win'],# == 'True',
                'special': fila['Special'],# == 'True',
                'type': fila['Type'],
                'str_vs': fila['Strong vs'],
                'elemental': fila['Element'],
                'cast': fila['Cast'],
                'inflicts': fila['Inflicts'],
                'stats': fila['Stats'],
                'seba': fila['Special Effect Before Attack'],
                'seaa': fila['Special Effect After Attack']
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
                'AGL': int(fila['AGL'])
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
                'Enemies': [x.strip() for x in fila['Enemies'].split(', ') if x.strip()],
                'Maximum': str(fila['Maximum']),
                'Can flee?': bool(fila['Can flee?']),
                'Ambush%': int(fila['Ambush%']),
                'Musical theme': str(fila['Musical theme']),
                'Location': [x.strip() for x in fila['Location'].split(', ') if x.strip()]
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
            armaduras[nombre] = {
                'equip_by': [x.strip() for x in fila['Equipped by'].split(',') if x.strip()],
                'price': fila['Price'], # int y '?'
                'value': int(fila['Value']),
                'DEF': int(fila['Defense']),
                'EVA': int(fila['Evasion']),
                'WEI': int(fila['Weight']),
                'buy': str(fila['Buy']),
                'find': str(fila['Find']),
                'drop': str(fila['Drop']),
                'type': str(fila['Type']),
                'stats': str(fila['Stats']),
                'resistance': str(fila['Resistance']),
                'description': str(fila['Description']),
                'used_as_item': str(fila['Used as item']),
                'end_of_turn': str(fila['End of turn'])
            }
    return armaduras


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
