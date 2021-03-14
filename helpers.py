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

def is_terminal(player, board):
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
					#print("row found")
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
					#print("column found")
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
						if (board[i][j] != board[i-k][j+k] or i-k < 0): break;
					if (k == target - 1): win = True
				if (win):
					#print("diagonal found")
					if (board[i][j] == player): return 1
					else: return -1

	# TIE
	if (full_board and not win):
		#print("tie")
		return 0

def ALPHA_BETA_SEARCH(player, board): # returns an action
	alpha = float('-inf')
	beta = float('inf')
	v = float('-inf')
	bestScore = float('-inf')
	bestMove = None
	moves = get_moves(board) # game.moves

    # find best action
	for move in moves:
		board[move[0]][move[1]] = player
		v = max(v, MIN_VALUE(switch_player(player), board, alpha, beta))
		board[move[0]][move[1]] = '-'
		if (v > bestScore):
			bestScore = v
			bestMove = move

	print(bestScore)
	print(bestMove)

def MAX_VALUE(player, board, alpha, beta): # returns
	#print(board)
	terminal = is_terminal(my_player(), board)
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
	terminal = is_terminal(my_player(), board)
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
		['O','O','X'],
		['X','-','-']]

# board = [['X','X','O'],
# 		['O','O','X'],
# 		['X','O','X']]

#board = [['-' for x in range(4)] for x in range(4)]
print(board)
this_player = 'X'
ALPHA_BETA_SEARCH(this_player, board)