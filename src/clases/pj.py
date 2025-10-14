import random
import math

from src.clases.arma import Arma
from src.utils.constantes import ESTADISTICAS_BASE, XP_TABLE, CRECIMIENTO_GARANTIZADO


class PJ:
    def __init__(self, clase:str="Warrior", name:str="no_name", LV:int=1):
        """
                Inicializa el personaje jugable con su nombre y clase.

                Args:
                    nombre (str): Nombre del personaje
                    clase (str): Clase del personaje ('Warrior', 'Thief', etc.)
                """
        self.name = name
        self.clase = clase
        self.LV = 1
        self.XP = 0
        self.MAX_LV = len(XP_TABLE)  # 99
        self.XP_limit0 = self.xp_Lv(self.LV, self.MAX_LV)
        self.XP_limit1 = self.xp_Lv(self.LV + 1, self.MAX_LV)
        self.arma = self.arma_inicial(self.clase)
        self.asignar_estadisticas_base() # Variables: STR_base,AGL_base,INT_base,STA_base,LCK_base
        self.asignar_estadisticas() # Variables: HP,MP,STR,AGL,INT,STA,LCK
        self.asignar_estadisticas_secundarias() # Variables: ATK,ACC,DEF,EVA,CRIT,MD
        self.asignar_HP_MAX_MP_MAX_y_sus_bases() # HP_MAX_base,MP_MAX_base,HP_MAX,MP_MAX
        self.levelear_si_es_necesario(LV)

        self.espera = 0
        self.alive = True
        self.char_type = "pj"
        # self.actualizar_HP_MAX()

    def xp_Lv(self, Nxt_Lv, max_Lv):
        if Nxt_Lv > max_Lv:
            return math.inf
        else:
            return XP_TABLE[Nxt_Lv] #df_XP_Table.iloc[Nxt_Lv - 1, 1]

    def asignar_estadisticas_base(self):
        """Asigna las estadísticas _base."""
        # Inicializar estadísticas con valores _base
        self.STR_base = self.obtener_estadistica('STR')
        self.AGL_base = self.obtener_estadistica('AGL')
        self.INT_base = self.obtener_estadistica('INT')
        self.STA_base = self.obtener_estadistica('STA')
        self.LCK_base = self.obtener_estadistica('LCK')

    def asignar_estadisticas(self):
        """Asigna las estadísticas."""
        # Inicializar estadísticas con valores base
        self.HP = self.obtener_estadistica('HP')
        self.MP = self.obtener_estadistica('MP')
        self.STR = self.STR_base
        self.AGL = self.AGL_base
        self.INT = self.INT_base
        self.STA = self.STA_base
        self.LCK = self.LCK_base
        # print(f"self.HP: {self.HP}")

    def asignar_estadisticas_secundarias(self):
        self.asignar_ATK()
        self.ACC = self.obtener_estadistica('Ini_ACC') + self.AGL + self.LV*self.obtener_estadistica('Mul_ACC')# + self.arma.acc
        self.asignar_DEF()
        self.EVA = self.obtener_estadistica('Ini_EVA') + 2 * self.AGL
        self.asignar_CRIT()
        self.MD = self.obtener_estadistica('Ini_MD') + self.LV *self.obtener_estadistica('Mul_MD')

    def actualizar_stats_secundarias_despues_de_leveleo(self):
        self.asignar_estadisticas_secundarias()

    def actualizar_stats_por_arma_y_secundarias(self):
        arma_stats = self.arma.getAllStats()
        self.STR += arma_stats['STR']
        self.AGL += arma_stats['AGL']
        self.INT += arma_stats['INT']
        self.STA += arma_stats['STA']
        self.LCK += arma_stats['LCK']
        # Actualizar el resto de stats (secundarias)
        self.actualizar_stats_secundarias_despues_de_leveleo()
        self.EVA += arma_stats['EVA']
        pass

    def get_atk_del_arma(self):
        if isinstance(self.arma.atk, str):
            if self.arma.atk == 'HP/10':
                return self.HP // 10
            elif self.arma.atk.isdigit():
                return int(self.arma.atk)
        return 0

    def get_arma_acc(self):
        if isinstance(self.arma.acc, str):
            if self.arma.acc == 'HP/10':
                return self.HP // 10
            elif self.arma.acc.isdigit():
                return int(self.arma.acc)
        return 0

    def get_arma_crit(self):
        return int(self.arma.crit)

    def asignar_ATK(self):
        if self.clase in ['Monk', 'Master'] and not self.armado():
            if self.clase == 'Monk':
                self.ATK = self.STR // 2 + (self.STA + 1) * 3 // 4
            elif self.clase == 'Master':
                self.ATK = self.STR // 2 + self.STA
        else:
            ### Standard ###
            self.ATK = self.get_atk_del_arma() + self.STR//2
            # print(f"LV: {self.LV}\tHP: {self.HP}\tarma_atk: {self.get_atk_del_arma()}\tself.STR//2: {self.STR//2}")

    def asignar_DEF(self):
        if self.clase in ['Monk', 'Master']:
            self.DEF = self.STA // 2
        else:
            ### Sum of the character's equipment's DEF
            self.DEF = 0

    def asignar_CRIT(self):
        if self.clase in ['Monk', 'Master']:
            ### Unarmed Monk or Master ###
            self.CRIT = self.LV * 2
        else:
            ### Weapon CRIT ###
            # self.CRIT = self.weapon.CRIT
            self.CRIT = 0 # + self.arma.acc

    def obtener_estadistica(self, stat):
        """Calcula el valor final de una estadística basada en el nivel."""
        return ESTADISTICAS_BASE[self.clase][stat]

    def levelear_si_es_necesario(self, LV:int):
        if self.LV == 1:
            return
        else:
            self.LV = LV
            iter = self.LV - 1
            for i in range(iter):
                self.Lv1UP()

    def Lv1UP(self, show_title = False):
        self.actualizar_LV_y_XP()
        self.actualizar_stats_principales_despues_de_leveleo(show_title)
        # self.actualizar_stats_por_arma_y_secundarias_despues_de_leveleo() # incluyen stats principales que no son base
        self.actualizar_stats_por_arma_y_secundarias() # incluyen stats principales que no son base
        # self.actualizar_stats_secundarias_despues_de_leveleo()

    def actualizar_LV_y_XP(self):
        self.LV += 1
        self.XP_limit0 = self.xp_Lv(self.LV, self.MAX_LV)
        self.XP_limit1 = self.xp_Lv(self.LV + 1, self.MAX_LV)

    def actualizar_stats_principales_despues_de_leveleo(self, show_title):
        # self.HP_MAX = self.HP_MAX + (self.STA // 4) + 1 + self.prob_aum(0.5) * random.randint(20, 25)
        self.aumentar_HP_MAX()
        self.aumentar_MP_MAX()
        self.STR_base = self.STR_base + self.aumentar_stat("S")
        self.AGL_base = self.AGL_base + self.aumentar_stat("A")
        self.INT_base = self.INT_base + self.aumentar_stat("I")
        self.STA_base = self.STA_base + self.aumentar_stat("V")
        self.LCK_base = self.LCK_base + self.aumentar_stat("L")
        self.STR = self.STR_base
        self.AGL = self.AGL_base
        self.INT = self.INT_base
        self.STA = self.STA_base
        self.LCK = self.LCK_base
        # self.mostrar(show_title)  #

    # def prob_aum(self, prob):
    #     if prob > random.random():
    #         return 1
    #     else:
    #         return 0

    def aumentar_HP_MAX(self):
        self.HP_MAX = self.HP_MAX + self.STA // 4 + 1 + self.consulta_gran_MP() # self.prob_aum(0.5) * random.randint(20, 25)

    def consulta_gran_HP(self) -> int:
        growth_text = CRECIMIENTO_GARANTIZADO[self.LV][self.clase]
        if "H" in growth_text:
            return self.obtener_gran_aumento_de_HP()
        elif random.randint(1, 8) == 1:
            return self.obtener_gran_aumento_de_HP()
        else:
            return 0

    def obtener_gran_aumento_de_HP(self) -> int:
        return random.randint(20, 25)

    def aumentar_MP_MAX(self):
        if self.clase not in ['Warrior', 'Thief', 'Monk', 'Master']:
            self.MP_MAX = self.MP_MAX + self.INT // 4 + 1 + self.consulta_gran_MP()

    def consulta_gran_MP(self) -> int:
        growth_text = CRECIMIENTO_GARANTIZADO[self.LV][self.clase]
        if "M" in growth_text:
            return self.obtener_gran_aumento_de_MP()
        elif random.randint(1, 8) == 1:
            return self.obtener_gran_aumento_de_MP()
        else:
            return 0

    def obtener_gran_aumento_de_MP(self) -> int:
        return random.randint(10, 12)

    def aumentar_stat(self, char:str) -> int:
        growth_text = CRECIMIENTO_GARANTIZADO[self.LV][self.clase]
        if char in growth_text:
            return 1
        elif random.randint(1, 8) == 1:
            return 1
        else:
            return 0

    def asignar_HP_MAX_MP_MAX_y_sus_bases(self):
        self.HP_MAX_base = self.HP
        self.MP_MAX_base = self.MP
        self.HP_MAX = self.HP
        self.MP_MAX = self.MP
        # self.HP_MAX = self.HP + (self.LV * self.STA // 4)
        # self.HP = self.HP_MAX
        # self.MP_MAX = self.MP + (self.LV * self.INT // 4)
        # self.HP = self.HP_MAX

    def ajustar_vida(self):
        if self.HP < 0:
            self.HP = 0
            self.alive = False
        if self.HP > self.HP_MAX:
            self.HP = self.HP_MAX

    def armado(self):
        if self.arma.name == 'Hands':
            return False
        else:
            return True

    def up_or_down_HP(self, quant):
        self.HP = max(0, min(self.HP+quant, self.HP_MAX))
        if self.HP == 0:
            self.alive = False

    def arma_inicial(self, tipo):
        if tipo == 'Warrior' or tipo == 'Thief' or tipo == 'B. Mage' or tipo == 'R. Mage'\
                or tipo == 'Fi' or tipo == 'Th' or tipo == 'BM' or tipo == 'RM'\
                or tipo == 'Knight' or tipo == 'Ninja' or tipo == 'B. Wizard' or tipo == 'R. Wizard'\
                or tipo == 'Kn' or tipo == 'Ni' or tipo == 'BW' or tipo == 'RW':
            return Arma('Knife')
        # elif tipo == 'W. Mage' or tipo == 'Monk' or tipo == 'W. Wizard' or tipo == 'Master'\
        #         or tipo == 'WM' or tipo == 'BB' or tipo == 'WW' or tipo == 'Ma':
        #     return Arma('Staff')
        elif tipo == 'W. Mage' or tipo == 'W. Wizard' or tipo == 'WM' or tipo == 'WW':
            return Arma('Staff')
        else: # 'Monk', 'Master', 'BB' y 'Ma'
            return Arma('Hands')

    def cambiar_arma(self, nueva_arma_name):
        self.arma = Arma(nueva_arma_name)
        self.actualizar_stats_por_arma_y_secundarias()








    def mostrar_datos(self):
        print(f"-" * 10, f"{self.name}", f"-" * 10)
        print(f"{self.clase} - LV. {self.LV}")
        print(f"HP: {self.HP} / {self.HP_MAX}")
        print(f"MP: {self.MP} / {self.MP_MAX}")
        print(f"XP: {self.XP}")
        print(f"MAX_LV: {self.MAX_LV}")
        print(f"XP_limit0: {self.XP_limit0}")
        print(f"XP_limit1: {self.XP_limit1}")
        print(f"STR\tAGL\tINT\tSTA\tLCK")
        print(f"{self.STR}\t{self.AGL}\t{self.INT}\t{self.STA}\t{self.LCK}")
        print(f"ATK\tACC\tDEF\tEVA\tCRI\tMD")
        print(f"{self.ATK}\t{self.ACC}\t{self.DEF}\t{self.EVA}\t{self.CRIT}\t{self.MD}")
        print(f"espera: {self.espera}")
        print(f"alive: {self.alive}")

    def mostrar_datos_2(self):
        print(f"-" * 10, f"{self.name}", f"-" * 10)
        print(f"{self.clase} - LV. {self.LV}")
        print(f"HP: {self.HP} / {self.HP_MAX}")
        print(f"MP: {self.MP} / {self.MP_MAX}")
        print(f"STR\tAGL\tINT\tSTA\tLCK")
        print(f"{self.STR}\t{self.AGL}\t{self.INT}\t{self.STA}\t{self.LCK}")
        print(f"ATK\tACC\tDEF\tEVA\tCRI\tMD")
        print(f"{self.ATK}\t{self.ACC}\t{self.DEF}\t{self.EVA}\t{self.CRIT}\t{self.MD}")
        print(f"espera: {self.espera}")
        print(f"alive: {self.alive}")

    def mostrar_datos_3(self):
        print(f"-" * 10, f"{self.name}", f"-" * 10)
        print(f"{self.clase} - LV. {self.LV}")
        print(f"HP: {self.HP} / {self.HP_MAX}")
        print(f"MP: {self.MP} / {self.MP_MAX}")
        print(f"alive: {self.alive}")

    def mostrar_datos_4(self):
        print(f"\t\t===== mostrar_datos_4 =====")
        print(f"-" * 10, f"{self.name}", f"-" * 10)
        print(f"-" * 8, f"{self.clase} - {self.LV}", f"-" * 8)
        print(f"HP: {self.HP} / {self.HP_MAX}")
        print(f"STR_b\tAGL_b\tINT_b\tSTA_b\tLCK_b")
        print(f"{self.STR_base}\t\t{self.AGL_base}\t\t{self.INT_base}\t\t{self.STA_base}\t\t{self.LCK_base}")
        print(f"STR\t\tAGL\t\tINT\t\tSTA\t\tLCK")
        print(f"{self.STR}\t\t{self.AGL}\t\t{self.INT}\t\t{self.STA}\t\t{self.LCK}")
        self.asignar_ATK()
        print(f"ATK: {self.ATK}\t\tATK_weapon ({self.arma.name}): {self.get_atk_del_arma()}")
        # print(f"XP: {self.XP}")
        # print(f"XP_limit0: {self.XP_limit0}")
        # print(f"XP_limit1: {self.XP_limit1}")
        print(f"\t\t===========================")