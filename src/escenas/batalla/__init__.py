# # src/batalla/__init__.py
# from .batalla import gestionar_turno
# from .acciones.ataque import ejecutar_ataque
# from .acciones.magia import ejecutar_magia
# from .acciones.defender import ejecutar_defensa
# from .acciones.mostrar import mostrar_estado
#
# # src/batalla/batalla.py
# from src.utils.utils_batalla import validar_input_numero
#
#
# def gestionar_turno(char_en_turno, enemies_alive):
#     while True:
#         opcion = input("[1: Atacar; 2: Magia; 3: Defender; 4: Mostrar; 5: Turnos]: ")
#
#         if opcion == "1":
#             if ejecutar_ataque(char_en_turno, enemies_alive):
#                 break
#         elif opcion == "2":
#             ejecutar_magia(char_en_turno, enemies_alive)
#             break
#         elif opcion == "3":
#             ejecutar_defensa(char_en_turno)
#             break
#         elif opcion == "4":
#             mostrar_estado(char_en_turno, enemies_alive)
#         elif opcion == "5":
#             break
#
#
# # src/batalla/acciones/ataque.py
# from ...utils.utilidades_batalla import validar_input_numero
#
#
# def ejecutar_ataque(char_en_turno, enemies_alive):
#     try:
#         index = validar_input_numero(
#             f"Ingresa un enemigo entre 1 y {enemies_alive.get_n()}: ",
#             1,
#             enemies_alive.get_n()
#         )
#         ataque_att_tar(char_en_turno, enemies_alive.get_char(index - 1))
#         return True
#     except ValueError:
#         print("Valor inválido.")
#         return False