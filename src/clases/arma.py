import random, math
from src.utils.constantes import ARMAS, RESET, FG_BRIGHT_BLACK, FG_BRIGHT_GREEN, FG_BRIGHT_CYAN, FG_BRIGHT_MAGENTA, \
    FG_BRIGHT_RED, FG_BRIGHT_YELLOW
from src.utils.utils_arma_armadura import equiped_by_exact_class, str_to_dict, porcentage_to_decimal, \
    get_gear_mult_color, get_price_with_mult, get_value_with_mult, value_market_mult, get_operation_type_A, \
    get_operation_type_B, get_operation_type_C, get_decored_name


class Arma:
    def __init__(self, name, mult: float = 0):
        self.name = name
        self.gear, self.mult, self.color = self.get_gear_mult_color(mult)
        # self.gear = "Legendary"
        # self.mult = 1.65
        # self.color = '\033[95m'
        self.compound_name = f"{self.name} | {self.gear} | {self.mult}"  # self.name + " | " + self.gear + " | " + self.mult
        self.decored_name = f"{self.color}{self.compound_name}{RESET}"
        if name != 'Hands':
            self.price = self.get_price_with_mult()  # ARMAS[name]['price']
            self.value = self.get_value_with_mult()  # 100
            if isinstance(self.price, int):
                self.value = self.price // 2
            self.atk = self.get_atk_with_mult()  # ARMAS[name]['atk']
            self.acc = self.get_acc_with_mult()  # ARMAS[name]['acc']
            self.crit = self.get_crit_with_mult()  # ARMAS[name]['crit']
            self.equip_by = self.equiped_by_exact_class(ARMAS[name]['equip_by'])  # List
            self.buy = ARMAS[name]['buy']
            self.find = ARMAS[name]['find']
            self.drop = ARMAS[name]['drop']
            self.gift = ARMAS[name]['gift']
            self.special = ARMAS[name]['special']
            self.type = ARMAS[name]['type']
            self.str_vs = ARMAS[name]['str_vs']
            self.elemental = ARMAS[name]['elemental']
            self.used_as_item = ARMAS[name]['used_as_item']
            self.inflicts = ARMAS[name]['inflicts']
            self.stats = self.str_to_dict(ARMAS[name]['stats'])
            self.allStats = self.getAllStats()
            self.seba = ARMAS[name]['seba']
            self.seaa = ARMAS[name]['seaa']
            self.description = ARMAS[name]['description']
        else:
            self.gear, self.mult = "", 0.00
            self.compound_name = f"{self.name}"
            self.decored_name = f"{self.name}"
            self.price, self.value, self.atk, self.acc, self.crit, self.equip_by = 0, 0, 0, 0, 0, 'All clases'
            self.buy, self.find, self.drop, self.gift, self.special, self.type, = '-', '-', '-', '-', False, '-'
            self.str_vs, self.elemental, self.used_as_item, self.inflicts, self.stats = '-', '-', '-', '-', '-'
            self.allStats, self.seba, self.seaa, self.description = self.getAllStats(), '-', '-', '-'

    def mostrar_datos(self):
        print("Precio:", self.price, '\t', type(self.price))
        print("Atk:", self.atk, '\t', type(self.atk))
        print("Acc:", self.acc, '\t', type(self.acc))
        print("Crit:", self.crit, '\t', type(self.crit))
        print("Equipped by:", self.equip_by, '\t', type(self.equip_by))
        print("Buy:", self.buy, '\t', type(self.buy))
        print("Find:", self.find, '\t', type(self.find))
        print("Drop:", self.drop, '\t', type(self.drop))
        print("Gift:", self.gift, '\t', type(self.gift))
        print("Special:", self.special, '\t', type(self.special))
        print("Type:", self.type, '\t', type(self.type))
        print("Strong vs:", self.str_vs, '\t', type(self.str_vs))
        print("Element:", self.elemental, '\t', type(self.elemental))
        print("Used as item:", self.used_as_item, '\t', type(self.used_as_item))
        print("Inflicts:", self.inflicts, '\t', type(self.inflicts))
        print("Stats:", self.stats, '\t', type(self.stats))
        print("Special Effect Before Attack:", self.seba, type(self.seba))
        print("Special Effect After Attack:", self.seaa, type(self.seaa))
        print("Description:", self.seaa, type(self.description))

    def equiped_by_exact_class(self, lst: list) -> list:
        return equiped_by_exact_class(lst)

    def str_to_dict(self, s: str = "-"):  # return str ("-") or dict
        return str_to_dict(s)

    def porcentage_to_decimal(self, porc: str):
        return porcentage_to_decimal(porc)

    def getAllStats(self) -> dict:  # self.stats es dict, excepto si es '-'
        aux = {'STR': 0, 'AGL': 0, 'INT': 0, 'STA': 0, 'LCK': 0, 'EVA': 0}
        if self.stats == '-':
            return aux
        else:
            if 'STR' in self.stats:
                aux['STR'] = self.stats['STR']
            if 'AGL' in self.stats:
                aux['AGL'] = self.stats['AGL']
            if 'INT' in self.stats:
                aux['INT'] = self.stats['INT']
            if 'STA' in self.stats:
                aux['STA'] = self.stats['STA']
            if 'LCK' in self.stats:
                aux['LCK'] = self.stats['LCK']
            if 'EVA' in self.stats:
                aux['EVA'] = self.stats['EVA']
            # print('getAllStats: aux:', aux)
            return aux

    # def get_atk(self):
    #     return self.atk
    #
    # def get_acc(self):
    #     return self.acc
    #
    # def get_crit(self):
    #     return self.crit

    def validar_nombre_arma(self, nombre: str) -> bool:
        return nombre == 'Hands' or nombre in ARMAS.keys()

    def get_gear_mult_color(self, mult):
        return get_gear_mult_color(mult)

    def get_price_with_mult(self):
        return get_price_with_mult(
            name=self.name,
            mult=self.mult,
            catalog=ARMAS
        )

    def get_value_with_mult(self):
        return get_value_with_mult(self.price, self.mult)

    def get_atk_with_mult(self):
        atk_str = ARMAS[self.name]['atk']
        try:
            # Intenta convertir el string a un número entero (int)
            # Si atk_str es "7", atk_num será 7. Si es "HP/10", saltará a 'except'
            atk_num = int(atk_str)
            # Si la conversión fue exitosa, realiza la multiplicación
            final_atk = math.trunc(atk_num * self.mult)
            return final_atk  # Devuelve un número entero/flotante
        except ValueError:
            # Si la conversión falló (porque era "HP/10" u otra cosa no numérica)
            # Entra aquí y aplica el formato de string
            return f"{atk_str} x {str(self.mult)}"  # Devuelve un string

    def get_acc_with_mult(self):
        acc_str = ARMAS[self.name]['acc']
        try:
            acc_num = int(acc_str)
            final_acc = math.trunc(acc_num * self.mult)  # Initial (Acc x mult)
            return final_acc  # Devuelve un número entero/flotante
        except ValueError:
            return f"{acc_str} x {str(self.mult)}"  # Devuelve un string

    def get_crit_with_mult(self):
        crit_str = ARMAS[self.name]['crit']
        try:
            crit_num = int(crit_str)
            final_crit = math.trunc(crit_num * self.mult)  # Initial (Crit x mult)
            return final_crit  # Devuelve un número entero/flotante
        except ValueError:
            return f"{crit_str} x {str(self.mult)}"  # Devuelve un string

    def mostrar_gear_stats(self):
        # print(f"===== mostrar_gear_stats =====")
        price_base_str = ARMAS[self.name]['price']
        calculated_price = self.price
        atk_base_str = ARMAS[self.name]['atk']
        acc_base_str = ARMAS[self.name]['acc']
        crit_base_str = ARMAS[self.name]['crit']

        print(f"\t{self.decored_name} Value_Market_Mult: {self.value_market_mult()}")
        print(f"\t\tPrice: {self.get_operation_type_A(price_base_str)} = {self.price}")
        print(f"\t\tValue: {self.get_operation_type_B(calculated_price)} = {self.value}")
        print(f"\t\tAtk: {self.get_operation_type_C(atk_base_str)} = {self.atk}")
        print(f"\t\tAcc: {self.get_operation_type_C(acc_base_str)} = {self.acc}")
        print(f"\t\tCrit: {self.get_operation_type_C(crit_base_str)} = {self.crit}")

    def value_market_mult(self):
        return value_market_mult(self.mult)

    def get_operation_type_A(self, num):
        return get_operation_type_A(num, self.mult)

    def get_operation_type_B(self, num):
        return get_operation_type_B(num)

    def get_operation_type_C(self, num):
        return get_operation_type_C(num, self.mult)

    def mostrar_datos_5(self):
        """Muestra los stats de esta arma"""
        print(f"    Atk: {self.atk}")
        print(f"    Acc: {self.acc}")
        print(f"    Crit: {self.crit}")

    def get_decored_name(self):
        return get_decored_name(self)


# Probar la creación de las Armas con sus Gears
for name, dictionary in ARMAS.items():
    # print(f"{name}")
    my_arma_01 = Arma(name)
    my_arma_01.mostrar_gear_stats()
