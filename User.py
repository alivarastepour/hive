from Piece import Piece
from constants import QUEEN, BEETLE, ANT, GRASSHOPPER, SPIDER


class User:
    def __init__(self, userId):
        self.id = userId
        self.availablePieces = dict(
            {
                QUEEN: [Piece(QUEEN, 1)],
                BEETLE: [Piece(BEETLE, i) for i in range(1, 3)],
                ANT: [Piece(ANT, i) for i in range(1, 4)],
                SPIDER: [Piece(SPIDER, i) for i in range(1, 3)],
                GRASSHOPPER: [Piece(GRASSHOPPER, i) for i in range(1, 4)],
            }
        )  # keeps track of individual user's remaining Pieces
        self.piecesPlacement = dict(
            {
                QUEEN: [None],
                BEETLE: [None, None],
                ANT: [None, None, None],
                SPIDER: [None, None],
                GRASSHOPPER: [None, None, None],
            }
        )
        self.hasEnteredTheQueen = False  # determines whether individual user's queen has been moved to the board

    def usePiece(self, piece, game):
        try:
            self.availablePieces.get(piece).pop(0)
        except IndexError:
            game.error = 'you have no {} left'.format(piece)
            return
        # self.piecesPlacement.update({piece:self.piecesPlacement.get(piece)[]})