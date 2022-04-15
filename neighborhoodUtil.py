def getNW(x, y):  # returns the north-west neighbor of a home
    return x - 1 if y % 2 == 1 else x, y - 1


def getN(x, y):  # returns the north neighbor of a home
    return x - 1 if y % 2 == 1 else x - 1, y


def getNE(x, y):  # returns the north-east neighbor of a home
    return x - 1 if y % 2 == 1 else x, y + 1


def getSW(x, y):  # returns the south-west neighbor of a home
    return x + 1 if y % 2 == 0 else x, y - 1


def getS(x, y):  # returns the south neighbor of a home
    return x + 1 if y % 2 == 0 else x + 1, y


def getSE(x, y):  # returns the south-east neighbor of a home
    return x + 1 if y % 2 == 0 else x, y + 1


def getNeighbors(x, y):  # returns neighbors of a house
    return [getNW(x, y), getN(x, y), getNE(x, y), getSW(x, y), getS(x, y), getSE(x, y)]


def getNeighborsWithDirection(x, y):  # returns neighbors of a house with the corresponding direction
    return [('nw', x - 1 if y % 2 == 1 else x, y - 1), ('n', x - 1 if y % 2 == 1 else x - 1, y),
            ('ne', x - 1 if y % 2 == 1 else x, y + 1), ('sw', x + 1 if y % 2 == 0 else x, y - 1),
            ('s', x + 1 if y % 2 == 0 else x + 1, y), ('se', x + 1 if y % 2 == 0 else x, y + 1)]


def getCoordinates(x, y, direction):  # conditionally returns the corresponding direction
    if direction == 'nw':
        return getNW(x, y)
    elif direction == 'n':
        return getN(x, y)
    elif direction == 'ne':
        return getNE(x, y)
    elif direction == 'sw':
        return getSW(x, y)
    elif direction == 's':
        return getS(x, y)
    elif direction == 'se':
        return getSE(x, y)
