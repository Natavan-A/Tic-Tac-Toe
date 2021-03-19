from point import Point


class Board:
    def __init__(self, size):
        self.__size             = size
        self.__elements         = self.__create(size)
        self.__available_points = size**2

    def __create(self, size):
        row = column = size
        return {f'{x},{y}': Point(x,y) for x in range(row) for y in range(column)}

    def set_point(self, x, y, player):
        point = self.__board[f'{x},{y}']
        point.set_assignee(player)
        self.__available_points -= 1

    def get_size(self):
        return self.__size

    def get_point(self, x, y):
        return self.__board[f'{x},{y}']
    
    def is_full(self):
        return self.__available_points == 0

class TTT_Board:
    def __init__(self, size, target):
        self.__size             = size
        self.__target           = target
        self.__all_cells        = size**2
        self.__filled_cells     = 0
        self.__winning_states   = self.set_winning_states(size, target)
        self.__matrix           = [['-' for i in range(size)] for i in range(size)]

    def get_size(self):
        return self.__size

    def get_target(self):
        return self.__target
    
    def is_full(self):
        return self.__all_cells == self.__filled_cells

    def get_winning_states(self):
        return self.__winning_states

    def get_matrix(self):
        return self.__matrix

    def fill_cell(self, sign, row, column):
        self.__matrix[row][column] = sign
        self.__filled_cells += 1

    def is_it_end(self, board):
        sign = None
        matrix = board.get_matrix()
        winning_states = board.get_winning_states()

        # CHECK IF BOARD IS FULL
        full_board = board.is_full()
        if (full_board): return True

        # CHECK FOR WINNING FOR EACH OF THE TERMINAL STATES
        for state in winning_states:
            sign = None
            for i in range(len(state)):
                cell = matrix[state[i][0]][state[i][1]]
                if (sign is None):
                    sign = cell
                    continue
                else:
                    if (cell != sign): break
                    elif (i != len(state)-1): continue

                # WHEN REACHED TO THE END AND ALL SIGNS ARE EQUAL
                return True

        return False

    def set_winning_states(self, board_size, target):
        winning_states = []

        for i in range(board_size):
            for j in range(board_size):
                # TEMPORARY VARIABLES
                rows = []
                columns = []
                diagonals = []
                diagonals2 = []

                # STORING POSSIBLE WINNING STATES ROW, COLUMN AND DIAONAL-BASED
                for k in range(target):
                    if (j+target <= board_size):
                        rows.append((i,j+k))
                        if (i+target <= board_size):
                            diagonals.append((i+k,j+k))
                        if (i-target+1 >= 0):
                            diagonals2.append((i-k,j+k))
                    if (i+target <= board_size):
                        columns.append((i+k,j))

                # STORING STATES TO THE GLOBAL LIST
                if (len(rows) != 0): 
                    winning_states.append(rows)
                if (len(columns) != 0): 
                    winning_states.append(columns)
                if (len(diagonals) != 0):
                    winning_states.append(diagonals)
                if (len(diagonals2) != 0):
                    winning_states.append(diagonals2)

        return winning_states