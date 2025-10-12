import random

from src.clases.personaje import *
from src.clases.pj import PJ
from src.clases.enemy import Enemy
from src.clases.arrCharacter import ArrCharacter

max_wait = 400

pj_1 = PJ('Warrior', 'Escanor')
pj_2 = PJ('Warrior', 'Arturo')
pj_3 = PJ('Thief', 'Robin Hood')
# pj_1 = PJ('Monk', 'Tenzin')
# pj_2 = PJ('Monk', 'Gyatso')
# pj_3 = PJ('Monk', 'Asceta')
pj_4 = PJ('Monk', 'Eremita')

# # Levelear a los personajes
# party_arr = [pj_1,pj_2,pj_3,pj_4]
# for i in range(10):
#     for p in party_arr:
#         p.Lv1UP()
# # HP y MP al máx
# for p in party_arr:
#     p.HP = p.HP_MAX
#     p.MP = p.MP_MAX

# Para party de Nivel 1
ene_1 = Enemy('Crazy Horse')
ene_2 = Enemy('Black Widow')

## Para party de Nivel 5
# ene_1 = Enemy('Werewolf')
# ene_2 = Enemy('Gigas Worm')
# # ene_3 = Enemy('Warg Wolf')

print(f"Enemies has appeared")
opc = -1
char_lst = [pj_1,pj_2,pj_3,pj_4,ene_1,ene_2]
arrChar = ArrCharacter()
arrChar.addArrChar(char_lst)
# party = arrChar.arrPer()
# enemies = arrChar.arrEne()

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

def proseguir_al_siguiente_turno(arr_char):
    chars_alive = arr_char.arrAlive()
    while(True):
        for j in range(chars_alive.get_n()):
            if chars_alive.get_char(j).espera >= max_wait:
                chars_alive.get_char(j).espera -= max_wait
                return chars_alive.get_char(j)
        for j in range(chars_alive.get_n()):
            chars_alive.get_char(j).espera += chars_alive.get_char(j).AGL

def ataque_fisico_de_enemigo_a_cualquier_jugador(ene_char, pjs_alive):
    # jug_char = []
    # for char in arr_char:
    #     if "COM" not in char.con:
    #         jug_char.append(char)
    # Seleccionar objetivo
    # if len(jug_char) == 1:
    #     daño = ene_char.obtener_daño_ataque_físico()
    #     per1.recibir_daño_ataque_físico(daño)
    n = pjs_alive.get_n()
    pos = random.randint(0, n - 1)
    # daño = ene_char.obtener_daño_ataque_físico()
    # pjs_alive.get_char(pos).recibir_daño_ataque_físico(daño)
    # ataque_ene_pj(ene_char, pjs_alive.get_char(pos))
    ataque_att_tar(ene_char, pjs_alive.get_char(pos))

def alive_chars(arr_char):
    personajes_vivos = []
    for char in arr_char:
        if char.alive:
            personajes_vivos.append(char)
    return personajes_vivos

def ejecutar_turno_de_enemigo(ene_char, arr_char):
    """
    param ene_char: El enemigo en turno
    param arr_char: arrCharacter de todos los personajes
    """
    # 1. Ataque físico; 2. Otros ataques
    atk_type = random.randint(1, 1)
    if atk_type == 1:
        pjs_alive = arr_char.arrPer().arrAlive()
        ataque_fisico_de_enemigo_a_cualquier_jugador(ene_char, pjs_alive)
    else:
        # No ataca porque no hay más que ataques físicos
        pass

def one_hit_att_tar(attacker, target):
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
            print(f"Crit Damage: 2 * {daño_att} - {defensa_tar} = {2 * daño_att - defensa_tar}")
            return max(2 * daño_att - defensa_tar, 0)
        else:
            print(f"Norm Damage: {daño_att} - {defensa_tar} = {daño_att - defensa_tar}")
            return max(daño_att - defensa_tar, 0)
    else:
        print("Miss Hit")
        return 0

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
    print(f"El HP de {target.name} ha sido afectado en {-daño_total}. Ahora es {target.HP}")
    if not target.alive:
        print(f" "*50, f"{target.name} HA MUERTO.")

def agregar_espera_aleatoria(arr_char):
    for char in arr_char.arr:
        char.espera = random.randint(0, max_wait)

# def dropear_enemigo_muerto(arr_char):
#     personajes_vivos = []
#     for char in arr_char:
#         if char.alive:
#             personajes_vivos.append(char)
#     arr_char = personajes_vivos

agregar_espera_aleatoria(arrChar)
pasa_turno = True

while(True):
    if pasa_turno:
        char_en_turno = proseguir_al_siguiente_turno(arrChar)
        print(f"")
        print(f"*" * 10, f"Turno de {char_en_turno.name}", f"*" * 10)
        if "enemy" == char_en_turno.char_type:
            # Ataque aleatorio de un enemigo a un jugador
            # print(f"Enemigo {char_en_turno.char_type} ha atacado.")
            # ataque_random_de_enemigo_a_jugador(char_en_turno, pers)
            ejecutar_turno_de_enemigo(char_en_turno, arrChar)
            continue
    opc = input("[1: Atacar; 2: Magia; 3: Defender; 4: Mostrar; 5: Turnos]: ")
    if opc == "1":
        enemies_alive = arrChar.arrEne().arrAlive()
        while(True):
            try:
                index = int(input(f"Ingresa un enemigo entre 1 y {enemies_alive.get_n()}: "))
                if 0 <= index-1 <= enemies_alive.get_n():
                    ataque_att_tar(char_en_turno, enemies_alive.get_char(index-1))
                    pasa_turno = True
                    break
            except ValueError:
                print("Valor inválido.")
    elif opc == "2":
        pasa_turno = False
    elif opc == "3":
        pasa_turno = False
    elif opc == "4":
        pasa_turno = False

        # print(f"*" * 10)
        # for p in arrChar.arr:
        #     p.mostrar_datos()
        # print(f"*" * 10)

        while (True):
            try:
                num = int(input(f"[1: Extremo detalle; 2: Detalle medio; 3: Básico]: "))
                if 1 <= num <= 3:
                    print(f"*" * 10)
                    if num == 1:
                        for p in arrChar.arr:
                            p.mostrar_datos()
                    elif num == 2:
                        for p in arrChar.arr:
                            p.mostrar_datos_2()
                    elif num == 3:
                        for p in arrChar.arr:
                            p.mostrar_datos_3()
                    print(f"*" * 10)
                    break
                else:
                    print("Valor inválido. Salida 1.")
            except ValueError:
                print("Valor inválido. Salida 2.")

    elif opc == "5":
        pasa_turno = False
        siguientes_x_turnos(arrChar, 8)
    else:
        pasa_turno = False
        print("Opcion invalida")