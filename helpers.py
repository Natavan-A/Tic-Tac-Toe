def switch_player(player):
	if (player == 'X'): return 'O'
	else: return 'X'

def is_terminal(player):
	n = len(board) 	# game.board
	target = 3		# game.target
	full_board = True
	win = False

	# ROW BASED WIN
	for i in range(n):
		for j in range(n):
			if (board[i][j] != '-' and j+target <= n):

				# STARTING FROM THE NEXT POSITION
				for k in range(j+1, target):
					if (board[i][j] != board[i][j+k]): break;
					if (k == target - 1): win = True
				if (win):
					print("row found")
					if (board[i][j] == player): return 1
					else: return -1
			else:
				# IF EMPTY SPOT DETECTED, THE BOARD IS NOT FULL
				if (board[i][j] == '-'):
					full_board = False

	# COLUMN BASED WIN
	for i in range(n):
		for j in range(n):
			if (board[j][i] != '-' and j+target <= n):

				# STARTING FROM THE NEXT POSITION
				for k in range(j+1, target):
					if (board[j][i] != board[j+k][i]): break;
					if (k == target - 1): win = True
				if (win):
					print("column found")
					if (board[j][i] == player): return 1
					else: return -1

	# DIAGONAL BASED WIN
	for i in range(n):
		for j in range(n):
			if (board[i][j] != '-' and j+target <= n):
				for k in range(target):
					if (i+target <= n):
						if (board[i][j] != board[i+k][j+k]): break;
					else:
						if (board[i][j] != board[i-k][j+k]): break;
					if (k == target - 1): win = True
				if (win):
					print("diagonal found")
					if (board[i][j] == player): return 1
					else: return -1

	if (full_board and not win):
		print("tie")
		return 0

def ALPHA_BETA_SEARCH(state): # returns an action
    pass

def MINIMAX_SEARCH(player, state): # returns 
    #if (terminal) return utility
    if (player == 'X'):
    	return MAX_VALUE(player, state)
    elif (player == 'O'):
    	return MIN_VALUE(player, state)


def MAX_VALUE(player, state): # returns 
    v = float('-inf')
    moves = game.moves

    # find maximum value
    for move in moves:
    	v = max(v, MINIMAX_SEARCH(switch_player(player), move))

    return v

def MIN_VALUE(player, state): # returns 
    v = float('inf')
    moves = game.moves

    # find minimum value
    for move in moves:
    	v = min(v, MINIMAX_SEARCH(switch_player(player), move))

    return v

# game part:::: will be removed
board = [['-' for x in range(3)] for x in range(3)]
board = [['X','O','X'],
		['X','O','O'],
		['O','X','X']]

board = [['X','O','X'],
		['O','O','O'],
		['O','X','X']]

board = [['X','O','X'],
		['O','O','X'],
		['O','X','X']]

board = [['O','O','X'],
		['O','X','O'],
		['X','O','X']]
# print(board)
player = 'X'
print(is_terminal(player))