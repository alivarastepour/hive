from Game import Game
from Piece import Piece
from User import User
from constants import ANT, SPIDER, QUEEN, BEETLE, GRASSHOPPER
from hexagon_board import App

if __name__ == '__main__':
    game = Game()
    user1, user2 = User(1), User(2)
    app = App()
    app.mainloop()

