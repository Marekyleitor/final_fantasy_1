import random, math
from src.utils.constantes import ARMAS, FG_BRIGHT_BLACK, FG_BRIGHT_GREEN, FG_BRIGHT_CYAN, FG_BRIGHT_MAGENTA, \
    FG_BRIGHT_RED, FG_BRIGHT_YELLOW
from src.utils.constantes import RESET


def equiped_by_exact_class(lst: list) -> list:
    """
        Traduce una lista de strings usando un diccionario de traducciones.
        Modifica la lista original.
        """
    if lst[0] == 'All classes':
        return ['Warrior', 'Knight', 'Thief', 'Ninja', 'W. Mage', 'W. Wizard', 'B. Mage', 'B. Wizard', 'Monk',
                'Master', 'R. Mage', 'R. Wizard']
    # Diccionario de clase exacta del PJ (ejemplo)
    traducciones = {
        'Wa': 'Warrior',
        'Kn': 'Knight',
        'Th': 'Thief',
        'Ni': 'Ninja',
        'WM': 'W. Mage',
        'WW': 'W. Wizard',
        'BM': 'B. Mage',
        'BW': 'B. Wizard',
        'Mo': 'Monk',
        'Ma': 'Master',
        'RM': 'R. Mage',
        'RW': 'R. Wizard'
    }
    for i in range(len(lst)):
        lst[i] = traducciones.get(lst[i], lst[i])
    return lst

def str_to_dict(s: str = "-"):  # return str ("-") or dict
    if s == '-':
        return s
    else:
        s = s.replace("{", "")
        s = s.replace("}", "")
        arr = s.split(", ")
        miDic = {}
        for elem in arr:
            val = elem.split(":")
            if "%" in val[1]:
                miDic[val[0]] = porcentage_to_decimal(val[1])
            else:
                miDic[val[0]] = int(val[1])
            # print(type(miDic[val[0]]))
        return miDic

def porcentage_to_decimal(porc: str):
    porc = porc.replace("%", "")
    deci = float(int(porc) / 100)
    return float(1 + deci)

def get_gear_mult_color(mult):
    G, M, C = "", 1.00, ""
    if mult == 0:  # mult será random
        random_1 = random.choice(range(1, 21))
        if random_1 >= 1 and random_1 <= 6:
            G = "Regular"
            M = 1.00
            C = FG_BRIGHT_BLACK  # '{ESC}[90m' o '\033[90m'
        elif random_1 >= 7 and random_1 <= 11:
            G = "Superior"
            M = random.choice(range(105, 130, 5)) / 100
            C = FG_BRIGHT_GREEN  # '{ESC}[92m' o '\033[92m'
        elif random_1 >= 12 and random_1 <= 15:
            G = "Famed"
            M = random.choice(range(130, 155, 5)) / 100
            C = FG_BRIGHT_CYAN  # '{ESC}[96m' o '\033[96m'
        elif random_1 >= 16 and random_1 <= 18:
            G = "Legendary"
            M = random.choice(range(155, 180, 5)) / 100
            C = FG_BRIGHT_MAGENTA  # '{ESC}[95m' o '\033[95m'
        elif random_1 >= 19 and random_1 <= 20:
            G = "Ornate"
            M = random.choice(range(180, 205, 5)) / 100
            C = FG_BRIGHT_RED  # '{ESC}[91m' o '\033[91m'
        else:
            G = "Hack"
            M = 1.00
            C = FG_BRIGHT_YELLOW  # '{ESC}[93m' o '\033[93m'
    else:
        M = mult
        if M == 1.00:
            G, C = "Regular", FG_BRIGHT_BLACK
        elif M in [1.05, 1.10, 1.15, 1.20, 1.25]:
            G, C = "Superior", FG_BRIGHT_GREEN
        elif M in [1.30, 1.35, 1.40, 1.45, 1.50]:
            G, C = "Famed", FG_BRIGHT_CYAN
        elif M in [1.55, 1.60, 1.65, 1.70, 1.75]:
            G, C = "Legendary", FG_BRIGHT_MAGENTA
        elif M in [1.80, 1.85, 1.90, 1.95, 2.00]:
            G, C = "Ornate", FG_BRIGHT_RED
        else:
            G, C = "Hack", FG_BRIGHT_YELLOW
    return G, M, C

def get_price_with_mult(name, mult, catalog):
    price_str = catalog[name]['price']

    try:
        price_num = int(price_str)
        final_price = math.trunc(price_num * value_market_mult(mult))
        return final_price
    except ValueError:
        return f"{price_str} x {mult}"

def get_value_with_mult(price_mult, mult):
    if isinstance(price_mult, int):  # price ya es el resultado de get_price_with_mult(self)
        value = price_mult / 2
    else:
        value = 100 * mult  # Float
        s = str(value)  # String
        if '.' in s:
            partes = s.split('.')
            decimales = partes[1]
            # Validamos si los primeros decimales son '9999' o muy cercanos a 1
            # También comprobamos si es '0000' lo que puede indicar un 0.00000001

            # Una forma simple es verificar si empieza con 999
            if decimales.startswith('999'):
                # print(f"Detectado error de precisión ({decimales[:5]}...), redondeando.")
                # Redondeamos matemáticamente al entero más cercano
                value = int(round(value))

            # Otra condición común para errores: si es muy cercano a cero (ej: 0.0000000001)
            elif decimales.startswith('00000'):
                # print(f"Detectado error de precisión ({decimales[:5]}...), redondeando.")
                value = int(round(value))

            else:
                # print(f"NO HAY error de precisión 1, Truncando.")
                value = int(value)
        else:
            # print(f"NO HAY error de precisión 2, Truncando.")
            value = int(value)
    return value

def value_market_mult(mult):
    return round((((mult - 1) / 0.05) + 1))

def get_operation_type_A(num, mult):
    """
    Relacionados al Price del arma.

    Args:
    num: El Price (ej: 5, 800, 45, 100)

    Returns:
    String de la operación que se realizará para calcular el valor final
    """
    return f"{num} x {value_market_mult(mult)}"  # Devuelve un string

def get_operation_type_B(num):
    """
    Relacionados al Value del arma.

    Args:
    num: El Price calculado del arma actual, no el base (ej: 5, 800, 45, 100)

    Returns:
    String de la operación que se realizará para calcular el valor final
    """
    return f"{num} / 2"  # Devuelve un string

def get_operation_type_C(num, mult):
    """
    Relacionados al Atk, Acc y Crit del arma.

    Args:
    num: El Atk, Acc o Crit (ej: 13, 20, 48)

    Returns:
    String de la operación que se realizará para calcular el valor final
    """
    return f"{num} x {mult}"  # Devuelve un string

def get_decored_name(self):
    if self.name == "Hands":
        return self.name
    else:
        if hasattr(self, "decored_name"):
            return f"{'Arma:':<16} {self.decored_name}"
        else:
            G = "Regular"
            M = 1.00
            C = FG_BRIGHT_BLACK
            text = f"{C}{self.name} | {G} | {M}{RESET}"
            return text