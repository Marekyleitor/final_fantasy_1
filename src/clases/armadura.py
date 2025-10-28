from src.utils.constantes import ARMADURAS

class Armadura:
    def __init__(self, name):
        self.name = name
        if name != '':
            self.equip_by = self.equiped_by_exact_class(ARMADURAS[name]['equip_by'])
            self.price = ARMADURAS[name]['price']
            self.value = ARMADURAS[name]['value']
            self.DEF = ARMADURAS[name]['DEF']
            self.EVA = ARMADURAS[name]['EVA']
            self.WEI = ARMADURAS[name]['WEI']
            self.buy = ARMADURAS[name]['buy']
            self.find = ARMADURAS[name]['find']
            self.drop = ARMADURAS[name]['drop']
            self.type = ARMADURAS[name]['type']
            self.stats = self.str_to_dict(ARMADURAS[name]['stats'])
            self.resistance = ARMADURAS[name]['resistance']
            self.description = ARMADURAS[name]['description']
            self.used_as_item = ARMADURAS[name]['used_as_item']
            self.end_of_turn = ARMADURAS[name]['end_of_turn']
        else:
            self.equip_by,self.price,self.value,self.DEF,self.EVA,self.WEI, = 'All clases',0,0,0,0,0
            self.buy,self.find,self.drop,self.type,self.stats,self.resistance, = '-','-','-','-','-','-'
            self.description,self.used_as_item,self.end_of_turn = '-','-','-'

    def mostrar_datos(self):
        print("Name:", self.name, '\t', type(self.name))
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

    def porcentage_to_decimal(self, porc:str):
        porc = porc.replace("%", "")
        deci = float(int(porc) / 100)
        return 1 + deci

    def getAllStats(self) -> dict:  # self.stats es dict, excepto si es '-'
        aux = {'STR': 0, 'AGL': 0, 'INT': 0, 'STA': 0, 'LCK': 0, 'HP_MAX': 1, 'MP_MAX': 1}
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
            if 'HP_MAX' in self.stats:
                aux['HP_MAX'] = self.porcentage_to_decimal(self.stats['HP_MAX'])
            if 'MP_MAX' in self.stats:
                aux['MP_MAX'] = self.porcentage_to_decimal(self.stats['MP_MAX'])
            # print('getAllStats: aux:', aux)
            return aux

    def get_DEF(self):
        return self.DEF

    def get_EVA(self):
        return self.EVA - self.WEI

    def validar_nombre_armadura(self, nombre:str) -> bool:
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