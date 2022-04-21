from neighborhoodUtil import *


def createBoard():  # inits the game's board
    board = []
    for a in range(22):
        temp = []
        for b in range(22):
            temp.append([])
        board.append(temp)
    return board


def getGraphBoundaries(graph):
    minX, maxX, minY, maxY = 22, 0, 22, 0
    for vertex in graph:
        x, y = vertex
        if x > maxX:
            maxX = x
        if x < minX:
            minX = x
        if y > maxY:
            maxY = y
        if y < minY:
            minY = y
    return (minX, maxX), (minY, maxY)


class Game:
    def __init__(self):
        self.selectedHexagon = ''  # determines which hexagon is selected
        self.selectedPiece = ''  # determines which piece is selected
        self.turn = 1  # determines whose turn is it
        self.error = ''  # determines whether there is an error or not
        self.board = createBoard()  # keeps track of game's board
        self.isFirstMove = True  # determines whether this is the first move
        self.isSecondMove = False  # determines whether this is the second move
        self.occupiedHomes = dict()  # keeps track of occupied homes

    def availablePositions(self):  # calculates available positions for a user
        if self.isFirstMove:
            self.isFirstMove = False
            self.isSecondMove = True
            return [(11, 11)]
        if self.isSecondMove:
            self.isSecondMove = False
            return getNeighbors(11, 11)
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
        return list(set(arr))

    def fillHome(self, user, piece, x, y):  # updates a home state with new piece
        self.occupiedHomes.update({(x, y): (user, piece)})
        print({(x, y): (user, piece)})
        if self.isFirstMove:
            self.isFirstMove = False

    def changeHome(self, x, y, prevX, prevY):
        self.occupiedHomes.update({(x, y): self.occupiedHomes.pop((prevX, prevY))})

    def isHomeSurrounded(self, x, y):
        neighbors = getNeighbors(x, y)
        count = 0
        for neighbor in neighbors:
            if neighbor in self.occupiedHomes.keys():
                count += 1
        return count == 6

    def canMove(self):  # returns true if the selected piece can move (graph connectivity check)
        g1 = list(self.occupiedHomes.keys()).copy()
        g1.remove(self.selectedHexagon)
        return self.checkConnectivity(g1)

    def canPut(self, x, y):  # returns true if the selected piece can move to a specific position (graph
        # connectivity check)
        g1 = list(self.occupiedHomes.keys()).copy()
        g1.remove(self.selectedHexagon)
        g1.append((x, y))
        return self.checkConnectivity(g1)

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

    def queenValidMoves(self, x, y):  # returns all valid positions for a queen
        validHomes = []
        neighbors = getNeighbors(x, y)
        for neighbor in neighbors:
            if neighbor not in self.occupiedHomes.keys() and not self.isHomeSurrounded(*neighbor):
                validHomes.append(neighbor)
        return validHomes

    def antValidMoves(self, x, y):  # returns all valid positions for an ant
        possibleHomes = list(filter(lambda a: a != (x, y), self.availablePositions()))
        validHomes = []
        for home in possibleHomes:
            g1 = list(self.occupiedHomes.keys()).copy()
            g1.remove((x, y))
            g1.append(home)
            f1 = self.checkConnectivity(g1)
            if f1:
                validHomes.append(home)
        return validHomes

    def beetleValidMoves(self, x, y):  # returns all valid positions for a beetle
        neighbors = getNeighbors(x, y)
        availablePositions = self.availablePositions()
        validHomes = [
            home for home in neighbors
            if (home in availablePositions or home in self.occupiedHomes.keys()) and not self.isHomeSurrounded(*home)
        ]
        valid = []
        for home in validHomes:
            g1 = list(self.occupiedHomes.keys()).copy()
            g1.remove((x, y))
            g1.append(home)
            f1 = self.checkConnectivity(g1)
            if f1:
                valid.append(home)
        return valid

    def spiderValidMoves(self, x, y):
        validHomes, possibleHomes = [], []
        neighbors = getNeighbors(x, y)
        f1 = False
        for firstLevelNeighbor in neighbors:
            if not self.canPut(*firstLevelNeighbor) or firstLevelNeighbor in self.occupiedHomes.keys():
                continue
            for secondLevelNeighbor in getNeighbors(*firstLevelNeighbor):
                if f1:
                    f1 = False
                    continue
                if not self.canPut(*secondLevelNeighbor) or secondLevelNeighbor in self.occupiedHomes.keys():
                    continue
                for thirdLevelNeighbor in getNeighbors(*secondLevelNeighbor):
                    if firstLevelNeighbor == thirdLevelNeighbor or thirdLevelNeighbor in self.occupiedHomes or \
                            thirdLevelNeighbor in validHomes or thirdLevelNeighbor not in self.availablePositions() or \
                            not self.canPut(*thirdLevelNeighbor):
                        f1 = True
                        continue
                    validHomes.append((thirdLevelNeighbor[0], thirdLevelNeighbor[1]))
        return validHomes

    def findPath(self, graph, v1, v2, visited):
        if v1 == v2:
            return True
        neighbors = list(filter(lambda v: v in graph, getNeighbors(*v1)))
        if v2 in neighbors:
            return True
        elif len(neighbors) != 0:
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                visited.append(v1)
                res = self.findPath(graph, neighbor, v2, visited)
                if res:
                    return True
        return False

    def checkConnectivity(self, graph):
        for v1 in graph:
            for v2 in graph:
                pathExists = self.findPath(graph, v1, v2, [])
                if not pathExists:
                    return False
        return True
