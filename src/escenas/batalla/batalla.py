# src/escenas/batalla/batalla.py
from .acciones.ataque import ejecutar_ataque
from .acciones.magia import ejecutar_magia
from .acciones.defender import ejecutar_defensa
from .acciones.mostrar import mostrar_estado
from src.clases.pj import PJ
from src.clases.enemy import Enemy
from src.clases.arrCharacter import ArrCharacter
from src.utils.utils_formation import *
from src.escenas.menu_de_la_party.opciones.inventario import inventario_en_batalla
from ...clases.arma import Arma
from ...clases.armadura import Armadura
from ...utils.constantes import ITEMS, ARMAS, ARMADURAS, VERDE, RESET

max_wait = 400

# def batalla(arrChar, location, estado_de_juego, inventory, gil):
def batalla(partida):
    partida.estado_de_juego = "Batalla"
    # 3. Encuentro con enemigos
    ## 3.1. Crear arreglo de enemigos
    form_ids = get_formation(partida.location)
    print(f"form_ids: {form_ids}")

    if form_ids == []:
        print("\tNO HAY ENCUENTROS CON ENEMIGOS AQUÍ.")
        # return arrChar.arrPer(), location, estado_de_juego, inventory, gil
        return partida

    random_choice = random.choice(form_ids)
    # random_choice = 123 # Chaos
    # random_choice = 115 # Lich
    # random_choice = 256 # Echidna
    # random_choice = 68 # Sea Scorpion x1-6, Sea Snake x2-5, Sea Troll x2
    # random_choice = 147 # Ogre Chief x1-4, Ogre x0-2
    # random_choice = 127 # Garland x1 (Longsword (2%))
    # random_choice = 126 # Pirate x9 (Leather Shield (2%))
    # random_choice = 164 # Test libre
    print(f"random_choice: {random_choice}")
    enemies_by_formation = get_enemies_from_formation(random_choice)
    print(f"enemies_by_formation: {enemies_by_formation}")
    enemies_array_str = get_enemies_how_many_and_which(enemies_by_formation)
    print(f"enemies_array_str: {enemies_array_str}")
    enemies_array = []
    for enemy in enemies_array_str:
        enemies_array.append(Enemy(enemy))


    ## 3.2. Y pasárselo a partida.arrChar
    partida.arrChar.addArrChar(enemies_array)
    partida.arrChar.update_enemy_names()
    print(f"Characters in partida.arrChar.n: {partida.arrChar.n}")
    # Mostrar tipo de enemigo y su nombre (ej.: "Goblin 2") de todos los enemigos en partida.arrChar
    for enemy in partida.arrChar.arrEne().arr:
        enemy.mostrar_datos_4()

    agregar_espera_aleatoria(partida.arrChar)
    pasar_turno = True

    while (True):
        # Validar la victoria, todos los enemigos muertos y al menos 1 pj vivo
        if partida.arrChar.arrEne().arrAlive().arr == [] and partida.arrChar.arrPer().arrAlive().arr != []:
            # Reiniciar espera aleatoria
            reiniciar_espera_aleatoria(partida.arrChar)
            # Obtención de XP, Gil y dropeo enemigo
            # arrChar, estado_de_juego, inventory, gil = ganancia_por_victoria(arrChar, estado_de_juego, inventory, gil)
            partida = ganancia_por_victoria(partida)
            # Aquí "partida.arrChar" ya solo posee los PJs
            # Devolver valores
            # return arrChar.arrPer(), location, estado_de_juego, inventory, gil
            return partida
        # Validar la derrota, si todos los pj están muertos
        if partida.arrChar.arrPer().arrAlive().arr == []:
            print(f"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁
    ⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀
    ⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀
    ⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀
    ⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀
    ⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀
    ⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆
    ⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀
    ⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀
    ⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀
    ⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀
    ⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
            #         print(f"""  ____    _    __  __ _____    _____     _______ ____
            #  / ___|  / \  |  \/  | ____|  / _ \ \   / / ____|  _ \
            # | |  _  / _ \ | |\/| |  _|   | | | \ \ / /|  _| | |_) |
            # | |_| |/ ___ \| |  | | |___  | |_| |\ V / | |___|  _ <
            #  \____/_/   \_\_|  |_|_____|  \___/  \_/  |_____|_| \_\ """)
            break
        if pasar_turno:
            char_en_turno = proseguir_al_siguiente_turno(partida.arrChar)
            print(f"")

            n_tabs = ""
            if char_en_turno.char_type == "enemy":
                n_tabs = "\t" * 16

            print(n_tabs, f"*" * 10, f"Turno de {char_en_turno.name}", f"*" * 10)
            if "enemy" == char_en_turno.char_type:
                # Ataque aleatorio de un enemigo a un jugador
                # print(f"Enemigo {char_en_turno.char_type} ha atacado.")
                # ataque_random_de_enemigo_a_jugador(char_en_turno, pers)
                ejecutar_turno_de_enemigo(char_en_turno, partida.arrChar)
                continue

        opc = input(f"Turno de {VERDE}{char_en_turno.name}{RESET}\n[1: Atacar; 2: Magia; 3: Defender; 4: Mostrar; 5: Turnos; 6: Huir; 7: Inventario]: ")
        if opc == "1":
            ## Atacar
            enemies_alive = partida.arrChar.arrEne().arrAlive()
            pasar_turno = ejecutar_ataque(char_en_turno, enemies_alive)

            # enemies_alive = partida.arrChar.arrEne().arrAlive()
            # while(True):
            #     try:
            #         text = input(f"Ingresa un enemigo entre 1 y {enemies_alive.get_n()}: ")
            #         if text.upper() == "Q":
            #             pasar_turno = False # no es necesario, xq ya está en falso supuestamente.
            #             print(f"Atacar cancelado.")
            #             break
            #         index = int(text)
            #         if 0 <= index-1 < enemies_alive.get_n():
            #             ataque_att_tar(char_en_turno, enemies_alive.get_char(index-1))
            #             pasar_turno = True
            #             break
            #     except ValueError:
            #         print("Valor inválido.")


        elif opc == "2":
            ## Magia
            pasar_turno = False
        elif opc == "3":
            ## Defender
            pasar_turno = False
        elif opc == "4":
            ## Mostrar
            pasar_turno = False

            # print(f"*" * 10)
            # for p in partida.arrChar.arr:
            #     p.mostrar_datos()
            # print(f"*" * 10)

            while (True):
                try:
                    num = int(input(f"[1: Extremo detalle; 2: Detalle medio; 3: Básico; 4: Extra]: "))
                    if 1 <= num <= 4:
                        print(f"*" * 10)
                        if num == 1:
                            for p in partida.arrChar.arr:
                                p.mostrar_datos()
                        elif num == 2:
                            for p in partida.arrChar.arr:
                                p.mostrar_datos_2()
                        elif num == 3:
                            for p in partida.arrChar.arr:
                                p.mostrar_datos_3()
                        elif num == 4:
                            for p in partida.arrChar.arr:
                                p.mostrar_datos_4()
                        print(f"*" * 10)
                        break
                    else:
                        print("Valor inválido. Salida 1.")
                except ValueError:
                    print("Valor inválido. Salida 2.")

        elif opc == "5":
            ## Turnos
            pasar_turno = False
            siguientes_x_turnos(partida.arrChar, 8)
        elif opc == "6":
            ## Huir
            # return arrChar.arrPer(), location, estado_de_juego, inventory, gil
            partida.arrChar = partida.arrChar.arrPer()
            return partida
        elif opc == "7":
            ## Inventario
            partida, pasar_turno = inventario_en_batalla(partida, char_en_turno)
            print(f"pasar_turno en batalla: {pasar_turno}")
            ## Ejemplo
            # enemies_alive = partida.arrChar.arrEne().arrAlive()
            # pasar_turno = ejecutar_ataque(char_en_turno, enemies_alive)

            # pass
        else:
            pasar_turno = False
            print("Opcion inválida")

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

def one_hit_att_tar(attacker, target):   # Está en ataque.py, pero no puedo quitarlo, otra func lo usa
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

def ataque_att_tar(attacker, target):   # Está en ataque.py, pero no puedo quitarlo, otra func lo usa
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

def agregar_espera_aleatoria(arr_char):
    for char in arr_char.arr:
        char.espera = random.randint(0, max_wait)

def reiniciar_espera_aleatoria(arr_char):
    for char in arr_char.arr:
        char.espera = 0

# def ganancia_por_victoria(arrChar, estado_de_juego, inventory, gil):
def ganancia_por_victoria(partida):
    party = partida.arrChar.arrPer()            # PJs vivos y muertos
    dead_enemies = partida.arrChar.arrEne()
    XP = 0
    gil_gained = 0
    dropped_entities = []                  # Is a list "[]"
    for enemy in dead_enemies.arr:
        XP += enemy.XP
        gil_gained += enemy.gil
        dropped_entities = enemy_drop_entities(enemy, dropped_entities)
    # Muestra lo que se obtuvo
    print("\t"*10, f"***** Obtención de Loot y XP *****")
    print("\t"*10, f"XP: {XP}")
    print("\t"*10, f"gil: {gil_gained}")
    # print("\t"*10, f"dropped entities: {dropped_entities}")
    print("\t"*10, f"dropped entities:")
    for entity in dropped_entities:
        # Si entity name tiene '\x1b'. Ejm: '\x1b[92mLongsword | Superior | 1.15\x1b[0m'
        print("\t" * 10, f"- {entity}")
    print("\t"*10, f"**********************************")
    # Repartición de XP
    party.subirXP_gru(XP)
    # Entrega de gil
    partida.gil += gil_gained
    # Dropeo enemigo
    ## Agregar dropped_entities a mi partida.inventory (diccionario)
    partida.inventory = add_entities_dropped_to_my_inventory(partida.inventory, dropped_entities)
    # Tal vez cambiar el estado de juego
    # return arrChar.arrPer(), estado_de_juego, inventory, gil
    partida.arrChar = party
    return partida

def enemy_drop_entities(enemy, dropped_entities):
    """
    Función individual, en la que se calcula si un enemigo dropea o no un entity, arma o armadura.

    Args:
    enemy: Objeto Enemy.
    dropped_entities: Lista de los entities dropeados hasta el momento.

    Returns:
    dropped_entities: Se agregue o no un nuevo objeto entity, arma o armadura a la lista, esta se devuelve.
    """
    text_drop = enemy.drop
    if text_drop == "-":
        return dropped_entities
    arr = text_drop.split(', ')
    for entity_porc in arr:
        entity, porc = entity_porc.split(' (')
        porc = int(porc.replace('%)', ''))
        n = random.randint(0,100)
        if n < porc:
            # Determino que tipo de entidad es (Entity, Arma o Armadura)
            if entity in ARMAS:
                arma_name = entity
                arma_01 = Arma(arma_name)
                dropped_entities.append(arma_01.decored_name)
            elif entity in ARMADURAS:
                armadura_name = entity
                armadura_01 = Armadura(armadura_name)
                dropped_entities.append(armadura_01.decored_name)
            elif entity in ITEMS:
                dropped_entities.append(entity)
            else:
                dropped_entities.append(entity)
    return dropped_entities

def add_entities_dropped_to_my_inventory(partida_inventory: dict, dropped_entities: list):
    for text_entity in dropped_entities:
        # Validar si el item es un arma
        if text_entity in ARMAS:
            # Si es un arma, generamos el objeto y obtenemos su self.decored_name
            text_entity = Arma(text_entity).decored_name
        # Validar si el item es una armadura
        elif text_entity in ARMADURAS:
            # Si es una armadura, generamos el objeto y obtenemos su self.decored_name
            text_entity = Armadura(text_entity).decored_name
        # La entidad, sea item, arma o armadura se guarda como texto en el partida_inventory
        if text_entity in partida_inventory:
            partida_inventory[text_entity] += 1
        else:
            partida_inventory[text_entity] = 1
    return partida_inventory

# def dropear_enemigo_muerto(arr_char):
#     personajes_vivos = []
#     for char in arr_char:
#         if char.alive:
#             personajes_vivos.append(char)
#     arr_char = personajes_vivos






# # src/escenas/batalla/batalla.py
# from .acciones.ataque import ejecutar_ataque
# from .acciones.magia import ejecutar_magia
# from .acciones.defender import ejecutar_defensa
# from .acciones.mostrar import mostrar_estado
#
#
# def gestionar_turno(pj, enemigos):
#     while True:
#         opcion = input("[1: Atacar; 2: Magia; 3: Defender; 4: Mostrar]: ")
#
#         if opcion == "1":
#             ejecutar_ataque(pj, enemigos)
#         elif opcion == "2":
#             ejecutar_magia(pj, enemigos)
#         elif opcion == "3":
#             ejecutar_defensa(pj)
#         elif opcion == "4":
#             mostrar_estado(pj, enemigos)