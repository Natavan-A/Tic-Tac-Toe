from connection import Connection
from player import Player
from board import Board
from game import Game
import time

if __name__ == "__main__":
    
    
    # data, _ = connection.create_a_team(name='helloss')

    # ADDING TEAM MEMBERS TO TEAMS
    # data, _ = connection.add_a_member(1248, 1055)
    # print(data)
    # data, _ = connection.add_a_member(1248, 1040)
    # print(data)
    # data, _ = connection.add_a_member(1256, 1051)
    # print(data)
    # data, _ = connection.add_a_member(1256, 1040)
    # print(data)
    # data, _ = connection.add_a_member(1256, 1055)
    # print(data)
    
    # CREATING A GAME
    # data, _ = connection.create_a_game(1248, 1256)

    # MAKING A MOVE
    # data, _ = connection.make_a_move(1248, 1474, "4,4")
    # print(data)

    # # MAKING AN OPPONENT MOVE
    # data, _ = connection.make_a_move(1256, 1474, "4,6")
    # print(data)

    # data, _ = connection.get_the_move_list(1474)
    # moves = data['moves'][0]
    # print(moves['teamId'])    
    player      = Player(1248, 'X')
    opponent    = Player(1256, 'O', opponent=True)

    game = Game(api_key='c9426ee5181dca77e9a2', user_id='1055')
    game.set_opponent(opponent)
    game.set_player(player)
    game.set_board(size=12, target=6)

    game.create()
    # game.connect(game_id=1509)

    # winner = game.start()
    winner = game.testing()

    if winner:
        print(f'Winner is {winner}')
    else:
        print('Game is tie!')

    # game.start_the_game()
    #isitend - teamId - 1248
    #helloss - teamId - 1256
    # 1248-1256 -> gameId - 1474

    # natavan -> 1051
    # aydin   -> 1055       