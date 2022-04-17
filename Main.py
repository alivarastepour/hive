from Game import Game
from Piece import Piece
from User import User
from constants import ANT, SPIDER, QUEEN, BEETLE, GRASSHOPPER
from hexagon_board import App
from gameInstance import game

if __name__ == '__main__':
    user1, user2 = User(1), User(2)
    # game.fillHome(1, QUEEN, 8, 10)
    game.fillHome(1, ANT, 7, 8)
    game.fillHome(2, ANT, 7, 9)
    game.fillHome(1, ANT, 8, 7)
    game.fillHome(2, ANT, 7, 10)
    game.fillHome(1, ANT, 8, 8)
    game.fillHome(2, ANT, 8, 11)
    game.fillHome(1, ANT, 8, 6)
    game.fillHome(2, ANT, 8, 12)
    game.fillHome(1, ANT, 9, 6)
    print(game.spiderValidMoves(8, 12))
    # game.fillHome(1, ANT, 9, 10)
    # game.fillHome(2, ANT, 7, 12)
    # game.fillHome(1, ANT, 9, 9)
    # game.fillHome(2, GRASSHOPPER, 7, 11)
    # game.fillHome(1, GRASSHOPPER, 10, 9)
    # game.fillHome(2, GRASSHOPPER, 8, 13)
    # game.fillHome(1, GRASSHOPPER, 10, 10)
    # game.fillHome(2, GRASSHOPPER, 6, 11)
    # game.fillHome(1, GRASSHOPPER, 11, 9)
    # game.fillHome(2, GRASSHOPPER, 6, 12)
    # print(game.availablePositions())
    # game.fillHome(1, GRASSHOPPER, 1, 6)
    # print(game.grasshopperValidMoves(8, 10))
    # print(game.availablePositions())
    # print()
