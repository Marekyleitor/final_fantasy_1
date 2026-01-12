class ArrCharacter:
    def __init__(self):
        self.n = 0
        self.arr = []

    def addChar(self, char):
        self.n += 1
        self.arr.append(char)

    def addArrChar(self, ArrChar):
        self.n += len(ArrChar)
        for char in ArrChar:
            self.arr.append(char)

    def mostrar_datos_todo(self):
        for char in self.arr:
            char.mostrar_datos()

    # def mostrarTodo2(self):
    #     for char in self.arr:
    #         char.mostrar2()

    def arrAlive(self):
        aux = []
        for per in self.arr:
            if per.alive:
                aux.append(per)
        arr_char = ArrCharacter()
        arr_char.addArrChar(aux)
        return arr_char

    def subirXP_gru(self, cant):
        auxArrAlive = self.arrAlive()
        cant_XP_One = cant // auxArrAlive.n
        for per in auxArrAlive.arr:
            per.subirXP(cant_XP_One, True)

    def arrPer(self):
        aux = []
        for char in self.arr:
            if char.char_type == "pj":
                aux.append(char)
        arr_char = ArrCharacter()
        arr_char.addArrChar(aux)
        return arr_char

    def arrEne(self):
        aux = []
        for char in self.arr:
            if char.char_type == "enemy":
                aux.append(char)
        arr_char = ArrCharacter()
        arr_char.addArrChar(aux)
        return arr_char

    def get_n(self):
        return self.n

    def get_char(self, index):
        return self.arr[index]

    def update_enemy_names(self):
        """
        Actualiza los IDs y nombres de todos los enemigos en la lista.
        """
        arr_char = ArrCharacter()
        arr_char.addArrChar(self.arr)  #
        enemies_arrChar = arr_char.arrEne()
        # Agrupar enemigos por tipo
        enemies_by_type = {}
        for enemy in enemies_arrChar.arr:
            if enemy.enemy_type not in enemies_by_type:
                enemies_by_type[enemy.enemy_type] = []
            enemies_by_type[enemy.enemy_type].append(enemy)

        # Actualizar IDs y nombres
        for enemy_type, enemy_group in enemies_by_type.items():
            sorted_enemies = sorted(enemy_group, key=lambda x: x.n_id)
            for index, enemy in enumerate(sorted_enemies, 1):
                enemy.n_id = index
                enemy.name = f"{enemy.enemy_type} {enemy.n_id}"

        # return enemies_arrChar.arr