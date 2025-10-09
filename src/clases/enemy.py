from src.utils.constantes import ENEMIGOS

class Enemy:
    def __init__(self, name):
        self.name = name
        self.HP = ENEMIGOS[name]['HP']
        self.ATK = ENEMIGOS[name]['ATK']
        self.DEF = ENEMIGOS[name]['DEF']
        self.MD = ENEMIGOS[name]['MD']
        self.WEAK = self.remove_None(ENEMIGOS[name]['WEAK'])
        self.RESI = self.remove_None(ENEMIGOS[name]['RESI'])
        self.gil = ENEMIGOS[name]['gil']
        self.XP = ENEMIGOS[name]['XP']
        self.Hits = ENEMIGOS[name]['Hits']
        self.ACC = ENEMIGOS[name]['ACC']
        self.status = ENEMIGOS[name]['status']
        self.CRIT = ENEMIGOS[name]['CRIT']
        self.EVA = ENEMIGOS[name]['EVA']
        self.run_level = ENEMIGOS[name]['run_level']
        self.magic = ENEMIGOS[name]['magic']
        self.sp_atk = ENEMIGOS[name]['sp_atk']
        self.family = ENEMIGOS[name]['family']
        self.AGL = ENEMIGOS[name]['AGL']
        self.espera = 0
        self.alive = True
        self.char_type = "enemy"

    def motrar_datos(self):
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

    def remove_None(self, lst):
        for text in lst:
            if text is None:
                return "-"

# chaos = Enemy("Chaos")
# chaos.motrar_datos()