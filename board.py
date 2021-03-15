from move import Move


class Board:
    def __init__(self, size, target):
        self.__size             = size
        self.__target           = target
        self.__board            = [[Move(x,y) for x in range(size)] for y in range(size)]
        self.__win_states       = self.calculate_win_states()
        self.__available_moves  = size**2

    def set_move(self, move):
        self.__board[x][y] = move
        self.__available_points -= 1

    def get_move(self, x, y):
        return self.__board[x][y]

    def get_size(self):
        return self.__size
        
    def get_target(self):
        return self.__target

    def get_win_states(self):
        return self.__win_states

    def calculate_win_states(self):
        win_states = {
            "vertical"  : {},
            "horizontal": {},
            "diagonal"  : {},
        }

        try:
            # vertical and horizontal win states
            # size - target + 1 -> winning state in each column/row
            for i in range(self.__size):
                vertical_win_state_list     = []
                horizontal_win_state_list   = []
                for j in range(self.__size - self.__target + 2): # additional +1 for making upperbound
                    vertical_win_state_list.append((j, i))
                    horizontal_win_state_list.append((i, j))
                win_states['vertical'][i]    = vertical_win_state_list
                win_states['horizontal'][i]  = horizontal_win_state_list

            # diagonal win states
            # size - target + 1 -> winning state in each row

        except:
            pass

    def is_full(self):
        return self.__available_moves == 0