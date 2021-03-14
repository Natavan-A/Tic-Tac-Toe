terminal_states = []

def switch_player(player):
	if (player == 'X'): return 'O'
	else: return 'X'

def my_player():
	return this_player

def get_moves(board):
	empy_spots = [] # a list to store moves
	n = len(board) 	# game.board

	# for loops can be removed if board class exists!!!
	for i in range(n):
		for j in range(n):
			if (board[i][j] == '-'): empy_spots.append((i,j))

	return empy_spots

def get_teminal_states(board_size, target):
	row_states = []
	column_states = []
	diagonal_states = []

	for i in range(board_size):
		for j in range(board_size):

			rows = []
			columns = []
			diagonals = []
			diagonals2 = []
			for k in range(target):
				if (j+target <= board_size):
					rows.append((i,j+k))
					if (i+target <= board_size):
						diagonals.append((i+k,j+k))
					if (i-target+1 >= 0):
						diagonals2.append((i-k,j+k))
				if (i+target <= board_size):
					columns.append((i+k,j))
			if (len(rows) != 0): 
				row_states.append(rows)
				terminal_states.append(rows)
			if (len(columns) != 0): 
				column_states.append(columns)
				terminal_states.append(columns)
			if (len(diagonals) != 0): 
				diagonal_states.append(diagonals)
				terminal_states.append(diagonals)
			if (len(diagonals2) != 0): 
				diagonal_states.append(diagonals2)
				terminal_states.append(diagonals2)

def is_terminal(player):
	full_board = True
	sign = None

	for state in terminal_states:
		sign = None
		for i in range(len(state)):
			cell = board[state[i][0]][state[i][1]]
			if(cell == '-'): full_board = False
			if (sign is None):
				sign = cell
				continue
			else:
				if (cell != sign): break
				elif (i != len(state)-1): continue

			return 1 if sign == player else -1

	if (full_board): return 0

def ALPHA_BETA_SEARCH(player, board): # returns an action
	alpha = float('-inf')
	beta = float('inf')
	v = float('-inf')
	bestScore = float('-inf')
	bestMove = None
	moves = get_moves(board) # game.moves
	get_teminal_states(len(board), 3)

    # find best action
	for move in moves:
		board[move[0]][move[1]] = player
		v = max(v, MIN_VALUE(switch_player(player), board, alpha, beta))
		board[move[0]][move[1]] = '-'
		if (v > bestScore):
			bestScore = v
			bestMove = move

	return bestMove

def MAX_VALUE(player, board, alpha, beta): # returns
	#print(board)
	terminal = is_terminal(my_player())
	if (terminal is not None): return terminal

	v = float('-inf')
	moves = get_moves(board) # game.moves

    # find maximum value
	for move in moves:
		board[move[0]][move[1]] = player
		v = max(v, MIN_VALUE(switch_player(player), board, alpha, beta))
		board[move[0]][move[1]] = '-'
		if v >= beta: return v
		alpha = max(alpha, v)

	return v

def MIN_VALUE(player, board, alpha, beta): # returns
	#print(board)
	terminal = is_terminal(my_player())
	if (terminal is not None): return terminal

	v = float('inf')
	moves = get_moves(board) # game.moves

    # find minimum value
	for move in moves:
		board[move[0]][move[1]] = player
		v = min(v, MAX_VALUE(switch_player(player), board, alpha, beta))
		board[move[0]][move[1]] = '-'
		if v <= alpha: return v
		beta = min(beta, v)

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

board = [['-','-','-'],
		['-','-','-'],
		['-','-','-']]

board = [['X','O'],
		['-','-']]

board = [['X','O','O'],
		['O','O','-'],
		['X','-','-']]

# board = [['X','X','O'],
# 		['O','O','X'],
# 		['X','O','X']]

board = [['-' for x in range(12)] for x in range(12)]
print(board)
this_player = 'X'
print(ALPHA_BETA_SEARCH(this_player, board))