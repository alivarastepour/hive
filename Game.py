class Game:
    def __init__(self):
        self.__selectedHexagon = ''  # determines which hexagon is selected
        self.__selectedPiece = ''  # determines which piece is selected
        self.__turn = ''  # determines whose turn is it
        self.error = ''  # determines whether there is an error or not
