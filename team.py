from copy import deepcopy

class Team:
    def __init__(self, id, sign, board):
        self.__id             = id
        self.__sign           = None
        self.__board          = board
        self.__moves          = []
        self.__win_states     = deepcopy(board.get_win_states())
        self.__is_turn        = True if sign.lower() == 'x' else False

    def get_id(self):
        return self.__id

    def get_sign(self):
        return self.__sign

    def is_turn(self):
        return self.__is_turn

    def played(self):
        self.__is_turn = False
