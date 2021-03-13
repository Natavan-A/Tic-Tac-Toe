from connection import Connection
from board import Board
from team import Team


class Game:
    def __init__(self):
        self.__id               = None
        self.__target           = None
        self.__me               = None
        self.__opponent         = None
        self.__board            = None
        self.__winning_states   = None
        self.__connection       = None


    def set_api_connection(self, connection):
        self.__connection = connection
    
    def set_target(self, target):
        self.__target = target

    def set_my_team(self, id, sign):
        self.__me = Team(id, sign, self.__target)

    def set_opponent_team(self, id, sign):
        self.__opponent = Team(id, sign, self.__target)

    def set_teams(self, me, opponent):
        self.__me       = me
        self.__opponent = opponent

    def set_target(self, target):
        self.__target = target

    def set_board(self, size=12):
        self.__board = Board(size)

    def create(self, game_type="TTT"):
        board_size  = self.__board.get_size()
        target      = self.__target
        player_1    = self.__me.get_id() if self.__me.get_sign() == 'X' else self.__opponent.get_id()
        player_2    = self.__me.get_id() if self.__me.get_sign() == 'O' else self.__opponent.get_id()

        # MAKING API REQUEST
        response    = self.__connection.create_a_game(player_1, player_2, game_type, board_size, target)
        
        # CHECKING WHETHER THE REQUEST IS VALID
        if Connection.validate(response):
            self.__id = response.json()['game_id']

