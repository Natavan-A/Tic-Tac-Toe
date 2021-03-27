from connection import Connection
from player import Player
from board import Board
from game import Game
import time

if __name__ == "__main__": 
    player      = Player(1248, 'X')
    opponent    = Player(1256, 'O', opponent=True)

    game = Game(api_key='c9426ee5181dca77e9a2', user_id='1055')
    game.set_opponent(opponent)
    game.set_player(player)
    game.set_board(size=12, target=6)

    # game.create()
    game.connect(game_id=1509)

    # winner = game.start()
    winner = game.testing()

    if winner:
        print(f'Winner is {winner}')
    else:
        print('Game is tie!')    