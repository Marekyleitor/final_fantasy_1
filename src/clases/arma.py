from src.utils.constantes import ARMAS

class Arma:
    def __init__(self, name):
        self.nombre = name
        if name != 'Hands':
            self.price = ARMAS[self.nombre]['Price']
            self.value = 0
            if isinstance(self.price, int):
                self.value = self.price // 2
            self.atk = ARMAS[self.nombre]['atk']
            self.acc = ARMAS[self.nombre]['acc']
            self.crit = ARMAS[self.nombre]['crit']
            self.equip_by = self.equiped_by_exact_class(ARMAS[self.nombre]['equip_by']) # List
            self.buy = ARMAS[self.nombre]['buy']
            self.find = ARMAS[self.nombre]['find']
            self.win = ARMAS[self.nombre]['win']
            self.special = ARMAS[self.nombre]['special']
            self.tipo = ARMAS[self.nombre]['tipo']
            self.str_vs = ARMAS[self.nombre]['str_vs']
            self.elemental = ARMAS[self.nombre]['elemental']
            self.cast = ARMAS[self.nombre]['cast']
            self.inflicts = ARMAS['inflicts'][self.nombre]
            self.stats = self.str_to_dict(ARMAS[self.nombre]['stats'])
            self.allStats = self.getAllStats(self.stats)
            self.seba = ARMAS[self.nombre]['seba']
            self.seaa = ARMAS[self.nombre]['seaa']
        else:
            self.price,self.value,self.atk,self.acc,self.crit,self.equip_by = 0,0,0,0,0,'All clases'
            self.buy,self.find,self.win,self.special,self.tipo,self.str_vs = '-','-','-',False,'-','-'
            self.elemento,self.cast,self.inflige,self.stats,self.seba,self.seaa = '-','-','-','-','-','-'

    def mostrar_Info(self):
        print("Precio:", self.price, '\t', type(self.price))
        print("Atk:", self.atk, '\t', type(self.atk))
        print("Acc:", self.acc, '\t', type(self.acc))
        print("Crit:", self.crit, '\t', type(self.crit))
        print("Equipped by:", self.equip_by, '\t', type(self.equip_by))
        print("Buy:", self.buy, '\t', type(self.buy))
        print("Find:", self.find, '\t', type(self.find))
        print("Win:", self.win, '\t', type(self.win))
        print("Special:", self.special, '\t', type(self.special))
        print("Type:", self.tipo, '\t', type(self.tipo))
        print("Strong vs:", self.str_vs, '\t', type(self.str_vs))
        print("Element:", self.elemento, '\t', type(self.elemento))
        print("Cast:", self.cast, '\t', type(self.cast))
        print("Inflicts:", self.inflige, '\t', type(self.inflige))
        print("Stats:", self.stats, '\t', type(self.stats))
        print("Special Effect Before Attack:", self.seba, type(self.seba))
        print("Special Effect After Attack:", self.seaa, type(self.seaa))

    def equiped_by_exact_class(self, lst:list) -> list:
        """
            Traduce una lista de strings usando un diccionario de traducciones.
            Modifica la lista original.
            """
        # Diccionario de clase exacta del PJ (ejemplo)
        traducciones = {
            'Fi': 'Warrior',
            'Kn': 'Knight',
            'Th': 'Thief',
            'Ni': 'Ninja',
            'WM': 'W. Mage',
            'WW': 'W. Wizard',
            'BM': 'B. Mage',
            'BW': 'B. Wizard',
            'BB': 'Monk',
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

    def getAllStats(self, dic) -> dict:  # dic es dict, excepto si es '-'
        aux = {'STR': 0, 'AGL': 0, 'INT': 0, 'STA': 0, 'LCK': 0, 'EVA': 0}
        if dic == '-':
            return aux
        else:
            if 'STR' in dic:
                aux['STR'] = dic['STR']
            if 'AGL' in dic:
                aux['AGL'] = dic['AGL']
            if 'INT' in dic:
                aux['INT'] = dic['INT']
            if 'STA' in dic:
                aux['STA'] = dic['STA']
            if 'LCK' in dic:
                aux['LCK'] = dic['LCK']
            if 'EVA' in dic:
                aux['EVA'] = dic['EVA']
            # print('getAllStats: aux:', aux)
            return aux