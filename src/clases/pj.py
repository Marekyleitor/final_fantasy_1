import random
import math

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
        self.asignar_estadisticas_base() # Variables: STR_base,AGL_base,INT_base,STA_base,LCK_base
        self.asignar_estadisticas() # Variables: HP,MP,STR,AGL,INT,STA,LCK
        self.asignar_estadisticas_secundarias() # Variables: ATK,ACC,DEF,EVA,CRIT,MD
        self.asignar_HP_MAX_MP_MAX_y_sus_bases() # HP_MAX_base,MP_MAX_base,HP_MAX,MP_MAX
        self.levelear_si_es_necesario(LV)
        # self.weapon = arma_inicial(self.clase)
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
        self.ACC = self.obtener_estadistica('Ini_ACC') + self.AGL + self.LV*self.obtener_estadistica('Mul_ACC')
        self.asignar_DEF()
        self.EVA = self.obtener_estadistica('Ini_EVA') + 2 * self.AGL
        self.asignar_CRIT()
        self.MD = self.obtener_estadistica('Ini_MD') + self.LV *self.obtener_estadistica('Mul_MD')

    def asignar_ATK(self):
        if self.clase in ['Monk', 'Master'] and not self.armado():
            if self.clase == 'Monk':
                self.ATK = self.STR // 2 + (self.STA + 1) * 3 // 4
            elif self.clase == 'Master':
                self.ATK = self.STR // 2 + self.STA
        else:
            ### Standard ###
            # self.ATK = Weapon Attack + self.STR//2
            self.ATK = self.STR // 2

    def asignar_DEF(self):
        if self.clase not in ['Monk', 'Master']:
            self.DEF = self.STA // 2
        else:
            ### Sum of the character's equipment's DEF
            self.DEF = 0

    def asignar_CRIT(self):
        if self.clase not in ['Monk', 'Master']:
            ### Unarmed Monk or Master ###
            self.CRIT = self.LV * 2
        else:
            ### Weapon CRIT ###
            # self.CRIT = self.weapon.CRIT
            self.CRIT = 0

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
        self.actualizar_stats(show_title)

    def actualizar_LV_y_XP(self):
        self.LV += 1
        self.XP_limit0 = self.xp_Lv(self.LV, self.MAX_LV)
        self.XP_limit1 = self.xp_Lv(self.LV + 1, self.MAX_LV)

    def actualizar_stats(self, show_title):
        # self.HP_MAX = self.HP_MAX + (self.STA // 4) + 1 + self.prob_aum(0.5) * random.randint(20, 25)
        self.aumentar_HP_MAX()
        self.aumentar_MP_MAX()
        # self.STR = self.STR + self.prob_aum(0.75)
        # self.AGL = self.AGL + self.prob_aum(0.625)
        # self.INT = self.INT + self.prob_aum(0.32)
        # self.STA = self.STA + self.prob_aum(0.5)
        # self.LCK = self.LCK + self.prob_aum(0.5)
        self.STR = self.STR + self.aumentar_stat("S")
        self.AGL = self.AGL + self.aumentar_stat("A")
        self.INT = self.INT + self.aumentar_stat("I")
        self.STA = self.STA + self.aumentar_stat("V")
        self.LCK = self.LCK + self.aumentar_stat("L")
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
        # if self.weapon.nombre == 'Hands'
        return False
        # else:
        # return True

    # def arma_inicial(tipo):
    #     if tipo == 'Fi' or tipo == 'Th' or tipo == 'BM' or tipo == 'RM':
    #         return Arma('Knife')
    #     elif tipo == 'WM' or tipo == 'BB':
    #         return Arma('Staff')

    def motrar_datos(self):
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

# guerrero = PJ("Warrior")
# print(f"\nEstadísticas del guerrero nivel {guerrero.LV}:")
# guerrero.motrar_datos()
# print(f"guerrero.HP: {guerrero.HP}")
# print(f"guerrero.HP_MAX: {guerrero.HP_MAX}")
# print(XP_TABLE[35])
# print(XP_TABLE.get(35))
# print(len(XP_TABLE))
# print(guerrero.XP_limit0)
# print(guerrero.XP_limit1)
# # print(CRECIMIENTO_GARANTIZADO)
# print(CRECIMIENTO_GARANTIZADO[9])
# print(CRECIMIENTO_GARANTIZADO[9]["Thief"])

