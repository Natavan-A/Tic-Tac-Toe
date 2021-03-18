from connection import Connection
from game import Game, Game2
from team import Team
from helpers import ALPHA_BETA_SEARCH

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

    game = Game2(connection, 12, 6, 1248, 1256, 'X')
    ttt_board = game.get_ttt_board()
    board = ttt_board.get_board()
    print(board)
    winning_states = ttt_board.get_winning_states()

    # ME
    next_move = ALPHA_BETA_SEARCH(game.get_my_sign(), board, winning_states)
    game.make_move(game.get_my_sign(), next_move[0], next_move[1])
    board = ttt_board.get_board()
    print(board)

    # OPPONENT
    next_move = ALPHA_BETA_SEARCH(game.get_opponent_sign(), board, winning_states)
    game.make_move(game.get_opponent_sign(), next_move[0], next_move[1])
    board = ttt_board.get_board()
    print(board)

    # ME
    next_move = ALPHA_BETA_SEARCH(game.get_my_sign(), board, winning_states)
    game.make_move(game.get_my_sign(), next_move[0], next_move[1])
    board = ttt_board.get_board()
    print(board)

    # OPPONENT
    next_move = ALPHA_BETA_SEARCH(game.get_opponent_sign(), board, winning_states)
    game.make_move(game.get_opponent_sign(), next_move[0], next_move[1])
    board = ttt_board.get_board()
    print(board)

    # ME
    next_move = ALPHA_BETA_SEARCH(game.get_my_sign(), board, winning_states)
    game.make_move(game.get_my_sign(), next_move[0], next_move[1])
    board = ttt_board.get_board()
    print(board)

    # OPPONENT
    next_move = ALPHA_BETA_SEARCH(game.get_opponent_sign(), board, winning_states)
    game.make_move(game.get_opponent_sign(), next_move[0], next_move[1])
    board = ttt_board.get_board()
    print(board)

    # ME
    next_move = ALPHA_BETA_SEARCH(game.get_my_sign(), board, winning_states)
    game.make_move(game.get_my_sign(), next_move[0], next_move[1])
    board = ttt_board.get_board()
    print(board)

    # OPPONENT
    next_move = ALPHA_BETA_SEARCH(game.get_opponent_sign(), board, winning_states)
    game.make_move(game.get_opponent_sign(), next_move[0], next_move[1])
    board = ttt_board.get_board()
    print(board)

    # ME
    next_move = ALPHA_BETA_SEARCH(game.get_my_sign(), board, winning_states)
    game.make_move(game.get_my_sign(), next_move[0], next_move[1])
    board = ttt_board.get_board()
    print(board)

    # game.start_the_game()
    #isitend - teamId - 1248
    #helloss - teamId - 1256
    # 1248-1256 -> gameId - 1474

    # natavan -> 1051
    # aydin   -> 1055
    # ilyas   -> 1040
