def createBoard():
    board = []
    for a in range(22):
        temp = []
        for b in range(22):
            temp.append([])
        board.append(temp)
    print(board)
    return board


class Game:
    def __init__(self):
        self.__selectedHexagon = ''  # determines which hexagon is selected
        self.selectedPiece = ''  # determines which piece is selected
        self.turn = ''  # determines whose turn is it
        self.error = ''  # determines whether there is an error or not
        self.board = createBoard()  # keeps track of game's board
