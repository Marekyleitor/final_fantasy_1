import random
from math import trunc


class Personaje:
    # Constructor: inicializa los atributos del objeto
    # def __init__(self, LV, EXP, HP, STR, AGL, VIT, ATK, HIT, EVA):
    #     self.LV = LV
    #     self.EXP = EXP
    #     self.HP = HP
    #     self.STR = STR
    #     self.AGL = AGL
    #     self.VIT = VIT
    #     self.ATK = ATK
    #     self.HIT = HIT
    #     self.EVA = EVA

    def __init__(self, con, LV, HP, STR, AGL, VIT, ATK, EVA, SPD):
        self.con = con
        self.LV = LV # 1
        self.HP = HP # 100
        self.HP_MAX = HP
        self.STR = STR # 23
        self.AGL = AGL # 12
        self.VIT = VIT # 19
        self.ATK = ATK # 5
        self.EVA = EVA # 38
        self.SPD = SPD # [5,7,9,4]
        self.espera = 0
        self.alive = True
        self.actualizar_HP_MAX()

    def actualizar_HP_MAX(self):
        self.HP_MAX = self.HP + (self.LV * self.VIT // 4)
        self.HP = self.HP_MAX

    def obtener_daño_ataque_físico(self):
        valor = self.ATK + 4 * self.STR//2
        return random.randint(valor-3, valor+3)

    def ajustar_vida(self):
        if self.HP < 0:
            self.HP = 0
            self.alive = False
        if self.HP > self.HP_MAX:
            self.HP = self.HP_MAX

    def recibir_daño_ataque_físico(self, ataque):
        esquiva = random.random() < self.EVA/256 + self.AGL/512 # TRUE: esquiva
        if esquiva:
            print(f"Ataque fue esquivado.")
        else:
            self.HP -= ataque
            self.ajustar_vida()
            print(f"Daño de ataque físico recibido: {ataque}.")

    def motrar_datos(self):
        print(f"{self.con} - LV. {self.LV}")
        print(f"HP: {self.HP} / {self.HP_MAX}")