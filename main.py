from connection import Connection
from player import Player
from board import Board
from game import Game
import time

if __name__ == "__main__":

    game = Game(api_key='c9426ee5181dca77e9a2', user_id='1055')
    # 1256 1255
    game.create(player=(1255, 'X'), opponent=(1256, 'O'), board_size=6, target=4)
    # game.connect(game_id=1509)

    winner = game.start()
    # winner = game.testing()
    
    print(f'Game ended at the round {game.get_board().get_round()}')

    if winner:
        print(f'The winner is {winner}')
    else:
        print('There is no winner. Game is tie!')    