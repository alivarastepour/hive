class User:
    def __init__(self, userId):
        self.id = userId
        self.availablePieces = dict({'queen': 1, 'beetle': 2, 'ant': 3, 'spider': 2,
                                     'grasshopper': 3, })  # keeps track of individual user's remaining Pieces
        self.hasEnteredTheQueen = False  # determines whether individual user's queen has been moved to the board
