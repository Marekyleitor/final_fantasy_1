# ataque.py
import random


def ejecutar_ataque(char_en_turno, enemies_alive):
    pasa_turno = True
    try:
        text = input(f"Ingresa un enemigo entre 1 y {enemies_alive.get_n()}: ")
        if text == "q":
            pasa_turno = False
            print(f"Atacar cancelado.")
            return pasa_turno
        index = int(text)
        if 0 <= index - 1 < enemies_alive.get_n():
            ataque_att_tar(char_en_turno, enemies_alive.get_char(index - 1))
            pasa_turno = True
            return pasa_turno
    except ValueError:
        print("Valor inválido.")

def ataque_att_tar(attacker, target):
    if "pj" == attacker.char_type:
        n_golpes = 1 + attacker.ACC//32
        if attacker.clase in ["Monk", "Master"]:
            n_golpes *= 2
    else:
        n_golpes = attacker.Hits
    # n_golpes = 1 + attacker.ACC//32 if "pj" == attacker.char_type else attacker.Hits
    daño_total = 0
    for i in range(n_golpes):
        daño_total += one_hit_att_tar(attacker, target)
    target.up_or_down_HP(-daño_total)

    n_tabs = ""
    if attacker.char_type == "enemy":
        n_tabs = "\t" * 16

    print(n_tabs, f"El HP de {target.name} ha sido afectado en {-daño_total}. Ahora es {target.HP}")
    if not target.alive:
        print(f" "*50, f"{target.name} HA MUERTO.")

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

    n_tabs = ""
    if attacker.char_type == "enemy":
        n_tabs = "\t" * 16

    if acierta:
        # Genera un número aleatorio de punto flotante entre 0.8 y 1.2
        # valor_aleatorio = round(random.uniform(0.8, 1.2), 2)
        # valor_aleatorio = random.choice([0.80,0.85,0.90,0.95,1.00,1.05,1.10,1.15,1.20])
        valor_aleatorio = random.choice(range(80,121))/100
        if critico:
            print(n_tabs, f"Crit Damage: 2 * {daño_att} * {valor_aleatorio} - {defensa_tar} = {int(2 * daño_att * valor_aleatorio - defensa_tar)}")
            return int(max(2 * daño_att * valor_aleatorio - defensa_tar, 0))
        else:
            print(n_tabs, f"Norm Damage: {daño_att} * {valor_aleatorio} - {defensa_tar} = {int(daño_att * valor_aleatorio - defensa_tar)}")
            return int(max(daño_att * valor_aleatorio - defensa_tar, 0))
    else:
        print(n_tabs, "Miss Hit")
        return 0