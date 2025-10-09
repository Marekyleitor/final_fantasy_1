from src.clases.personaje import *
from src.clases.pj import PJ
from src.clases.enemy import Enemy
from src.clases.arrCharacter import ArrCharacter

max_wait = 400

pj_1 = PJ('Warrior', 'Escanor')
pj_2 = PJ('Warrior', 'Arturo')
pj_3 = PJ('Thief', 'Robin Hood')
pj_4 = PJ('Monk', 'Monje')

ene_1 = Enemy('Crazy Horse')
ene_2 = Enemy('Black Widow')

char_lst = [pj_1,pj_2,pj_3,pj_4,ene_1,ene_2]
arrChar = ArrCharacter()
arrChar.addArrChar(char_lst)    # <- objeto ArrCharacter
party = arrChar.arrPer()        # <- lista
enemies = arrChar.arrEne()      # <- lista

def siguientes_x_turnos(arr_char, n):
    turnos = []
    acum = []
    for i in range(arr_char.get_n()):
        acum.append(arr_char.get_char(i).espera)

    while len(turnos) < n:
        for j in range(arr_char.get_n()):
            acum[j] += arr_char.get_char(j).AGL
            if acum[j] >= max_wait:
                acum[j] -= max_wait
                turnos.append(arr_char.get_char(j))
                print(f"{arr_char.get_char(j).name}", end = ", ")
    print("...")
    return turnos

siguientes_x_turnos(arrChar, 8)
