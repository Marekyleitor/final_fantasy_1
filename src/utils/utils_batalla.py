# utils_batalla.py
def validar_input_numero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Valor debe estar entre {minimo} y {maximo}")
        except ValueError:
            print("Valor inválido.")