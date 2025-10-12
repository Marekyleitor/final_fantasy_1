class ArrCharacter:
    def __init__(self):
        self.n = 0
        self.arr = []

    def addChar(self, char):
        self.n += 1
        self.arr.append(char)

    def addArrChar(self, ArrChar):
        self.n = len(ArrChar)
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
        cant_XP_One = cant // len(auxArrAlive)
        for per in auxArrAlive:
            per.subirXP(cant_XP_One, False)

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