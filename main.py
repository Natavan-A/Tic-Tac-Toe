import time
from connection import Connection
from game import Game
from helpers import ALPHA_BETA_SEARCH

my_id = 1255
def make_a_move(connection, game, teamId, next_move):
    next_move_str = "{},{}".format(next_move[0],next_move[1])
    sign = game.get_my_sign()
    if (teamId != game.get_my_id()): sign = game.get_opponent_sign()
    
    data = (connection.make_a_move(teamId, game.get_id(), next_move_str)).json()
    if (data['code'] != 'FAIL'):
        game.make_a_move(sign, next_move[0], next_move[1])
    else: print(data)

def play_an_open_game(connection):
    global my_id
    # RETRIEVE IDS OF OPEN GAMES
    myGames = connection.get_my_games().json()['myGames']
    print("MY OPEN GAMES: "+ str(len(myGames)))

    # PLAY ONE OF OPEN GAMES
    if (len(myGames) > 0):
        print(myGames[-1])
        game_id = list(myGames[-1].keys())[0]
        parts = myGames[-1][game_id].split(':')
        opponent_id = 0
        my_sign = 'O'
        if (int(parts[0]) == my_id): opponent_id = int(parts[1])
        else:
            opponent_id = int(parts[0])
            my_sign = 'X'

        requestInfo = connection.get_board_string(game_id).json()
        board = requestInfo['output'].strip()
        lines = board.split('\n')
        size = len(lines)
        target = int(requestInfo['target'])

        print("Board Size: "+str(size)+"; Target: "+str(target))

        # CREATING THE GAME
        game = Game(connection, size, target, my_id, opponent_id, my_sign, game_id)
        ttt_board = game.get_ttt_board()
        winning_states = ttt_board.get_winning_states()
        print(ttt_board.get_matrix())

        # STORING ALL PREVIOUS MOVES
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                ch = lines[i][j]
                current_teamId = my_id
                if ch == 'X' or ch == 'O':
                    game.make_a_move(ch, i, j)

        print(ttt_board.get_matrix())

        playing(connection, game, ttt_board, winning_states)

def play_an_open_game_with_id(connection, game_id, opponent_id):
    global my_id

    my_sign = 'X'

    requestInfo = connection.get_board_string(game_id).json()
    board = requestInfo['output'].strip()
    lines = board.split('\n')
    size = len(lines)
    target = int(requestInfo['target'])

    print("Board Size: "+str(size)+"; Target: "+str(target))

    # CREATING THE GAME
    game = Game(connection, size, target, my_id, opponent_id, my_sign, game_id)
    ttt_board = game.get_ttt_board()
    winning_states = ttt_board.get_winning_states()
    print(ttt_board.get_matrix())

    # STORING ALL PREVIOUS MOVES
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            ch = lines[i][j]
            current_teamId = my_id
            if ch == 'X' or ch == 'O':
                game.make_a_move(ch, i, j)

    print(ttt_board.get_matrix())

    playing(connection, game, ttt_board, winning_states)

def create_and_play_a_game(connection, opponent_id, size, target):
    # CREATE YOUR OWN GAME
    global my_id
    game = Game(connection, size, target, my_id, opponent_id, 'O')
    ttt_board = game.get_ttt_board()
    winning_states = ttt_board.get_winning_states()
    print(game.get_id())
    print(ttt_board.get_matrix())

    playing(connection, game, ttt_board, winning_states)


def playing(connection, game, ttt_board, winning_states):
    # ME
    next_move = ALPHA_BETA_SEARCH(game.get_my_sign(), ttt_board, winning_states)
    make_a_move(connection, game, game.get_my_id(), next_move)
    print(ttt_board.get_matrix())
                
    while (ttt_board.is_it_end() == False):
        data = (connection.get_the_move_list(game.get_id())).json()
        print(data)
        if (int(data['moves'][0]['teamId']) == game.get_my_id()):
            # OPPONENT
            while(int(data['moves'][0]['teamId']) == game.get_my_id()):
                print("waiting for the opponent...")
                data = (connection.get_the_move_list(game.get_id())).json()
                time.sleep(7)

            # SAVING OPPONENT'S MOVE
            print("Opponent played")
            next_move = (int(data['moves'][0]['moveX']), int(data['moves'][0]['moveY']))
            game.make_a_move(game.get_opponent_sign(), next_move[0], next_move[1])
            print(ttt_board.get_matrix())
        else:
            # ME
            next_move = ALPHA_BETA_SEARCH(game.get_my_sign(), ttt_board, winning_states)
            make_a_move(connection, game, game.get_my_id(), next_move)
            print(ttt_board.get_matrix())

def test_play(connection, opponent_id, size, target):
    # CREATE YOUR OWN GAME
    global my_id
    sign = 'O'
    game = Game(connection, size, target, my_id, opponent_id, sign)
    ttt_board = game.get_ttt_board()
    winning_states = ttt_board.get_winning_states()
    print(ttt_board.get_matrix())

    # ME
    next_move = ALPHA_BETA_SEARCH(game.get_my_sign(), ttt_board, winning_states)
    # make_a_move(connection, game, game.get_my_id(), next_move)
    game.make_a_move(sign, next_move[0], next_move[1])
    print(ttt_board.get_matrix())
                
    while (ttt_board.is_it_end() == False):
        # data = (connection.get_the_move_list(game.get_id())).json()
        # if (int(data['moves'][0]['teamId']) == game.get_my_id()):
        # OPPONENT
        next_move = ALPHA_BETA_SEARCH(game.get_opponent_sign(), ttt_board, winning_states)
        # make_a_move(connection, game, game.get_opponent_id(), next_move)
        game.make_a_move(game.get_opponent_sign(), next_move[0], next_move[1])
        print(ttt_board.get_matrix())
        # else:
        # ME
        next_move = ALPHA_BETA_SEARCH(game.get_my_sign(), ttt_board, winning_states)
        # make_a_move(connection, game, game.get_my_id(), next_move)
        game.make_a_move(sign, next_move[0], next_move[1])
        print(ttt_board.get_matrix())

if __name__ == "__main__":
    connection = Connection(api_key='c9426ee5181dca77e9a2', user_id='1055')
    
    # data, _ = connection.create_a_team(name='helloss')

    # ADDING TEAM MEMBERS TO TEAMS
    # data = connection.add_a_member(1255, 1055)
    # print(data.json())
    # data, _ = connection.add_a_member(1248, 1040)
    # print(data)
    # data, _ = connection.add_a_member(1256, 1051)
    # print(data)
    # data, _ = connection.add_a_member(1256, 1040)
    # print(data)
    # data, _ = connection.add_a_member(1256, 1055)
    # print(data)
    
    # print(connection.get_my_games().json()['myGames'])
    # print(connection.get_board_string("2750").json())
    ################ IMPORTANT COMMANDS ############
    # play_an_open_game_with_id(connection, 2750, 1244) -- Won
    # create_and_play_a_game(connection, 1255, 3, 3)
    play_an_open_game_with_id(connection, 2771, 1255)
    ################################################

    #isitend - teamId - 1248
    #helloss - teamId - 1256
    #hellls  - teamId - 1255
    # 1248-1256 -> gameId - 1474

    # natavan -> 1051
    # aydin   -> 1055
    # ilyas   -> 1040
