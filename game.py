from connection import Connection
from board import TTT_Board

class Game:
    def __init__(self, connection, size, target, my_team_id, opponent_team_id, my_sign, game_id = None):
        self.__id               = None
        self.__connection       = connection
        self.__ttt_board        = TTT_Board(size, target)
        self.__my_id            = int(my_team_id)
        self.__opponent_id      = int(opponent_team_id)
        self.__my_sign          = my_sign
        self.__opponent_sign    = 'O' if my_sign == 'X' else 'X'

        if (game_id == None):
            # MAKING API REQUEST
            response = self.__connection.create_a_game(my_team_id, opponent_team_id, "TTT", size, target)
            
            # CHECKING WHETHER THE REQUEST IS VALID
            if Connection.validate(response):
                self.__id = response.json()['gameId']
        else:
            self.__id = game_id

    def get_id(self):
    	return self.__id

    def get_api_connection(self):
        return self.__connection

    def get_ttt_board(self):
        return self.__ttt_board

    def get_my_id(self):
    	return self.__my_id

    def get_my_sign(self):
    	return self.__my_sign

    def get_opponent_id(self):
    	return self.__opponent_id

    def get_opponent_sign(self):
    	return self.__opponent_sign

    def make_a_move(self, sign, row, column):
    	self.__ttt_board.fill_cell(sign, row, column)