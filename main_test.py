max = 64

def calcular_turnos(arr):
    acum = []
    for i in range(len(arr)):
        acum.append(0)
    ticks = 100
    for i in range(ticks):
        for j in range(len(acum)):
            acum[j] += arr[j]
            if acum[j] >= max:
                acum[j] -= max
                print(f"Turno de posición: {j}")

def siguientes_x_turnos(arr, n):
    turnos = []
    acum = []
    for i in range(len(arr)):
        acum.append(0)

    while len(turnos) < n:
        for j in range(len(acum)):
            acum[j] += arr[j]
            if acum[j] >= max:
                acum[j] -= max
                turnos.append(j)
                print(f"Turno de posición: {j}")


# arr = [2,3,5,7]
arr = [5,7,9,4]
# calcular_turnos(arr)
siguientes_x_turnos(arr, 8)

# print("Ejercicio 01")