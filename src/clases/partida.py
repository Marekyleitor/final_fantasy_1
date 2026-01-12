import pickle
from src.utils.constantes import VERDE, ROJO, AZUL, RESET

class Partida:
    def __init__(self, arrChar:object=None, location:str="", estado_de_juego:str="", inventory:dict={}, gil:int=0):
        # Inicializamos con los valores por defecto
        self.arrChar = arrChar # object
        self.location = location # ""  # String para la ubicación
        self.estado_de_juego = estado_de_juego # "" # String para la partida del juego
        self.inventory = inventory # {}  # Diccionario para inventory
        self.gil = gil # 0  # Entero para gil

    def guardar_partida(self, nombre_archivo):
        """Guarda la partida actual del juego"""
        try:
            with open("./saves/FF1-save " + nombre_archivo, 'wb') as archivo:
                pickle.dump(self.__dict__, archivo)
            print(f"Estado del juego guardado en {AZUL}saves/FF1-save {nombre_archivo}{RESET}")
        except Exception as e:
            print(f"Error al guardar la partida: {e}")

    @classmethod
    def cargar_partida(cls, nombre_archivo):
        """Carga un estado previo del juego"""
        try:
            with open("./saves/FF1-save " + nombre_archivo, 'rb') as archivo:
                datos = pickle.load(archivo)
                instancia = cls(**datos)  # Crea nueva instancia con los datos cargados
                # instancia.__dict__.update(datos)
                print(f"Partida {AZUL}FF1-save {nombre_archivo}{RESET} cargada exitosamente.")
                return instancia
        except FileNotFoundError:
            print("No se encontró el archivo de guardado")
            return None
        except Exception as e:
            print(f"Error al cargar la partida: {e}")
            return None