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
			return 1 if sign == player else -1

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

board = [['O','O','-', '-', '-'],
		['X','-','-', '-', '-'],
		['-','-','-', '-', '-'],
		['X','-', '-', '-', '-'],
		['X','-', '-', '-', '-']]
n = 3
t = 3
overall_X = 0
overall_O = 0

for i in range(n):
	for j in range(n-t+1):
		print('max:', i, 'max:', j)
		# Row-based evaluation
		rx = False
		ro = False
		rempty = False

		# Column-based evaluation
		cx = False
		co = False
		cempty = False


		# Row-based evaluation writing to overall value
		for jj in range(j, j+t):
			print("positions:", i, j, jj, board[i][jj])
			if (board[i][jj] == '-'): rempty = True
			if (board[i][jj] == 'X'): rx = True
			if (board[i][jj] == 'O'): ro = True
			print('netice :', rx, ro, rempty)
		# print("beraber:", jj, j+t-1)

		if (rx == True and ro == False): overall_X = overall_X + 1
		if (ro == True and rx == False): overall_O = overall_O + 1
		if (ro == False and rx == False and rempty):
			overall_X = overall_X + 1
			overall_O = overall_O + 1


		# Column-based evaluation writing to overall value
		for jj in range(j, j+t):
			# print("positions:", i, j, jj, board[i][jj])
			print("positions:", jj,i,  board[jj][i])

			if (board[jj][i] == '-'): cempty = True
			if (board[jj][i] == 'X'): cx = True
			if (board[jj][i] == 'O'): co = True
			print('netice :', cx, co, cempty)

		if (cx == True and co == False): overall_X = overall_X + 1
		if (co == True and cx == False): overall_O = overall_O + 1
		if (co == False and cx == False and cempty):
			overall_X = overall_X + 1
			overall_O = overall_O + 1


		# 	if(board[i][jj] == '-'): rempty = True
		# 	if(board[i][jj] == 'X'): rx = True
		# 	if(board[i][jj] == 'O'): ro = True
		# 	print('netice :', rx, ro, rempty)
		#
		# 	# print("beraber:", jj, j+t-1)
		#
		# if (rx == True and ro == False): overall_X = overall_X + 1
		# if (ro == True and rx == False): overall_O = overall_O + 1
		# if (ro == False and rx == False and rempty):
		# 	overall_X = overall_X + 1
		# 	overall_O = overall_O + 1



print("cavab:", overall_X, overall_O)

# for i in range (n-t+1):
# 	for j in range(n):
# 		print('max:', i, 'max:', j)
# 		x = False
# 		o = False
# 		empty = False
# 		for jj in range(j, j + t):
# 			print("positions:", i, j, jj, board[i][i])
# board = [['-' for x in range(12)] for x in range(12)]
# print(board)
# this_player = 'X'
# print(ALPHA_BETA_SEARCH(this_player, board))