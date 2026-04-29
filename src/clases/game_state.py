import pickle
from src.utils.constantes import VERDE, ROJO, AZUL, RESET
from typing import Dict, Any, Optional
from src.clases.arrCharacter import ArrCharacter


class GameState:
    """
    Clase que encapsula el estado global del juego.
    Contiene toda la información necesaria para el juego: personajes, ubicación,
    estado actual, inventario y dinero.
    """

    def __init__(
        self,
        arr_char: Optional[ArrCharacter] = None,
        location: str = "Cornelia",
        estado_de_juego: str = "Mundo Abierto",
        inventory: Optional[Dict[str, Any]] = None,
        gil: int = 0
    ):
        """
        Inicializa el estado del juego.

        Args:
            arr_char: Instancia de ArrCharacter con los personajes del juego
            location: Ubicación actual (ej: "Cornelia", "Pravoka")
            estado_de_juego: Estado actual (ej: "Mundo Abierto", "Town", "Dungeon", "Batalla")
            inventory: Diccionario del inventario {item_name: cantidad}
            gil: Dinero del jugador
        """
        self.arr_char = arr_char
        self.location = location
        self.estado_de_juego = estado_de_juego
        self.inventory = inventory or {}
        self.gil = gil

    def __repr__(self):
        return (
            f"GameState(location='{self.location}', "
            f"estado='{self.estado_de_juego}', "
            f"gil={self.gil}, "
            f"inventory_items={len(self.inventory)})"
        )

    def __str__(self):
        return self.__repr__()

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