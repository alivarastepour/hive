from neighborhoodUtil import *


def createBoard():  # inits the game's board
    board = []
    for a in range(22):
        temp = []
        for b in range(22):
            temp.append([])
        board.append(temp)
    return board


class Game:
    def __init__(self):
        self.selectedHexagon = ''  # determines which hexagon is selected
        self.selectedPiece = ''  # determines which piece is selected
        self.turn = 2  # determines whose turn is it
        self.error = ''  # determines whether there is an error or not
        self.board = createBoard()  # keeps track of game's board
        self.isFirstMove = True  # determines whether this is the first move
        self.occupiedHomes = dict()  # keeps track of occupied homes

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

    def isHomeSurrounded(self, x, y):
        neighbors = getNeighbors(x, y)
        count = 0
        for neighbor in neighbors:
            if neighbor in self.occupiedHomes.keys():
                count += 1
        return count == 6

    def grasshopperValidMoves(self, x, y):  # returns all valid positions for a grasshopper
        validHomes = []
        if (x, y) not in self.occupiedHomes.keys():
            self.error = 'this home does not contain a grasshopper'
            return
        neighbors = getNeighborsWithDirection(x, y)
        for neighbor in neighbors:
            direction, x, y = neighbor
            if not (x, y) in self.occupiedHomes.keys():
                continue
            while True:
                possibleHome = getCoordinates(x, y, direction)
                if possibleHome not in self.occupiedHomes.keys():
                    validHomes.append(possibleHome)
                    break
                x, y = getCoordinates(x, y, direction)
        return validHomes

    def queenValidMoves(self, x, y):
        validHomes = []
        neighbors = getNeighbors(x, y)
        for neighbor in neighbors:
            if neighbor not in self.occupiedHomes.keys() and not self.isHomeSurrounded(*neighbor):
                validHomes.append(neighbor)
        return validHomes
