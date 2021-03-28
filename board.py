from square import Square
from helpers import *


class Board:
    def __init__(self, size, target, players):
        self.__size                 = size
        self.__moves                = []
        self.__round                = 0
        self.__target               = target
        self.__players              = players
        self.__squares              = {(x, y): Square(x, y) for x in range(size) for y in range(size)}
        # self.__scores_table         = self.__compute_scores()
        self.__winner               = None
        self.__compute_terminals()

        # FEEDBACK
        print(f'Board sized {size} with target {target} is set.')


    # PRIVATE METHODS
    def __compute_terminals(self):

        size                = self.__size
        target              = self.__target
        squares             = self.__squares

        # number of terminal states: size - target + 1 and +1 for upperbound
        num_of_terminals    = size - target + 1

        
        def compute_terminal(kind, initial, target=6, closure=None):
            x, y        = initial
            terminals   = []

            if kind.__eq__('east_north'):
                # vertical
                x, y = initial
                terminal = []
                for _ in range(target):
                    terminal.append((x, y))
                    x += 1
                terminals.append(terminal)

                # horizontal
                x, y = initial
                terminal = []
                for _ in range(target):
                    terminal.append((x, y))
                    y += 1
                terminals.append(terminal)

                # diagonal
                x, y = initial
                terminal = []
                for _ in range(target):
                    terminal.append((x, y))
                    x += 1
                    y += 1
                terminals.append(terminal)

            if kind.__eq__('east_south'):
                # vertical
                x, y = initial
                terminal = []
                for _ in range(target):
                    terminal.append((x, y))
                    x -= 1
                terminals.append(terminal)

                # horizontal
                x, y = initial
                terminal = []
                for _ in range(target):
                    terminal.append((x, y))
                    y += 1

                # diagonal
                x, y = initial
                terminal = []
                for _ in range(target):
                    terminal.append((x, y))
                    x -= 1
                    y += 1
                terminals.append(terminal)

            if kind.__eq__('west_north'):
                # vertical
                x, y = initial
                terminal = []
                for _ in range(target):
                    terminal.append((x, y))
                    x += 1
                terminals.append(terminal)

                # horizontal
                x, y = initial
                terminal = []
                for _ in range(target):
                    terminal.append((x, y))
                    y -= 1
                terminals.append(terminal)

                # diagonal
                x, y = initial
                terminal = []
                for _ in range(target):
                    terminal.append((x, y))
                    x += 1
                    y -= 1
                terminals.append(terminal)


            if kind.__eq__('west_south'):
                # vertical
                x, y = initial
                terminal = []
                for _ in range(target):
                    terminal.append((x, y))
                    x -= 1
                terminals.append(terminal)

                # horizontal
                x, y = initial
                terminal = []
                for _ in range(target):
                    terminal.append((x, y))
                    y -= 1
                terminals.append(terminal)

                # diagonal
                x, y = initial
                terminal = []
                for _ in range(target):
                    terminal.append((x, y))
                    x -= 1
                    y -= 1
                terminals.append(terminal)

            if closure: closure(terminals)

        def set_to_squares(terminals):
            for terminal in terminals:
                terminal = [squares[position] for position in terminal]
                for square in terminal: square.add_terminal(terminal)


        for x in range(num_of_terminals):
            for y in range(num_of_terminals):
                compute_terminal(kind='east_north', initial=(x, y), target=target, closure=set_to_squares)

                compute_terminal(kind='west_north', initial=(x, size - y - 1), target=target, closure=set_to_squares)
                
                compute_terminal(kind='east_south', initial=(size - x - 1, y), target=target, closure=set_to_squares)

                compute_terminal(kind='west_south', initial=(size - x - 1, size - y - 1), target=target, closure=set_to_squares)



        print(f'Terminals calculated')
        
    # PUBLIC METHODS
    def get_move(self, move):
        return self.__squares[move]

    def get_terminals(self):
        return self.__terminals

    def get_terminal_score(self, key):
        key = sorted(key, key=lambda item: item if item else 0)
        return self.__scores_table[str(key)]
    
    def record_round(self):
        self.__round = len(self.__moves)

    def get_round(self):
        self.__round

    def get_moves(self):
        return self.__moves

    def get_latest_move(self):
        return self.__moves[-1]

    def get_size(self):
        return self.__size

    def get_winner(self):
        return self.__winner
    
    def get_target(self):
        return self.__target
    
    def get_empty_squares(self):
        return list(set(self.__squares.values()).difference(set(self.__moves)))

    def get_empty_squares_sorted(self):
        return sorted(list(set(self.__squares.values()).difference(set(self.__moves))), key=lambda item: item.get_score(), reverse=True)
        
    def get_current_player(self):
        return self.__players[0]

    def get_next_player(self):
        return self.__players[1]
    
    def set_players(self, players):
        self.__players = players if players[0].get_sign().lower() == 'x' else players.reverse()

    def set_square(self, move):
        move.set_assignee(self.get_current_player())
        self.__moves.append(move)
        self.__update_empty_square_scores()
        self.__players.reverse() # change players order

    def undo(self):
        self.__squares[self.__moves[-1].get_position()].set_assignee(None)
        self.__moves.pop()
        self.__update_empty_square_scores()
        self.__players.reverse()

    def has_moves(self, enough=None):
        if enough:
            return len(self.__moves) >= self.__target
        return not len(self.__moves[self.__round:]) == 0

    def has_winner(self):
        if self.__winner:
            return True
        return False

    def is_full(self):
        return (self.__size ** 2) - len(self.__moves) == 0

    def is_terminal(self):
        square          = self.__moves[-1] # lastest move
        previous_player  = self.get_next_player() # next player is logically was previous one
        win_state       = [previous_player] * self.__target
        
        if self.is_full(): return True
        
        for terminal in square.get_terminals():
            if win_state == [square.get_assignee() for square in terminal]:
                self.__winner = previous_player
                return True
        return False

    def __update_empty_square_scores(self):
        empty_squares   = self.get_empty_squares()
        
        for square in empty_squares:
            for terminal in [[square.get_assignee() for square in terminal] for terminal in square.get_terminals()]:
                u_terminal = set(terminal)
                if any(u_terminal):
                    if len(u_terminal) == 3: square.update_score(-100)
                    else:
                        player = u_terminal.__iter__().__next__()
                        count  = len(list(filter(lambda item: item is player, terminal)))
                        square.update_score(10**count)
                else:
                    square.update_score(1)

    def sketch_board(self):
        board = self.__squares
        for i in range(self.__size):
            for j in range(self.__size):
                print(f'{board[(i,j)].get_assignee().get_sign() if board[(i,j)].get_assignee() else "."}|', end='')
            print()