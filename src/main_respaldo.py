from src.clases.personaje import *
from src.clases.pj import PJ
from src.clases.enemy import Enemy

max_wait = 400

per1 = Personaje("P1",25, 500, 44, 27, 28, 10, 38, 10)
# per2 = Personaje("P2",25, 300, 25, 26, 17, 5, 38, 12)
# ene1 = Personaje("COM_01",30, 356, 11, 7, 5, 9, 72, 8)
# ene2 = Personaje("COM_02",26, 420, 9, 6, 4, 7, 48, 11)
#
# pj_1 = PJ(1, 0, 35, 0, 20, 5, 1, 10, 5, 10, 15)
# pj_2 = PJ(1, 0, 30, 0, 5, 10, 5, 5, 15, 5, 15)
# pj_3 = PJ(1, 0, 33, 0, 33, 5, 5, 20, 5, 5, 10)
# pj_4 = PJ(1, 0, 30, 0, 10, 10, 10, 5, 5, 7, 20)
# pj_5 = PJ(1, 0, 28, 0, 5, 5, 15, 10, 5, 5, 20)
# pj_6 = PJ(1, 0, 25, 0, 1, 10, 20, 1, 10, 5, 20)

pj_1 = PJ('Warrior')
pj_2 = PJ('Warrior')
pj_3 = PJ('Thief')
pj_4 = PJ('Monk')




print(f"Enemies has appeared")
opc = -1
# pers = [per1, per2, ene1, ene2]

def siguientes_x_turnos(arr_char, n):
    turnos = []
    acum = []
    for i in range(len(arr_char)):
        acum.append(arr_char[i].espera)

    while len(turnos) < n:
        for j in range(len(arr_char)):
            acum[j] += arr_char[j].SPD
            if acum[j] >= max_wait:
                acum[j] -= max_wait
                turnos.append(arr_char[j])
                print(f"{arr_char[j].con}", end = ", ")
    print("...")
    return turnos

def proseguir_al_siguiente_turno(arr_char):
    while(True):
        for j in range(len(arr_char)):
            arr_char[j].espera += arr_char[j].SPD
            if arr_char[j].espera >= max_wait:
                arr_char[j].espera -= max_wait
                print(f"Personaje en turno {arr_char[j].con}")
                return arr_char[j]

def ataque_random_de_enemigo_a_jugador(ene_char, arr_char):
    jug_char = []
    for char in arr_char:
        if "COM" not in char.con:
            jug_char.append(char)
    # Seleccionar objetivo
    # if len(jug_char) == 1:
    #     daño = ene_char.obtener_daño_ataque_físico()
    #     per1.recibir_daño_ataque_físico(daño)
    n = len(jug_char)
    pos = random.randint(0, n - 1)
    daño = ene_char.obtener_daño_ataque_físico()
    jug_char[pos].recibir_daño_ataque_físico(daño)

def alive_chars(arr_char):
    personajes_vivos = []
    for char in arr_char:
        if char.alive:
            personajes_vivos.append(char)
    return personajes_vivos

# def dropear_enemigo_muerto(arr_char):
#     personajes_vivos = []
#     for char in arr_char:
#         if char.alive:
#             personajes_vivos.append(char)
#     arr_char = personajes_vivos

pasa_turno = True

while(True):
    if pasa_turno:
        personaje_en_turno = proseguir_al_siguiente_turno(pers)
        if "COM" in personaje_en_turno.con:
            # Ataque aleatorio de un enemigo a un jugador
            # print(f"Enemigo {personaje_en_turno.con} ha atacado.")
            ataque_random_de_enemigo_a_jugador(personaje_en_turno, pers)
            continue
    opc = input("[1: Atacar; 2: Magia; 3: Defender; 4: Mostrar; 5: Turnos]: ")
    if opc == "1":
        enemigos = []
        for p in pers:
            if "COM" in p.con:
                enemigos.append(p)
        while(True):
            try:
                opc = int(input(f"Ingresa un enemigo entre 1 y {len(enemigos)}: "))
                if 0 <= opc-1 <= len(enemigos):
                    daño = per1.obtener_daño_ataque_físico()
                    enemigos[opc-1].recibir_daño_ataque_físico(daño)
                    if not enemigos[opc-1].alive:
                        # dropear_enemigo_muerto(pers)
                        pers = alive_chars(pers)
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
        print(f"*" * 10)
        for p in pers:
            p.mostrar_datos()
        print(f"*" * 10)
    elif opc == "5":
        pasa_turno = False
        siguientes_x_turnos(pers, 8)
    else:
        print("Opcion invalida")