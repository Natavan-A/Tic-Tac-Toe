from alpha_beta_search import AlphaBetaSearch
from connection        import Connection
from board             import Board
from player            import Player
from square            import Square
import pygame
import time

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

    # PUBLIC METHODS
    def set_board(self, size=12, target=6):
        players = [self.__player, self.__opponent]
        self.__board = Board(size, target, players)

    def set_player(self, player):
        self.__player = player

    def set_opponent(self, opponent):
        self.__opponent = opponent

    def create(self, game_type="TTT"):

        response = self.__connection.create_a_game(
            self.__player.get_id(), 
            self.__opponent.get_id(), 
            game_type, 
            self.__board.get_size(), 
            self.__board.get_target()
        )
        
        if self.__connection.validate(response):
            game_id = response.json()['gameId']
            self.__set_id(game_id)


    def connect(self, game_id):
        # CHECK WHETHER GAME ID EXISTS
        response = self.__connection.get_board_string(game_id)

        if self.__connection.validate(response):
            self.__set_id(game_id)
            print(f'Connected to the game {game_id}')

    def testing(self):

            board       = self.__board
            opponent    = self.__opponent
            search      = AlphaBetaSearch(board)
            start       = time.time()
            end_game    = False

            while not end_game:

                response = None

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
                if search.terminal_test(): end_game = True
                print('Evaluation time: {}s'.format(round(end - start, 7)))
                # pygame.time.delay(600)

            return self.__board.get_winner().get_sign()


    def start(self):

        board       = self.__board
        opponent    = self.__opponent
        search      = AlphaBetaSearch(board)
        start       = time.time()
        end_game    = False

        while not end_game:

            response = None

            if not board.get_current_player() is opponent: # if my turn

                move = search.start()
                response = self.__connection.make_a_move(teamId=self.__player.get_id(), gameId=self.__id, move=f'{move.get_x()},{move.get_y()}')
                
                while not self.__connection.validate(response):
                    response = self.__connection.make_a_move(teamId=self.__player.get_id(), gameId=self.__id, move=f'{move.get_x()},{move.get_y()}')

                print(f'{move.get_position()} -> player')
            else:
                # print('INPUT')
                # x, y = map(int, input().split())
                # move = board.get_move((x, y))
                response = self.__connection.get_the_move_list(gameId=self.__id)
                while not self.__connection.validate(response) or not response.json()['moves'][0]['teamId'] == self.__player.get_id():
                    response = self.__connection.get_the_move_list(gameId=self.__id)
                    move = tuple(map(int, response.json()['moves'][0]['move'].split(',')))
                    move = self.__board.get_move(move)
                    print('wainting opponent')
                # move = search.start()
                print(f'{move.get_position()} -> opponent')

            end = time.time()
            board.set_square(move)
            board.record_round()
            board.sketch_board()
            if search.terminal_test(): end_game = True
            print('Evaluation time: {}s'.format(round(end - start, 7)))
            # pygame.time.delay(600)

        return self.__board.get_winner().get_sign()









    # def start(self):

    #     board   = self.__board
    #     search  = AlphaBetaSearch()
    #     start   = time.time()
    #     self.__board.sketch_board()

    #     while True:
    #         # IF IT IS MY TURN
    #         move = search.start(board)
                
            
    #         if board.get_current_player() is self.__player:
    #             print(f'{move.get_position()} -> player')
    #                 # response = self.__connection.make_a_move(teamId=self.__my_team.get_id(), gameId=self.__id, move=f'{move[0]},{move[1]}')

    #         # IF IT IS OPPONENT TURN
    #         else:
    #             # response = self.__connection.get_the_move_list(gameId=self.__id)
    #             print(f'{move.get_position()} -> opponent')
    #             # if self.__connection.validate(response):
    #                 # move = tuple(map(int, response.json()['moves'][0]['move'].split(',')))
    #                 # if self.__board.get_move(move).is_assigned():
    #                 #     print('not yet played') 
    #             #     return
    #         end = time.time()
    #         print('Evaluation time: {}s'.format(round(end - start, 7)))
           
    #         # if self.__connection.validate(response):
    #         self.__board.set_square(move), self.__board.sketch_board()
    #         pygame.time.delay(600)


        
        