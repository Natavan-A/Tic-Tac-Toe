def switch_player(player):
	if (player == 'X'): return 'O'
	else: return 'X'

def get_moves(board):
	empy_spots = [] # a list to store moves
	n = len(board) 	# game.board

	# for loops can be removed if board class exists!!!
	for i in range(n):
		for j in range(n):
			if (board[i][j] == '-'): empy_spots.append((i,j))

	return empy_spots

def is_terminal(player, board, winning_states):
	full_board = True
	sign = None

	# CHECK FOR WINNING FOR EACH OF THE TERMINAL STATES
	for state in winning_states:
		sign = None
		for i in range(len(state)):
			cell = board[state[i][0]][state[i][1]]
			if(full_board and cell == '-'): full_board = False
			if (sign is None):
				sign = cell
				continue
			else:
				if (cell != sign): break
				elif (i != len(state)-1): continue

			# WHEN REACHED TO THE END AND ALL SIGNS ARE EQUAL
			#	DETERMINE WHO WINS AND RETURN A VALUE ACCORDINGLY WIN/LOSE
			if (sign == player):
				return 1
			elif (sign == switch_player(player)):
				return -1

	# IF NOONE WINS AND BOARD IS FULL
	#	RETURN TIE
	if (full_board): return 0

def ALPHA_BETA_SEARCH(current_player, board, winning_states): # returns an action
	alpha = float('-inf')
	beta = float('inf')
	utility = float('-inf')
	bestScore = float('-inf')
	bestMove = None
	moves = get_moves(board) # game.moves

    # find best action
	for move in moves:
		board[move[0]][move[1]] = current_player
		utility = max(utility, MIN_VALUE(current_player, switch_player(current_player), board, winning_states, alpha, beta))
		board[move[0]][move[1]] = '-'
		if (utility > bestScore):
			bestScore = utility
			bestMove = move

	return bestMove

def MAX_VALUE(my_player, current_player, board, winning_states, alpha, beta):
	terminal = is_terminal(my_player, board, winning_states)
	if (terminal is not None): return terminal

	utility = float('-inf')
	moves = get_moves(board) # game.moves

    # find maximum value
	for move in moves:
		board[move[0]][move[1]] = current_player
		utility = max(utility, MIN_VALUE(my_player, switch_player(current_player), board, winning_states, alpha, beta))
		board[move[0]][move[1]] = '-'
		if utility >= beta: return utility
		alpha = max(alpha, utility)

	return utility

def MIN_VALUE(my_player, current_player, board, winning_states, alpha, beta):
	terminal = is_terminal(my_player, board, winning_states)
	if (terminal is not None): return terminal

	utility = float('inf')
	moves = get_moves(board) # game.moves

    # find minimum value
	for move in moves:
		board[move[0]][move[1]] = current_player
		utility = min(utility, MAX_VALUE(my_player, switch_player(current_player), board, winning_states, alpha, beta))
		board[move[0]][move[1]] = '-'
		if utility <= alpha: return utility
		beta = min(beta, utility)

	return utility

# game part:::: will be removed
# board = [['-' for x in range(3)] for x in range(3)]
# board = [['X','O','X'],
# 		['X','O','O'],
# 		['O','X','X']]

# board = [['X','O','X'],
# 		['O','O','O'],
# 		['O','X','X']]

# board = [['X','O','X'],
# 		['O','O','X'],
# 		['O','X','X']]

# board = [['O','O','X'],
# 		['O','X','O'],
# 		['X','O','X']]

# board = [['-','-','-'],
# 		['-','-','-'],
# 		['-','-','-']]

# board = [['X','O'],
# 		['-','-']]

# board = [['X','O','O'],
# 		['O','O','-'],
# 		['X','-','-']]

# board = [['X','X','O'],
# 		['O','O','X'],
# 		['X','O','X']]

# board = [['-' for x in range(12)] for x in range(12)]
# print(board)
# this_player = 'X'
# print(ALPHA_BETA_SEARCH(this_player, board))