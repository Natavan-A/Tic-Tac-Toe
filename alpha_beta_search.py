from copy import deepcopy

class AlphaBetaSearch:
    def __init__(self,  board, my_team, opponent_team):
        self.__board            = board
        self.__my_team          = my_team
        self.__opponent_team    = opponent_team


    def __switch_players(self, player):
        return self.__my_team if not player == self.__my_team else self.__opponent_team

    def __terminal_test(self, state):
        if state.is_full() or state.has_winner():
            return True
        return False

    def __utility(self, state, player):
        if state.has_winner():
            if player == state.get_winner(): 
                return 1
            return 0
        return 0.5


    def __result(self, state, player, move):
        state.set_move(player, move)
        state.update_available_moves(move)
        return state

    def __max_value(self, state, player, a, b):
        if self.__terminal_test(state): return self.__utility(state, player)

        v = float("-inf")
        best_move = None

        for move in state.get_available_moves():
            temp = v
            
            state_copied  = self.__result(deepcopy(state), player, move)
            player_copied = self.__switch_players(deepcopy(player))

            v = max(v, self.__min_value(state_copied, player_copied, a, b))

            if not temp == v: best_move = move

            if v >= b: a = max(a, v)

        state.get_move(best_move).set_value(v)

        return v

    def __min_value(self, state, player, a, b):
        if self.__terminal_test(state): return self.__utility(state, player)

        v = float("inf")
        worst_move = None

        for move in state.get_available_moves():
            temp = v

            state_copied  = self.__result(deepcopy(state), player, move)
            player_copied = self.__switch_players(deepcopy(player))

            v = min(v, self.__max_value(state_copied, player_copied, a, b))
            
            if not temp == v: worst_move = move

            if v <= a: b = min(b, v)

        state.get_move(worst_move).set_value(v)

        return v

    def start(self, ):
        state  = deepcopy(self.__board)
        player = deepcopy(self.__my_team)

        best_move  = None
        best_value = float('-inf')

        for move in state.get_available_moves():
            v = self.__max_value(state, player, a=float('-inf'), b=float('inf'))

        move = state.get_best_move(v)

        return move