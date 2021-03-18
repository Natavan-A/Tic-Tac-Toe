from move import Move
from copy import deepcopy


class Board:
    def __init__(self, size, target):
        self.__size                   = size
        self.__target                 = target
        self.__board                  = {(x, y): Move(x,y) for x in range(size) for y in range(size)}
        self.__winner                 = None
        self.__win_states             = self.calculate_win_states()
        self.__available_moves        = deepcopy(self.__board)
        self.__available_moves_count  = size**2

    def set_move(self, player, move):
        move = self.__board[move]
        move.set_assignee(player)
        self.__available_moves_count -= 1

    def get_move(self, move):
        return self.__board[move]

    def get_size(self):
        return self.__size
        
    def get_target(self):
        return self.__target

    def get_win_states(self):
        return self.__win_states
    
    def get_available_moves(self):
        return self.__available_moves

    def update_available_moves(self, move):
        del self.__available_moves[move]

    def get_best_move(self, value):
        for key, move in self.__board.items():
            if move.get_value() == value:
                return key

    def get_winner(self):
        return self.__winner

    def has_winner(self):
        return not self.__winner == None


    def get_available_moves_count(self):
        return self.__available_moves_count
    
    def calculate_win_states(self):
        win_states = {
            "vertical"  : dict(),
            "horizontal": dict(),
            "diagonal"  : list(),
        }

        try:
            # vertical and horizontal win states
            # size - target + 1 -> winning state in each column/row
            for i in range(self.__size):
                vertical_win_state_list      = list()
                horizontal_win_state_list    = list()
                for j in range(self.__size - self.__target + 2): # additional +1 for making upperbound
                    vertical_win_state_list.append((j, i))
                    horizontal_win_state_list.append((i, j))
                win_states['vertical'][i]    = vertical_win_state_list
                win_states['horizontal'][i]  = horizontal_win_state_list

            # diagonal win states
            # size - target + 1 -> winning state in the longest diagonal
            diagonal_win_state_set = set()
            for i in range(self.__size - self.__target + 1):
                for j in range(self.__size - self.__target + 1):
                    diagonal_win_state_set.add((i, j))
                    diagonal_win_state_set.add((i, self.__size - 1 - j)) # we want to get mirror reflection like
            win_states['diagonal'] = list(diagonal_win_state_set)
        except:
            print("ERROR IN BOARD FINDING WINNING STATES")

    def is_full(self):
        return self.__available_moves_count == 0
