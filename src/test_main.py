import random

from src.clases.personaje import *
from src.clases.pj import PJ
from src.clases.enemy import Enemy
from src.clases.arrCharacter import ArrCharacter

max_wait = 400

pj_1 = PJ('Warrior', 'Escanor')
pj_2 = PJ('Warrior', 'Arturo')
pj_3 = PJ('Thief', 'Robin Hood')
pj_4 = PJ('Monk', 'Eremita')

ene_1 = Enemy('Crazy Horse')
ene_2 = Enemy('Black Widow')
ene_3 = Enemy('Crawler')

char_lst = [pj_1,pj_2,pj_3,pj_4,ene_1,ene_2]
arrChar = ArrCharacter()
arrChar.addArrChar(char_lst)    # <- objeto ArrCharacter
party = arrChar.arrPer()        # <- objeto ArrCharacter
enemies = arrChar.arrEne()      # <- objeto ArrCharacter

def agregar_espera_aleatoria(arr_char):
    for char in arr_char.arr:
        char.espera = random.randint(0, max_wait)

def siguientes_x_turnos(arr_char, n):
    turnos = []
    acum = []
    chars_alive = arr_char.arrAlive()
    for i in range(chars_alive.get_n()):
        acum.append(chars_alive.get_char(i).espera)

    while len(turnos) < n:
        for j in range(chars_alive.get_n()):
            acum[j] += chars_alive.get_char(j).AGL
            if acum[j] >= max_wait:
                acum[j] -= max_wait
                turnos.append(chars_alive.get_char(j))
                print(f"{chars_alive.get_char(j).name}", end = ", ")
    print("...")
    return turnos

def for_prob_one_hit_ene_pj(ene_char, pj_char, n_acie, n_crit):
    prob_impact = 168
    my_rnd_0_200 = random.randint(0, 200)
    daño_ene = ene_char.ATK
    acc_ene = ene_char.ACC
    crit_ene = ene_char.CRIT
    defensa_pj = pj_char.DEF
    eva_pj = pj_char.EVA
    acierta = my_rnd_0_200 <= min(acc_ene + prob_impact, 255) - eva_pj
    critico = my_rnd_0_200 <= crit_ene
    if acierta:
        n_acie += 1
    if critico:
        n_crit += 1
    return n_acie, n_crit

def one_hit_att_tar(attacker, target):
    # ene_char => attacker
    # pj_char => target
    prob_impact = 168
    my_rnd_0_200 = random.randint(0,200)
    daño_att = attacker.ATK
    acc_att = attacker.ACC
    crit_att = attacker.CRIT
    defensa_tar = target.DEF
    eva_tar = target.EVA
    # prob_impact se reduce en 40 si el atacante está afectado por Oscuridad
    # aumenta en 40 si el defensor está afectado por Oscuridad
    # y aumenta en otros 40 si el defensor es débil al ataque
    acierta = my_rnd_0_200 <= min(acc_att+prob_impact, 255) - eva_tar
    critico = my_rnd_0_200 <= crit_att
    if acierta:
        if critico:
            print(f"Crit Damage: 2 * ({daño_att} - {defensa_tar}) = {2 * (daño_att - defensa_tar)}")
            return max(2 * (daño_att - defensa_tar), 0)
        else:
            print(f"Norm Damage: {daño_att} - {defensa_tar} = {daño_att - defensa_tar}")
            return max(daño_att - defensa_tar, 0)
    else:
        print("Miss Hit")
        return 0

# def ataque_ene_pj(ene_char, pj_char):
#     n_golpes = ene_char.Hits
#     daño_total = 0
#     for i in range(n_golpes):
#         daño_total += one_hit_att_tar(ene_char, pj_char)
#     pj_char.up_or_down_HP(-daño_total)
#     print(f"El HP de {pj_char.name} ha sido afectado en {-daño_total}")
#
# def ataque_pj_ene(pj_char, ene_char):
#     n_golpes = 1 + pj_char.ACC//32
#     daño_total = 0
#     for i in range(n_golpes):
#         daño_total += one_hit_att_tar(pj_char, ene_char)
#     ene_char.up_or_down_HP(-daño_total)
#     print(f"El HP de {pj_char.name} ha sido afectado en {-daño_total}")

def ataque_att_tar(attacker, target):
    if "pj" == attacker.char_type:
        n_golpes = 1 + attacker.ACC//32
    else:
        n_golpes = attacker.Hits
    # n_golpes = 1 + attacker.ACC//32 if "pj" == attacker.char_type else attacker.Hits
    daño_total = 0
    for i in range(n_golpes):
        daño_total += one_hit_att_tar(attacker, target)
    target.up_or_down_HP(-daño_total)
    print(f"El HP de {target.name} ha sido afectado en {-daño_total}")


# agregar_espera_aleatoria(arrChar)
# siguientes_x_turnos(arrChar, 8)
# # ataque_ene_pj(ene_3, pj_1)
# # ataque_pj_ene(pj_1, ene_3)
# ataque_att_tar(ene_3, pj_1)
# ataque_att_tar(pj_1, ene_3)

# # Testear la probabilidad de acierto y crítico
# n_acie = 0
# n_crit = 0
# n = 10000000
# for i in range(n):
#     n_acie, n_crit = for_prob_one_hit_ene_pj(ene_3, pj_1, n_acie, n_crit)
# print(f"n_acie: {n_acie}/{n} => {n_acie/n*100}%")
# print(f"n_crit: {n_crit}/{n} => {n_crit/n*100}%")

pj_1.cambiar_arma("Ultima weapon")

pj_1.mostrar_datos_4()
for i in range(98):
    pj_1.Lv1UP()
    pj_1.HP = pj_1.HP_MAX
pj_1.mostrar_datos_4()

# pj_4.mostrar_datos_4()
# for i in range(98):
#     pj_4.Lv1UP()
# pj_4.mostrar_datos_4()