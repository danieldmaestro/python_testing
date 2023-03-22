class Game:
    def __init__(self):
        self.__row_1 = {'a1': None,
                        'a2': None,
                        'a3': None}
        self.__row_2 = {'b1': None,
                        'b2': None,
                        'b3': None}
        self.__row_3 = {'c1': None,
                        'c2': None,
                        'c3': None}
    @property
    def row_1(self):
        return self.__row_1
    
    @property
    def row_2(self):
        return self.__row_2
    
    @property
    def row_3(self):
        return self.__row_3
    
    def play(self, player_sign, cell):
        if "a" in cell:
            if self.row_1[cell] != None:
                self.row_1[cell] = player_sign
        elif "b" in cell:
            if self.row_2[cell] != None:
                self.row_2[cell]  = player_sign
        elif "c" in cell:
            if self.row_3[cell] != None:
                self.row_3[cell] = player_sign
        else:
            print("Enter valid cell identifier")
    
    def win_combo(self):
        for v in self.row_1.values():
