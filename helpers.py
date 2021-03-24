# RETURN THE SIGN OF THE OTHER PLAYER
def switch_player(player):
	if (player == 'X'): return 'O'
	else: return 'X'

# GET AVAILABLE MOVES ON THE BOARD
def get_moves(matrix):
	empy_spots = [] # a list to store moves
	n = len(matrix)

	for i in range(n):
		for j in range(n):
			if (matrix[i][j] == '-'): empy_spots.append((i,j))

	return empy_spots

# RETURN APPROPRIATE VALUE (1,-1,0) BASED ON THE BOARD STATE
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

	# BASED ON THE SIGNS ON THE BOARD DETERMINE WHICH PLAYER IS IN FAVOR
	if (X_lines > O_lines):
		return 1 if player == "X" else -1
	elif (X_lines < O_lines):
		return 1 if player == "O" else -1
	else: return 0

# RETURN A VALUE CONSIDERING THE DEPTH OF THE GAME TREE, IF THE GAME IS OVER
def is_terminal(player, board, matrix, moves_amount, winning_states, level):
	sign = None

	# CHECK IF BOARD IS FULL
	full_board = board.get_all_cells() == moves_amount

	# CHECK FOR WINNING FOR EACH OF THE TERMINAL STATES
	for state in winning_states:
		sign = None
		for i in range(len(state)):
			cell = matrix[state[i][0]][state[i][1]]

			if (cell == '-'): break
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

# RETURN THE BEST ACTION FOR THE PLAYER IN THE CURRENT STATE OF THE BOARD
def ALPHA_BETA_SEARCH(current_player, board, winning_states):
	matrix = board.get_matrix()					# board of the current game
	moves = get_moves(matrix)					# available moves on the board
	alpha = float('-inf')						# initial alpha value for pruning
	beta = float('inf')							# initial beta value for pruning
	bestScore = float('-inf')					# the best utility value among every move
	bestMove = moves[0]							# the best move/action among every move
	moves_amount = board.get_filled_cells()+1	# amount of played actions on the board
	moves_heuristic = {}						# a dictionary to store information about actions
	max_depth = board.get_max_depth()			# the maximum number of levels in the tree before running out of time
	level = 1									# current level in the tree

    # FIND THE BEST ACTION
	for move in moves:
		# PLAY THE MOVE
		moves_heuristic[move] = 0
		matrix[move[0]][move[1]] = current_player
		utility = MINIMAX_VALUE(False, current_player, switch_player(current_player),
								board, matrix, moves_amount, moves_heuristic, move, winning_states, alpha, beta, level, max_depth)
		# UNPLAY THE MOVE
		matrix[move[0]][move[1]] = '-'

		# IF CURRENTLY THE BEST MOVE, SAVE IT
		if ( utility > bestScore or (utility == bestScore and moves_heuristic[move] > moves_heuristic[bestMove]) ):
			bestScore = utility
			bestMove = move

	return bestMove

# RETURN UTILITY VALUE FOR THE STATE
def MINIMAX_VALUE(is_max, my_player, current_player, board, matrix, moves_amount, moves_heuristic, my_move, winning_states, alpha, beta, level, max_depth):
	# CHECK IF THE GAME IS OVER - WIN/LOSE/TIE
	terminal = is_terminal(my_player, board, matrix, moves_amount, winning_states, level)
	if (terminal is not None):
		moves_heuristic[my_move] += terminal
		return terminal

	# CHECK IF THE GAME REACHED THE MAXIMUM LEVEL IN THE TREE
	if (level == max_depth):
		eval_v = evaluation(current_player, matrix, winning_states)
		moves_heuristic[my_move] += eval_v
		return eval_v

	level += 1
	moves_amount += 1
	moves = get_moves(matrix)

	if is_max:
	    # FIND MAXIMUM VALUE AMOING AVAILABLE MOVES
		utility = float('-inf')
		for move in moves:
			# PLAY THE MOVE
			matrix[move[0]][move[1]] = current_player
			utility = max(utility, MINIMAX_VALUE(False, my_player, switch_player(current_player), 
												board, matrix, moves_amount, moves_heuristic, my_move, winning_states, alpha, beta, level, max_depth))
			# UNPLAY THE MOVE
			matrix[move[0]][move[1]] = '-'
			# PRUNING
			if utility >= beta: return utility
			alpha = max(alpha, utility)
	else:
		# FIND MINIMUM VALUE AMOING AVAILABLE MOVES
		utility = float('inf')
		for move in moves:
			# PLAY THE MOVE
			matrix[move[0]][move[1]] = current_player
			utility = min(utility, MINIMAX_VALUE(True, my_player, switch_player(current_player),
												board, matrix, moves_amount, moves_heuristic, my_move, winning_states, alpha, beta, level, max_depth))
			# UNPLAY THE MOVE
			matrix[move[0]][move[1]] = '-'
			# PRUNING
			if utility <= alpha: return utility
			beta = min(beta, utility)

	# RETURN UTILITY VALUE
	return utility