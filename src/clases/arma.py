import random, math
from src.utils.constantes import ARMAS, FG_BRIGHT_BLACK, FG_BRIGHT_GREEN, FG_BRIGHT_CYAN, FG_BRIGHT_MAGENTA, \
    FG_BRIGHT_RED, FG_BRIGHT_YELLOW
from src.utils.constantes import RESET

class Arma:
    # def __init__(self, name):
    #     self.name = name
    #     if name != 'Hands':
    #         self.price = ARMAS[name]['price']
    #         self.value = 100
    #         if isinstance(self.price, int):
    #             self.value = self.price // 2
    #         self.atk = ARMAS[name]['atk']
    #         self.acc = ARMAS[name]['acc']
    #         self.crit = ARMAS[name]['crit']
    #         self.equip_by = self.equiped_by_exact_class(ARMAS[name]['equip_by']) # List
    #         self.buy = ARMAS[name]['buy']
    #         self.find = ARMAS[name]['find']
    #         self.drop = ARMAS[name]['drop']
    #         self.special = ARMAS[name]['special']
    #         self.type = ARMAS[name]['type']
    #         self.str_vs = ARMAS[name]['str_vs']
    #         self.elemental = ARMAS[name]['elemental']
    #         self.cast = ARMAS[name]['cast']
    #         self.inflicts = ARMAS[name]['inflicts']
    #         self.stats = self.str_to_dict(ARMAS[name]['stats'])
    #         self.allStats = self.getAllStats()
    #         self.seba = ARMAS[name]['seba']
    #         self.seaa = ARMAS[name]['seaa']
    #     else:
    #         self.price,self.value,self.atk,self.acc,self.crit,self.equip_by = 0,0,0,0,0,'All clases'
    #         self.buy,self.find,self.drop,self.special,self.type,self.str_vs = '-','-','-',False,'-','-'
    #         self.elemental,self.cast,self.inflicts,self.stats = '-','-','-','-'
    #         self.allStats,self.seba,self.seaa = self.getAllStats(),'-','-'

    def __init__(self, name, mult:float=0):
        self.name = name
        self.gear, self.mult, self.color = self.get_gear_mult_color(mult)
        # self.gear = "Legendary"
        # self.mult = 1.65
        # self.color = '\033[95m'
        self.compund_name = f"{self.name} | {self.gear} | {self.mult}" # self.name + " | " + self.gear + " | " + self.mult
        self.decored_name = f"{self.color}{self.compund_name}{RESET}"
        if name != 'Hands':
            self.price = self.get_price_with_mult() # ARMAS[name]['price']
            self.value = self.get_value_with_mult() # 100
            if isinstance(self.price, int):
                self.value = self.price // 2
            self.atk = self.get_atk_with_mult() # ARMAS[name]['atk']
            self.acc = self.get_acc_with_mult() # ARMAS[name]['acc']
            self.crit = self.get_crit_with_mult() # ARMAS[name]['crit']
            self.equip_by = self.equiped_by_exact_class(ARMAS[name]['equip_by']) # List
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
            self.compund_name = f"{self.name}"
            self.decored_name = f"{self.name}"
            self.price,self.value,self.atk,self.acc,self.crit,self.equip_by = 0,0,0,0,0,'All clases'
            self.buy,self.find,self.drop,self.gift,self.special,self.type, = '-','-','-','-',False,'-'
            self.str_vs,self.elemental,self.used_as_item,self.inflicts,self.stats = '-','-','-','-','-'
            self.allStats,self.seba,self.seaa,self.description = self.getAllStats(),'-','-','-'

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

    def equiped_by_exact_class(self, lst:list) -> list:
        """
            Traduce una lista de strings usando un diccionario de traducciones.
            Modifica la lista original.
            """
        if lst[0] == 'All classes':
            return ['Warrior','Knight','Thief','Ninja','W. Mage','W. Wizard','B. Mage','B. Wizard','Monk','Master','R. Mage','R. Wizard']
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

    def str_to_dict(self, s:str="-"):# return str ("-") or dict
        if s == '-':
            return s
        else:
            s = s.replace("{", "")
            s = s.replace("}", "")
            arr = s.split(", ")
            miDic = {}
            for elem in arr:
                val = elem.split(":")
                miDic[val[0]] = int(val[1])
                # print(type(miDic[val[0]]))
            return miDic

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

    def validar_nombre_arma(self, nombre:str) -> bool:
        return nombre == 'Hands' or nombre in ARMAS.keys()

    def get_gear_mult_color(self, mult):
        G, M, C = "", 1.00, ""
        if mult == 0:   # mult será random
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

    def get_price_with_mult(self):
        price_str = ARMAS[self.name]['price']
        try:
            price_num = int(price_str)
            # final_price = math.trunc(price_num * self.mult) # Initial (Price x mult)
            # final_price = math.trunc(price_num * round((((self.mult - 1) / 0.05) + 1)))
            final_price = math.trunc(price_num * self.value_market_mult(self.mult))
            return final_price  # Devuelve un número entero/flotante
        except ValueError:
            return f"{price_str} x {str(self.mult)}"  # Devuelve un string

    def get_value_with_mult(self):
        if isinstance(self.price, int): # self.price ya es el resultado de get_price_with_mult(self)
            value = (self.price * self.mult) / 2
        else:
            value = 100 * self.mult     # Float
            s = str(value)              # String
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
            final_acc = math.trunc(acc_num * self.mult) # Initial (Acc x mult)
            return final_acc  # Devuelve un número entero/flotante
        except ValueError:
            return f"{acc_str} x {str(self.mult)}"  # Devuelve un string

    def get_crit_with_mult(self):
        crit_str = ARMAS[self.name]['crit']
        try:
            crit_num = int(crit_str)
            final_crit = math.trunc(crit_num * self.mult) # Initial (Crit x mult)
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

        print(f"\t{self.decored_name} Value_Market_Mult: {self.value_market_mult(self.mult)}")
        print(f"\t\tPrice: {self.get_operation_type_A(price_base_str)} = {self.price}")
        print(f"\t\tValue: {self.get_operation_type_B(calculated_price)} = {self.value}")
        print(f"\t\tAtk: {self.get_operation_type_C(atk_base_str)} = {self.atk}")
        print(f"\t\tAcc: {self.get_operation_type_C(acc_base_str)} = {self.acc}")
        print(f"\t\tCrit: {self.get_operation_type_C(crit_base_str)} = {self.crit}")

    def value_market_mult(self, mult):
        return round((((mult - 1) / 0.05) + 1))

    def get_operation_type_A(self, num):
        """
        Relacionados al Price del arma.

        Args:
        num: El Price (ej: 5, 800, 45, 100)

        Returns:
        String de la operación que se realizará para calcular el valor final
        """
        return f"{num} x {self.value_market_mult(self.mult)}"  # Devuelve un string

    def get_operation_type_B(self, num):
        """
        Relacionados al Value del arma.

        Args:
        num: El Price calculado del arma actual, no el base (ej: 5, 800, 45, 100)

        Returns:
        String de la operación que se realizará para calcular el valor final
        """
        return f"{num} / 2"  # Devuelve un string

    def get_operation_type_C(self, num):
        """
        Relacionados al Atk, Acc y Crit del arma.

        Args:
        num: El Atk, Acc o Crit (ej: 13, 20, 48)

        Returns:
        String de la operación que se realizará para calcular el valor final
        """
        return f"{num} x {self.mult}"  # Devuelve un string

    def mostrar_datos_5(self):
        print(f"    Atk: {self.atk}")
        print(f"    Acc: {self.acc}")
        print(f"    Crit: {self.crit}")

# Probar la creación de las Armas con sus Gears
for name, dictionary in ARMAS.items():
    # print(f"{name}")
    my_arma_01 = Arma(name)
    my_arma_01.mostrar_gear_stats()
