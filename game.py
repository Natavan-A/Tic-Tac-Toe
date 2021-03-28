from alpha_beta_search import AlphaBetaSearch
from connection        import Connection
from board             import Board
from player            import Player
from square            import Square
import pygame
import time
import sys

class Game:
    def __init__(self, api_key, user_id):
        self.__id               = None
        self.__board            = None
        self.__player           = None
        self.__opponent         = None
        self.__connection       = Connection(api_key=api_key, user_id=user_id)
        print(f'Game is ready to set up.')


    # PRIVATE METHODS
    def __set_id(self, id):
        self.__id = id
        print(f'Game {id} has been created.')

    def __set_board(self, size=12, target=6):
        players = [self.__player, self.__opponent]
        self.__board = Board(size, target, players)
        
    # PUBLIC METHODS

    def get_board(self):
        return self.__board
        
    def create(self, player, opponent, board_size, target, game_type="TTT"):

        self.__player   = Player(player[0], player[1])
        self.__opponent = Player(opponent[0], opponent[1], opponent=True)
        self.__set_board(board_size, target)

        data = self.__connection.create_a_game(
            self.__player.get_id(), 
            self.__opponent.get_id(), 
            game_type, 
            self.__board.get_size(), 
            self.__board.get_target()
        )
        
        if data: self.__set_id(data['gameId'])
        else:
            print("Exiting from the system")
            sys.exit()


    def connect(self, player, game_id):
        # CHECK WHETHER GAME ID EXISTS
        data = self.__connection.get_board_string(game_id)

        if data:
            self.__set_id(game_id)
            print(f'Connected to the game {game_id}.')
        else:
            print("Error! Exiting from the game.")
            sys.exit()

    def testing(self):

        board       = self.__board
        opponent    = self.__opponent
        search      = AlphaBetaSearch(board)
        start       = time.time()

        while True:

            if not board.get_current_player() is opponent: # if my turn
                move = search.start()
                print(f'{move.get_position()} -> player')
            else:
                print('INPUT')
                x, y = map(int, input().split())
                move = board.get_move((x, y))
                # move = search.start()
                print(f'{move.get_position()} -> opponent')

            end = time.time()
            board.set_square(move)
            board.record_round()
            board.sketch_board()
            print('Evaluation time: {}s'.format(round(end - start, 7)))
            if search.terminal_test(): break

        return self.__board.get_winner().get_sign()


    def start(self):

        board       = self.__board
        opponent    = self.__opponent
        search      = AlphaBetaSearch(board)
        data        = None

        while True:
            start = time.time() # record start time

            # if the turn is mine
            if not board.get_current_player() is opponent:
                move = search.start()
                while True: 
                    data = self.__connection.make_a_move(teamId=self.__player.get_id(), gameId=self.__id, move=f'{move.get_x()},{move.get_y()}')
                    if data: break                    

            # get latest move and record it
            while True:
                data = self.__connection.get_the_move_list(gameId=self.__id)

                if data:
                    last_player = data['moves'][0]['teamId']
                    if self.__opponent.__eq__(last_player): break

                print('waiting opponent')
            
            end     = time.time() # record end time
            move    = self.__board.get_move(tuple(map(int, data['moves'][0]['move'].split(','))))

            print(f'Round: {board.get_round()}\n Last move: {move.get_position()}\n Player: {board.get_current_player()}')

            board.set_square(move) # store the move
            board.record_round()  # we should know what round of the game it is
            board.sketch_board() # draw the board

            print('Evaluation time: {}s'.format(round(end - start, 7)))

            if search.terminal_test(): break

        return self.__board.get_winner().get_sign()
