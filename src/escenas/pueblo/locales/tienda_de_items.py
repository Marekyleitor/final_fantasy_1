from src.utils.constantes import ITEMS
from src.utils.constantes import VERDE, ROJO, AZUL, RESET


def tienda_de_items(arrChar, location, estado_de_juego, inventory, gil):
    while True:
        print("\n=== Tienda de Items ===")
        print("1. Comprar")
        print("2. Vender")
        print("3. Dónde encontrar cada elemento")
        print("Q. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ## Comprar
            arrChar, location, estado_de_juego, inventory, gil = comprar(arrChar, location, estado_de_juego, inventory, gil)
        elif opcion == "2":
            ## Vender
            # arrChar, location, estado_de_juego, inventory, gil = vender(arrChar, location, estado_de_juego, inventory, gil)
            pass
        elif opcion == "3":
            ## Dónde encontrar cada elemento
            donde_encontrar_cada_elemento()
        elif opcion.upper() == "Q":
            ## Salir
            return arrChar, location, estado_de_juego, inventory, gil

def comprar(arrChar, location, estado_de_juego, inventory, gil):
    # item será un diccionario: 'Potion': {'type': 'Usable', 'subtype': 'Healing', 'price': 40, ... }
    items_for_sale = {}
    for item_name, item_data in ITEMS.items():
        # item_name: Es el key. Ejm: "Potion", "Ether", etc.
        # item_data: Es el value, que es otro diccionario. Ejm: {'type': 'Usable', 'subtype': 'Healing', 'price': 40, ...
        # Validamos que exista el diccionario interno
        if isinstance(item_data, dict):
            # Obtenemos las ciudades permitidas
            cities = item_data.get("buy", "")
            # Verificamos si está disponible
            # print(f"{item_name}: {item_data.get("buy")}")  # El texto de "buy"
            if item_data.get("buy") == ["All shops"] or location in cities:
                items_for_sale[item_name] = item_data

    while True:
        # Mostrar los items a la venta y su precio correctamente espaciado
        print(f"\n\t\t{'Items_for_sale':<20}Precio")
        for item_name, item_data in items_for_sale.items():
            # print(f"- {item}")
            print(f"\t\t- {item_name:<18}{item_data["price"]:>6}")
        print()
        # Pide escribir el item que desea comprar
        item_a_comprar = input("Escriba el nombre del elemento a comprar (q: Salir): ")
        if item_a_comprar.upper() == "Q":
            break
        elif item_a_comprar in items_for_sale: # Si el elemento escrito está a la venta
            # Muestra las opciones
            print("1. Escribir cantidad a comprar")
            print("2. Comprar hasta 99")
            print("3. Comprar hasta lo que te permita tu dinero")
            print("Q. Salir")
            # Pide elegir opciones
            while True:
                opcion_de_compra = input("Escriba la opción de compra (q: Salir): ")
                if opcion_de_compra.upper() == "Q":
                    break
                elif opcion_de_compra == "1":

                    while True:
                        cantidad = input("Ingrese cantidad a comprar (q: Salir): ")
                        if cantidad.upper() == "Q":
                            break
                        try:
                            cantidad = int(cantidad)
                            # Valida si se puede comprar por precio
                            if ITEMS[item_a_comprar]["price"] * cantidad <= gil:
                                # Muestra la futura compra y el precio total
                                print(f"\nTratas de comprar {VERDE}Potion{RESET} ({ITEMS[item_a_comprar]["price"]} gil) x{cantidad} = {ROJO}{ITEMS[item_a_comprar]["price"]*cantidad}{RESET} gil")
                                print(f"Tu dinero: {gil} gil - {ROJO}{ITEMS[item_a_comprar]["price"]*cantidad}{RESET} gil = {AZUL}{gil-ITEMS[item_a_comprar]["price"]*cantidad}{RESET} gil")
                                # Pregunta si en realidad quiere comprar
                                if input("¿Aceptas la compra? (S/N): ").upper() == 'S':
                                    # Obtengo el o los elementos
                                    if item_a_comprar in inventory:
                                        inventory[item_a_comprar] += cantidad
                                    else:
                                        inventory[item_a_comprar] = cantidad
                                    # Se descuenta de mi gil
                                    gil -= ITEMS[item_a_comprar]["price"] * cantidad
                                # else:
                                #     break
                            else:
                                print(f"No tienes suficiente dinero. Gil: {AZUL}{gil}{RESET}. Costo Total: {ROJO}{ITEMS[item_a_comprar]["price"]*cantidad}{RESET}.")

                        except ValueError:
                            print("Valor inválido.")

                    break
                elif opcion_de_compra == "2":
                    break
                elif opcion_de_compra == "3":
                    break
                else:
                    continue
            pass


    return arrChar, location, estado_de_juego, inventory, gil

def vender(arrChar, location, estado_de_juego, inventory, gil):

    return arrChar, location, estado_de_juego, inventory, gil

def donde_encontrar_cada_elemento():
    for item_name, item_data in ITEMS.items():
        if isinstance(item_data, dict):
            # Vemos cada item y sus locales de venta
            print(f"\t* {item_name:<20}{item_data.get("buy")}")  # El texto de "buy"