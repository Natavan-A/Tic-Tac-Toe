from connection import Connection
from game import Game, Game2
from team import Team
from helpers import ALPHA_BETA_SEARCH

def make_a_move(connection, game, teamId, next_move):
    next_move_str = "{},{}".format(next_move[0],next_move[1])
    sign = game.get_my_sign()
    if (teamId != game.get_my_id()): sign = game.get_opponent_sign()

    print(connection.make_a_move(teamId, game.get_id(), next_move_str))
    ##### if unsuccessful ???
    game.make_a_move(sign, next_move[0], next_move[1])


if __name__ == "__main__":
    connection = Connection(api_key='c9426ee5181dca77e9a2', user_id='1055')
    
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



    # game = Game()
    # game.set_api_connection(connection)
    # game.set_target(20)
    # game.set_board(12)
    # game.set_my_team(1248, 'X')
    # game.set_opponent_team(1256, 'O')

    # game.create()
    # print(connection.get_my_games())

    game = Game2(connection, 8, 4, 1248, 1256, 'X')
    ttt_board = game.get_ttt_board()
    print(ttt_board.get_matrix())
    winning_states = ttt_board.get_winning_states()

    # ME
    next_move = ALPHA_BETA_SEARCH(game.get_my_sign(), ttt_board, winning_states)
    make_a_move(connection, game, game.get_my_id(), next_move)
    print(ttt_board.get_matrix())

    # OPPONENT
    next_move = ALPHA_BETA_SEARCH(game.get_opponent_sign(), ttt_board, winning_states)
    make_a_move(connection, game, game.get_opponent_id(), next_move)
    print(ttt_board.get_matrix())

    # ME
    next_move = ALPHA_BETA_SEARCH(game.get_my_sign(), ttt_board, winning_states)
    make_a_move(connection, game, game.get_my_id(), next_move)
    print(ttt_board.get_matrix())

    # OPPONENT
    next_move = ALPHA_BETA_SEARCH(game.get_opponent_sign(), ttt_board, winning_states)
    make_a_move(connection, game, game.get_opponent_id(), next_move)
    print(ttt_board.get_matrix())

    # ME
    next_move = ALPHA_BETA_SEARCH(game.get_my_sign(), ttt_board, winning_states)
    make_a_move(connection, game, game.get_my_id(), next_move)
    print(ttt_board.get_matrix())

    # OPPONENT
    next_move = ALPHA_BETA_SEARCH(game.get_opponent_sign(), ttt_board, winning_states)
    make_a_move(connection, game, game.get_opponent_id(), next_move)
    print(ttt_board.get_matrix())

    # ME
    next_move = ALPHA_BETA_SEARCH(game.get_my_sign(), ttt_board, winning_states)
    make_a_move(connection, game, game.get_my_id(), next_move)
    print(ttt_board.get_matrix())

    # OPPONENT
    next_move = ALPHA_BETA_SEARCH(game.get_opponent_sign(), ttt_board, winning_states)
    make_a_move(connection, game, game.get_opponent_id(), next_move)
    print(ttt_board.get_matrix())

    # ME
    next_move = ALPHA_BETA_SEARCH(game.get_my_sign(), ttt_board, winning_states)
    make_a_move(connection, game, game.get_my_id(), next_move)
    print(ttt_board.get_matrix())

    # OPPONENT
    # next_move = ALPHA_BETA_SEARCH(game.get_opponent_sign(), ttt_board, winning_states)
    # make_a_move(connection, game, game.get_opponent_id(), next_move)
    # print(ttt_board.get_matrix())

    # game.start_the_game()
    #isitend - teamId - 1248
    #helloss - teamId - 1256
    # 1248-1256 -> gameId - 1474

    # natavan -> 1051
    # aydin   -> 1055
    # ilyas   -> 1040
