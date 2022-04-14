class Piece:
    def __init__(self, pieceName, pieceId):
        self.name = pieceName  # determines which kind of piece is it
        self.id = pieceId  # determines the id of piece

    def __eq__(self, other):
        return self.id == self.id and self.name == self.name
