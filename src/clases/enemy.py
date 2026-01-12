from src.utils.constantes import ENEMIGOS
from src.utils.constantes import VERDE, ROJO, AZUL, RESET

class Enemy:
    def __init__(self, enemy_type):
        self.enemy_type = enemy_type
        self.n_id = 1
        self.name = enemy_type + f" {self.n_id}"
        self.background = ENEMIGOS[enemy_type]['background']
        self.HP = ENEMIGOS[enemy_type]['HP']
        self.ATK = ENEMIGOS[enemy_type]['ATK']
        self.DEF = ENEMIGOS[enemy_type]['DEF']
        self.MD = ENEMIGOS[enemy_type]['MD']
        self.WEAK = self.remove_None(ENEMIGOS[enemy_type]['WEAK'])
        self.RESI = self.remove_None(ENEMIGOS[enemy_type]['RESI'])
        self.gil = ENEMIGOS[enemy_type]['gil']
        self.XP = ENEMIGOS[enemy_type]['XP']
        self.Hits = ENEMIGOS[enemy_type]['Hits']
        self.ACC = ENEMIGOS[enemy_type]['ACC']
        self.status = ENEMIGOS[enemy_type]['status']
        self.CRIT = ENEMIGOS[enemy_type]['CRIT']
        self.EVA = ENEMIGOS[enemy_type]['EVA']
        self.run_level = ENEMIGOS[enemy_type]['run_level']
        self.magic = ENEMIGOS[enemy_type]['magic']
        self.sp_atk = ENEMIGOS[enemy_type]['sp_atk']
        self.family = ENEMIGOS[enemy_type]['family']
        self.AGL = ENEMIGOS[enemy_type]['AGL']
        if self.AGL < 10:
            self.AGL = 10
        self.drop = ENEMIGOS[enemy_type]['drop']
        self.espera = 0
        self.alive = True
        self.char_type = "enemy"

    def up_or_down_HP(self, quant):
        self.HP = max(0, min(self.HP+quant, ENEMIGOS[self.enemy_type]['HP']))
        if self.HP == 0:
            self.alive = False

    def mostrar_datos(self):
        n_tabs = "\t" * 16
        print(n_tabs, f"-" * 10, f"Enemy: {self.enemy_type}", f"-" * 10)
        print(n_tabs, "HP:", self.HP, '\t', type(self.HP))
        print(n_tabs, "ATK:", self.ATK, '\t', type(self.ATK))
        print(n_tabs, "DEF:", self.DEF, '\t', type(self.DEF))
        print(n_tabs, "MD:", self.MD, '\t', type(self.MD))
        print(n_tabs, "WEAK:", self.WEAK, '\t', type(self.WEAK))
        print(n_tabs, "RESI:", self.RESI, '\t', type(self.RESI))
        print(n_tabs, "Gil:", self.gil, '\t', type(self.gil))
        print(n_tabs, "XP:", self.XP, '\t', type(self.XP))
        print(n_tabs, "Hits:", self.Hits, '\t', type(self.Hits))
        print(n_tabs, "ACC:", self.ACC, '\t', type(self.ACC))
        print(n_tabs, "Status:", self.status, '\t', type(self.status))
        print(n_tabs, "CRIT:", self.CRIT, '\t', type(self.CRIT))
        print(n_tabs, "EVA:", self.EVA, '\t', type(self.EVA))
        print(n_tabs, "Run_level:", self.run_level, '\t', type(self.run_level))
        print(n_tabs, "Magic:", self.magic, '\t', type(self.magic))
        print(n_tabs, "Sp_atk:", self.sp_atk, '\t', type(self.sp_atk))
        print(n_tabs, "Family:", self.family, '\t', type(self.family))
        print(n_tabs, "AGL:", self.AGL, '\t', type(self.AGL))
        print(n_tabs, "Drop:", self.drop, '\t', type(self.drop))

    def mostrar_datos_2(self):
        n_tabs = "\t" * 16
        print(n_tabs, f"-" * 10, f"Enemy: {self.enemy_type}", f"-" * 10)
        print(n_tabs, f"HP: {self.HP} / {ENEMIGOS[self.enemy_type]['HP']}")
        print(n_tabs, f"ATK\tACC\tDEF\tEVA\tCRI\tMD")
        print(n_tabs, f"{self.ATK}\t{self.ACC}\t{self.DEF}\t{self.EVA}\t{self.CRIT}\t{self.MD}")
        print(n_tabs, f"AGL: {self.AGL}")
        if self.alive:
            print(n_tabs, f"alive: {AZUL}{self.alive}{RESET}")
        else:
            print(n_tabs, f"alive: {ROJO}{self.alive}{RESET}")

    def mostrar_datos_3(self):
        n_tabs = "\t" * 16
        print(n_tabs, f"-" * 10, f"Enemy: {self.enemy_type}", f"-" * 10)
        print(n_tabs, f"HP: {self.HP} / {ENEMIGOS[self.enemy_type]['HP']}")
        if self.alive:
            print(n_tabs, f"alive: {AZUL}{self.alive}{RESET}")
        else:
            print(n_tabs, f"alive: {ROJO}{self.alive}{RESET}")

    def mostrar_datos_4(self):
        # print(f"\t\t===== mostrar_datos_4 (Enemy) =====")
        n_tabs = "\t" * 16
        print(n_tabs, f"\tself.name: {self.name}")
        # print(f"-" * 10, f"self.name: {self.name}", f"-" * 10)
        # print(f"-" * 10, f"self.n_id: {self.n_id}", f"-" * 10)

    def remove_None(self, lst):
        for text in lst:
            if text is None:
                return "-"

# chaos = Enemy("Chaos")
# chaos.mostrar_datos()