from alpha_beta_search import AlphaBetaSearch
from connection        import Connection
from board             import Board
from player            import Player
from square            import Square
import pygame
import time
import sys
from helpers           import parse_board_string

class Game:
    def __init__(self, api_key, user_id):
        self.__id               = None
        self.__board            = None
        self.__players          = None
        self.__winner           = None
        self.__connection       = Connection(api_key=api_key, user_id=user_id)
        print(f'Game is ready to set up.')


    # PRIVATE METHODS
    def __set_id(self, id):
        self.__id = id
        print(f'Game {id} has been created.')

    def __set_board(self, size=12, target=6):
        self.__board = Board(size, target)

    def __set_players(self, player, opponent):
        player, opponent = Player(player['id'], player['sign']), Player(opponent['id'], opponent['sign'], opponent=True)

        if opponent.get_sign().lower() == 'o': self.__players = [opponent, player]
        elif player.get_sign().lower() == 'o': self.__players = [player, opponent]
        else:
            print('There is no any O sign assignment')
            sys.exit()

    def __update_turn(self):
        self.__players.reverse()
        

    # PUBLIC METHODS
    def get_board(self):
        return self.__board
        
    def create(self, player, opponent, board_size, target, game_type="TTT"):
        self.__set_players(player, opponent)
        self.__set_board(board_size, target)

        data = self.__connection.create_a_game(
            player['id'], 
            opponent['id'], 
            game_type, 
            board_size=board_size, 
            target=target
        )

        if data: 
            self.__set_id(data['gameId'])
        else:
            print("Exiting from the system")
            sys.exit()

    def get_current_player(self):
        return self.__players[0]

    def set_winner(self, player):
        self.__winner = player

    def get_winner(self):
        return self.__winner

    def has_winner(self):
        if self.__winner:
            return True
        return False

    def connect(self, player, opponent, game_id):
        data        = self.__connection.get_board_string(game_id)
        size, moves = parse_board_string(data['output'])
        target      = data['target']

        self.__set_players(player, opponent)
        self.__set_board(size=size, target=target)

        # tunning the latest player
        current_player = self.get_current_player()
        latest_player_id = self.__connection.get_the_move_list(gameId=self.__id)['moves'][0]['teamId']
        if not current_player.get_id() == latest_player_id: self.__update_turn()
        
        if moves:
            for move, sign in moves.items():
                player = self.__players[0] if self.get_current_player().get_sign().lower().__eq__(sign.lower()) else self.__players[1]
                move = self.__board.get_move(move)
                self.__board.set_square(move, player)
                self.__board.record_round()
        self.__set_id(game_id)
        print(f'Connected to the game {game_id}.')

    def testing(self, board_size, target):

        self.__set_board(board_size, target)
        self.__set_players({'id':777, 'sign':'O'}, {'id':111, 'sign':'X'})

        board       = self.__board
        search      = AlphaBetaSearch(board)
        player, opponent    = (self.__players[0], self.__players[1]) if not self.get_current_player().is_opponent() else (self.__players[1], self.__players[0])
        board.compute_terminals(player, opponent)

        while True:

            start = time.time()
            if self.get_current_player() is player: # if my turn
                move = search.start(*self.__players)

            elif self.get_current_player() is opponent: # if opponent turn
                try:
                    print('input:')
                    x, y = map(int, input().split())
                except: pass

                move = board.get_move((x, y))
                # move = search.start()

            end     = time.time() # record end time
            print(f'Round: {board.get_round()}\nLast move: {move.get_position()}\nPlayer: {self.get_current_player().get_sign()}')

            board.set_move(move, self.get_current_player())  # store the move
            board.update_terminals(player, opponent)
            board.record_round()    # we should know what round of the game it is
            board.sketch_board()    # draw the board

            print('Evaluation time: {}s'.format(round(end - start, 7)))

            if board.is_terminal(): return self.get_current_player()
            if board.is_full():     return None
            self.__update_turn()    # change the order of players


    def start(self):

        board               = self.__board
        search              = AlphaBetaSearch(board)
        player, opponent    = self.__players[0], self.__players[1] if not self.get_current_player().is_opponent() else self.__players[1], self.__players[0]

        data, move          = [None] * 2

        while True:
            start = time.time() # record start time

            # if the turn is mine
            if board.get_current_player() is player:
                move = search.start(*self.__players)
                while True: 
                    data = self.__connection.make_a_move(teamId=player.get_id(), gameId=self.__id, move=f'{move.get_x()},{move.get_y()}')
                    if data: break                    

            # get latest move and record it
            elif board.get_current_player() is opponent:
                while True:
                    data = self.__connection.get_the_move_list(gameId=self.__id)

                    if data and (opponent.get_id() == int(data['moves'][0]['teamId'])): 
                        move = self.__board.get_move(tuple(map(int, data['moves'][0]['move'].split(','))))
                        break

                    print('waiting opponent')
            
            end     = time.time() # record end time
            print(f'Round: {board.get_round()}\nLast move: {move.get_position()}\nPlayer: {self.get_current_player().get_sign()}')

            board.set_move(move, self.get_current_player())  # store the move
            board.update_terminals(player, opponent)
            board.record_round()    # we should know what round of the game it is
            board.sketch_board()    # draw the board

            print('Evaluation time: {}s'.format(round(end - start, 7)))

            if board.is_terminal(): return self.get_current_player()
            if board.is_full():     return None
            self.__update_turn()    # change the order of players