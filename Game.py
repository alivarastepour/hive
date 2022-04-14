def createBoard():  # inits the game's board
    board = []
    for a in range(22):
        temp = []
        for b in range(22):
            temp.append([])
        board.append(temp)
    return board


def getNeighbors(x, y):  # returns neighbors of a house
    return [(x - 1 if y % 2 == 1 else x, y - 1), (x - 1 if y % 2 == 1 else x - 1, y),
            (x - 1 if y % 2 == 1 else x, y + 1), (x + 1 if y % 2 == 0 else x, y - 1),
            (x + 1 if y % 2 == 0 else x + 1, y), (x + 1 if y % 2 == 0 else x, y + 1)]


class Game:
    def __init__(self):
        self.selectedHexagon = ''  # determines which hexagon is selected
        self.selectedPiece = ''  # determines which piece is selected
        self.turn = 2  # determines whose turn is it
        self.error = ''  # determines whether there is an error or not
        self.board = createBoard()  # keeps track of game's board
        self.isFirstMove = True  # determines whether this is the first move
        self.occupiedHomes = dict()  # keeps track of occupied homes

    # def getBoundary(self):
    #     minX, maxX, minY, maxY = 21, 0, 21, 0
    #     for home in self.occupiedHomes:
    #         user, piece, x, y = home
    #         if x > maxX:
    #             maxX = x
    #         if x < minX:
    #             minX = x
    #         if y > maxY:
    #             maxY = y
    #         if y < minY:
    #             minY = y
    #     return (minX, maxX), (minY, maxY)

    def availablePositions(self):  # calculates available positions for a user
        arr = []
        for (x, y) in self.occupiedHomes.keys():
            arr.extend(getNeighbors(x, y))
            duplicates = self.occupiedHomes.keys()
            invalid = []
            for a in arr:
                if a in duplicates:
                    invalid.append(a)
            arr = list(filter(lambda b: b not in invalid, arr))
            if not self.isFirstMove:
                invalid.clear()
                for h in arr:
                    nei = getNeighbors(h[0], h[1])
                    for n in nei:
                        try:
                            player = self.occupiedHomes.get(n, None)[0]
                        except TypeError:
                            continue
                        if player is not None and player != self.turn:
                            invalid.append(h)
                arr = list(filter(lambda b: b not in invalid, arr))
        return arr

    def fillHome(self, user, piece, x, y):  # updates a home state with new piece
        self.occupiedHomes.update({(x, y): (user, piece)})
        if self.isFirstMove:
            self.isFirstMove = False
