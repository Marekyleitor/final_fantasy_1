import random, math
from src.utils import utils_arma_armadura
from src.utils.constantes import ARMADURAS, RESET, FG_BRIGHT_BLACK, FG_BRIGHT_GREEN, FG_BRIGHT_CYAN, FG_BRIGHT_MAGENTA, \
    FG_BRIGHT_RED, FG_BRIGHT_YELLOW
from src.utils.utils_arma_armadura import equiped_by_exact_class, str_to_dict, porcentage_to_decimal, \
    get_gear_mult_color, get_price_with_mult, get_value_with_mult, value_market_mult, get_operation_type_A, \
    get_operation_type_B, get_operation_type_C, get_decored_name


class Armadura:
    def __init__(self, name, mult: float = 0):
        self.name = name
        self.gear, self.mult, self.color = get_gear_mult_color(mult)
        self.compound_name = f"{self.name} | {self.gear} | {self.mult}"  # self.name + " | " + self.gear + " | " + self.mult
        self.decored_name = f"{self.color}{self.compound_name}{RESET}"
        if name != '':
            self.equip_by = self.equiped_by_exact_class(ARMADURAS[name]['equip_by'])
            self.price = self.get_price_with_mult()  # ARMADURAS[name]['price']
            self.value = self.get_value_with_mult()  # ARMADURAS[name]['value']
            self.DEF = self.get_def_with_mult()  # ARMADURAS[name]['DEF']
            self.EVA = self.get_eva_with_mult()  # ARMADURAS[name]['EVA']
            self.WEI = self.get_wei_with_mult()  # ARMADURAS[name]['WEI']
            self.buy = ARMADURAS[name]['buy']
            self.find = ARMADURAS[name]['find']
            self.drop = ARMADURAS[name]['drop']
            self.type = ARMADURAS[name]['type']
            self.stats = self.str_to_dict(ARMADURAS[name]['stats'])
            self.allStats = self.getAllStats()
            self.resistance = ARMADURAS[name]['resistance']
            self.description = ARMADURAS[name]['description']
            self.used_as_item = ARMADURAS[name]['used_as_item']
            self.end_of_turn = ARMADURAS[name]['end_of_turn']
        else:
            self.gear, self.mult = "", 0.00
            self.compound_name = f"{self.name}"
            self.decored_name = f"{self.name}"
            self.equip_by, self.price, self.value, self.DEF, self.EVA, self.WEI, = 'All clases', 0, 0, 0, 0, 0
            self.buy, self.find, self.drop, self.type, self.stats, = '-', '-', '-', '-', '-'
            self.allStats, self.resistance, self.description, self.used_as_item = self.getAllStats(), '-', '-', '-'
            self.end_of_turn = '-'

    def mostrar_datos(self):
        print("Name:", self.name, '\t', type(self.name))
        print("Gear:", self.gear, '\t', type(self.gear))
        print("Mult:", self.mult, '\t', type(self.mult))
        print("Color:", self.color, '\t', type(self.color))
        print("Equipped by:", self.equip_by, '\t', type(self.equip_by))
        print("Price:", self.price, '\t', type(self.price))
        print("Value:", self.value, '\t', type(self.value))
        print("Defense:", self.DEF, '\t', type(self.DEF))
        print("Evasion:", self.EVA, '\t', type(self.EVA))
        print("Weight:", self.WEI, '\t', type(self.WEI))
        print("Buy:", self.buy, '\t', type(self.buy))
        print("Find:", self.find, '\t', type(self.find))
        print("Drop:", self.drop, '\t', type(self.drop))
        print("Type:", self.type, '\t', type(self.type))
        print("Stats:", self.stats, '\t', type(self.stats))
        print("Resistance:", self.resistance, '\t', type(self.resistance))
        print("Description:", self.description, '\t', type(self.description))
        print("Used as item:", self.used_as_item, '\t', type(self.used_as_item))
        print("End of turn:", self.end_of_turn, '\t', type(self.end_of_turn))

    def equiped_by_exact_class(self, lst: list) -> list:
        return equiped_by_exact_class(lst)

    def str_to_dict(self, s: str = "-"):  # return str ("-") or dict
        return str_to_dict(s)

    def porcentage_to_decimal(self, porc: str):
        return porcentage_to_decimal(porc)

    def getAllStats(self) -> dict:  # self.stats es dict, excepto si es '-'
        aux = {'STR': 0, 'AGL': 0, 'INT': 0, 'STA': 0, 'LCK': 0, 'HP_MAX': 1.0, 'MP_MAX': 1.0}
        if self.stats == '-':
            return aux
        else:
            if 'STR' in self.stats:
                aux['STR'] = int(self.stats['STR'] * self.mult)
            if 'AGL' in self.stats:
                aux['AGL'] = int(self.stats['AGL'] * self.mult)
            if 'INT' in self.stats:
                aux['INT'] = int(self.stats['INT'] * self.mult)
            if 'STA' in self.stats:
                aux['STA'] = int(self.stats['STA'] * self.mult)
            if 'LCK' in self.stats:
                aux['LCK'] = int(self.stats['LCK'] * self.mult)
            if 'HP_MAX' in self.stats:
                aux['HP_MAX'] = float((self.stats['HP_MAX'] - 1.0) * self.mult) + 1.0
            if 'MP_MAX' in self.stats:
                aux['MP_MAX'] = float((self.stats['MP_MAX'] - 1.0) * self.mult) + 1.0
            # print('getAllStats: aux:', aux)
            return aux

    # def get_DEF(self):
    #     return self.DEF
    #
    # def get_EVA(self):
    #     return self.EVA
    #
    # def get_WEI(self):
    #     return self.WEI

    def validar_nombre_armadura(self, nombre: str) -> bool:
        if nombre == '' or nombre in ARMADURAS.keys():
            return True
        else:
            print(f"Nombre de armadura inválido. Debe ser '' o uno del archivo csv.")
            return False

    def armadura_es_tipo_correcto(self, slot_armor_str, armor_name):
        print(f"slot_armor_str:\t{slot_armor_str}")
        print(f"armor_name:\t{armor_name}")
        if armor_name == '':
            return True
        elif slot_armor_str == ARMADURAS[armor_name]['type']:
            return True
        else:
            print(f"Nombre de armadura con tipo de armadura incorrecta.")
            return False

    def get_gear_mult_color(self, mult):
        return get_gear_mult_color(mult)

    def get_price_with_mult(self):
        return get_price_with_mult(
            name=self.name,
            mult=self.mult,
            catalog=ARMADURAS
        )

    def get_value_with_mult(self):
        return get_value_with_mult(self.price, self.mult)

    def get_def_with_mult(self):
        def_str = 0 if self.name == '' else ARMADURAS[self.name]['DEF']
        try:
            def_num = int(def_str)
            final_def = math.trunc(def_num * self.mult)  # Initial (def x mult)
            return final_def  # Devuelve un número entero/flotante
        except ValueError:
            return f"{def_str} x {str(self.mult)}"  # Devuelve un string

    def get_eva_with_mult(self):
        eva_str = 0 if self.name == '' else ARMADURAS[self.name]['EVA']
        try:
            eva_num = int(eva_str)
            final_eva = math.trunc(eva_num * self.mult)  # Initial (eva x mult)
            return final_eva  # Devuelve un número entero/flotante
        except ValueError:
            return f"{eva_str} x {str(self.mult)}"  # Devuelve un string

    def get_wei_with_mult(self):
        wei_str = 0 if self.name == '' else ARMADURAS[self.name]['WEI']
        try:
            wei_num = int(wei_str)
            final_wei = math.trunc(wei_num * self.mult)  # Initial (wei x mult)
            return final_wei  # Devuelve un número entero/flotante
        except ValueError:
            return f"{wei_str} x {str(self.mult)}"  # Devuelve un string

    def mostrar_gear_stats(self):
        # print(f"===== mostrar_gear_stats =====")
        price_base_str = ARMADURAS[self.name]['price']
        calculated_price = self.price
        def_base_str = ARMADURAS[self.name]['DEF']
        eva_base_str = ARMADURAS[self.name]['EVA']
        wei_base_str = ARMADURAS[self.name]['WEI']

        print(f"\t{self.decored_name} Value_Market_Mult: {self.value_market_mult()}")
        print(f"\t\tPrice: {self.get_operation_type_A(price_base_str)} = {self.price}")
        print(f"\t\tValue: {self.get_operation_type_B(calculated_price)} = {self.value}")
        print(f"\t\tDEF: {self.get_operation_type_C(def_base_str)} = {self.DEF}")
        print(f"\t\tEVA: {self.get_operation_type_C(eva_base_str)} = {self.EVA}")
        print(f"\t\tWEI: {self.get_operation_type_C(wei_base_str)} = {self.WEI}")
        print(f"\t\tStats: {self.getAllStats()}")

    def value_market_mult(self):
        return value_market_mult(self.mult)

    def get_operation_type_A(self, num):
        return get_operation_type_A(num, self.mult)

    def get_operation_type_B(self, num):
        return get_operation_type_B(num)

    def get_operation_type_C(self, num):
        return get_operation_type_C(num, self.mult)

    def mostrar_datos_5(self):
        """Muestra los stats de esta armadura"""
        print(f"    DEF: {self.DEF}")
        print(f"    EVA: {self.EVA}")
        print(f"    WEI: {self.WEI}")

    def get_decored_name(self):
        return get_decored_name(self)


# Probar la creación de las Armaduras con sus Gears
for name, dictionary in ARMADURAS.items():
    # print(f"{name}")
    my_armadura_01 = Armadura(name)
    my_armadura_01.mostrar_gear_stats()