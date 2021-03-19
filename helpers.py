def switch_player(player):
	if (player == 'X'): return 'O'
	else: return 'X'

def get_moves(matrix):
	empy_spots = [] # a list to store moves
	n = len(matrix) 	# game.board

	# for loops can be removed if board class exists!!!
	for i in range(n):
		for j in range(n):
			if (matrix[i][j] == '-'): empy_spots.append((i,j))

	return empy_spots

def evaluation(player, matrix, winning_states):
	X_lines = 0
	O_lines = 0
	target = len(winning_states[0])

	for state in winning_states:
		overall_X = 0
		overall_O = 0
		overall_E = 0

		# CALCULATE AMOUNT OF X, O AND EMPTY SPOTS
		for i in range(target):
			cell = matrix[state[i][0]][state[i][1]]
			if (cell == 'X'): overall_X += 1
			elif (cell == 'O'): overall_O += 1
			else: overall_E += 1

		if (overall_E > 0):
			points = target - overall_E
			if (overall_X > 0 and overall_O == 0):
				if points > 1: points *=(target**(overall_X-1))
				X_lines += points
			elif (overall_O > 0 and overall_X == 0):
				if points > 1: points *=(target**(overall_O-1))
				O_lines += points

	if (X_lines > O_lines):
		return float('inf') if player == "X" else float('-inf')
	elif (X_lines < O_lines):
		return float('inf') if player == "O" else float('-inf')
	else: return 0

def is_terminal(player, board, matrix, winning_states, level):
	sign = None

	# CHECK IF BOARD IS FULL
	full_board = board.is_full()

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
			#	DETERMINE WHO WINS AND RETURN A VALUE ACCORDINGLY WIN/LOSE
			if (sign == player):
				return 10 - level
			elif (sign == switch_player(player)):
				return level - 10

	# IF NOONE WINS AND BOARD IS FULL
	#	RETURN TIE
	if (full_board): return 0

def ALPHA_BETA_SEARCH(current_player, board, winning_states): # returns an action
	matrix = board.get_matrix()
	moves = get_moves(matrix) # game.moves
	alpha = float('-inf')
	beta = float('inf')
	bestScore = float('-inf')
	bestMove = moves[0]
	level = 1
	max_depth = 8

    # find best action
	for move in moves:
		matrix[move[0]][move[1]] = current_player
		utility = MIN_VALUE(current_player, switch_player(current_player),
								board, matrix, winning_states, alpha, beta, level, max_depth)
		matrix[move[0]][move[1]] = '-'
		if (utility > bestScore):
			bestScore = utility
			bestMove = move

	return bestMove

def MAX_VALUE(my_player, current_player, board, matrix, winning_states, alpha, beta, level, max_depth):
	terminal = is_terminal(my_player, board, matrix, winning_states, level)
	if (terminal is not None): return terminal
	if (level == max_depth): return evaluation(current_player, matrix, winning_states)

	utility = float('-inf')
	moves = get_moves(matrix) # game.moves
	level += 1

    # find maximum value
	for move in moves:
		matrix[move[0]][move[1]] = current_player
		utility = max(utility, MIN_VALUE(my_player, switch_player(current_player), 
											board, matrix, winning_states, alpha, beta, level, max_depth))
		matrix[move[0]][move[1]] = '-'
		if utility >= beta: return utility
		alpha = max(alpha, utility)

	return utility

def MIN_VALUE(my_player, current_player, board, matrix, winning_states, alpha, beta, level, max_depth):
	terminal = is_terminal(my_player, board, matrix, winning_states, level)
	if (terminal is not None): return terminal
	if (level == max_depth): return evaluation(current_player, matrix, winning_states)

	utility = float('inf')
	moves = get_moves(matrix) # game.moves
	level += 1

    # find minimum value
	for move in moves:
		matrix[move[0]][move[1]] = current_player
		utility = min(utility, MAX_VALUE(my_player, switch_player(current_player),
											board, matrix, winning_states, alpha, beta, level, max_depth))
		matrix[move[0]][move[1]] = '-'
		if utility <= alpha: return utility
		beta = min(beta, utility)

	return utility