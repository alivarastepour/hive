class Game:
    def __init__(self):
        self.__selectedHexagon = ''  # determines which hexagon is selected
        self.selectedPiece = ''  # determines which piece is selected
        self.turn = ''  # determines whose turn is it
        self.error = ''  # determines whether there is an error or not

    @property
    def selectedHexagon(self):
        return self.__selectedHexagon

    @selectedHexagon.setter
    def selectedHexagon(self, val):
        print(val)
        self.__selectedHexagon = val