# formation_utils.py

from typing import List, Dict, Optional
import random
# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.utils.constantes import FORMACION

def get_formation(location: str) -> List[int]:
    """
    Obtiene los números de formación para una ubicación específica.

    Args:
        location: Nombre de la ubicación (ej: "Pravoka")

    Returns:
        Lista de números de formación que aparecen en esa ubicación
    """
    return [
        int(numero) for numero, datos in FORMACION.items()
        if location in datos['Location']
    ]

def get_enemies_from_formation(formation_number: int) -> List[str]:
    """
    Obtiene la lista de enemigos para un número de formación específico.

    Args:
        formation_number: Número de la formación

    Returns:
        Lista de cadenas con los enemigos en formato "Nombre xM-N"
    """
    return FORMACION.get(str(formation_number), {}).get('Enemies', [])

def get_enemies_how_many_and_which(enemies: List[str]) -> List[str]:
    """
    Determina la cantidad real de enemigos basándose en los rangos.

    Args:
        enemies: Lista de enemigos en formato "Nombre xM-N"

    Returns:
        Lista con la cantidad real de enemigos
    """
    result = []
    for enemy in enemies:
        name, range_str = enemy.split(' x')
        if '-' in range_str:
            min_val, max_val = map(int, range_str.split('-'))
            count = random.randint(min_val, max_val)
            result.extend([name] * count)
        else:
            result.append(name)
    return result

## Southern Cornelia region -> [0]
## Cornelia-Cornelia Bridge-Earthgift Shrine region -> [0, 3, 6, 128, 130]

# form_ids = get_formation("Cornelia-Cornelia Bridge-Earthgift Shrine region")
# print(f"form_ids: {form_ids}")
# enemies_by_formation = get_enemies_from_formation(2)
# print(f"enemies_by_formation: {enemies_by_formation}")
# enemies_array_str = get_enemies_how_many_and_which(enemies_by_formation)
# print(f"enemies_array_str: {enemies_array_str}")