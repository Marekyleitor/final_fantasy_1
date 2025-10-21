from src.utils.constantes import ENEMIGOS

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
        self.espera = 0
        self.alive = True
        self.char_type = "enemy"

    def up_or_down_HP(self, quant):
        self.HP = max(0, min(self.HP+quant, ENEMIGOS[self.enemy_type]['HP']))
        if self.HP == 0:
            self.alive = False

    def mostrar_datos(self):
        print(f"-" * 10, f"Enemy: {self.enemy_type}", f"-" * 10)
        print("HP:", self.HP, '\t', type(self.HP))
        print("ATK:", self.ATK, '\t', type(self.ATK))
        print("DEF:", self.DEF, '\t', type(self.DEF))
        print("MD:", self.MD, '\t', type(self.MD))
        print("WEAK:", self.WEAK, '\t', type(self.WEAK))
        print("RESI:", self.RESI, '\t', type(self.RESI))
        print("Gil:", self.gil, '\t', type(self.gil))
        print("XP:", self.XP, '\t', type(self.XP))
        print("Hits:", self.Hits, '\t', type(self.Hits))
        print("ACC:", self.ACC, '\t', type(self.ACC))
        print("Status:", self.status, '\t', type(self.status))
        print("CRIT:", self.CRIT, '\t', type(self.CRIT))
        print("EVA:", self.EVA, '\t', type(self.EVA))
        print("Run_level:", self.run_level, '\t', type(self.run_level))
        print("Magic:", self.magic, '\t', type(self.magic))
        print("Sp_atk:", self.sp_atk, '\t', type(self.sp_atk))
        print("Family:", self.family, '\t', type(self.family))
        print("AGL:", self.AGL, '\t', type(self.AGL))

    def mostrar_datos_2(self):
        print(f"-" * 10, f"Enemy: {self.enemy_type}", f"-" * 10)
        print(f"HP: {self.HP} / {ENEMIGOS[self.enemy_type]['HP']}")
        print(f"ATK\tACC\tDEF\tEVA\tCRI\tMD")
        print(f"{self.ATK}\t{self.ACC}\t{self.DEF}\t{self.EVA}\t{self.CRIT}\t{self.MD}")
        print(f"AGL: {self.AGL}")
        print(f"alive: {self.alive}")

    def mostrar_datos_3(self):
        print(f"-" * 10, f"Enemy: {self.enemy_type}", f"-" * 10)
        print(f"HP: {self.HP} / {ENEMIGOS[self.enemy_type]['HP']}")
        print(f"alive: {self.alive}")

    def mostrar_datos_4(self):
        # print(f"\t\t===== mostrar_datos_4 (Enemy) =====")
        print(f"\tself.name: {self.name}")
        # print(f"-" * 10, f"self.name: {self.name}", f"-" * 10)
        # print(f"-" * 10, f"self.n_id: {self.n_id}", f"-" * 10)

    def remove_None(self, lst):
        for text in lst:
            if text is None:
                return "-"

# chaos = Enemy("Chaos")
# chaos.mostrar_datos()