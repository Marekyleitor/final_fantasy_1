import random, math
from src.utils.constantes import ARMAS, FG_BRIGHT_BLACK, FG_BRIGHT_GREEN, FG_BRIGHT_CYAN, FG_BRIGHT_MAGENTA, \
    FG_BRIGHT_RED, FG_BRIGHT_YELLOW
from src.utils.constantes import RESET


# utils_arma_armadura.py
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

def value_market_mult(mult):
    return round((((mult - 1) / 0.05) + 1))

def get_price_with_mult(name, mult, catalog):
    price_str = catalog[name]['price']

    try:
        price_num = int(price_str)
        final_price = math.trunc(price_num * value_market_mult(mult))
        return final_price
    except ValueError:
        return f"{price_str} x {mult}"