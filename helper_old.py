terminal_states = []
row_states = []
column_states = []
diagonal_states = []

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

			# STORING STATES TO GLOBAL LISTS
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

def is_terminal(player, level):
	full_board = True
	sign = None

	for i in range(len(board)):
		for j in range(len(board)):
			if (board[i][j] == '-'):
				full_board = False
				break
		if (full_board == False): break

	# CHECK FOR WINNING FOR EACH OF THE TERMINAL STATES
	for state in terminal_states:
		sign = None
		for i in range(len(state)):
			cell = board[state[i][0]][state[i][1]]

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
				return 10-level
			elif (sign == switch_player(player)):
				return level-10

	# IF NOONE WINS AND BOARD IS FULL
	#	RETURN TIE
	if (full_board): return 0

def evaluation(player):
	X_lines = 0
	O_lines = 0
	target = len(terminal_states[0])

	for state in terminal_states:
		overall_X = 0
		overall_O = 0
		overall_E = 0
		# print(state)
		for i in range(target):
			cell = board[state[i][0]][state[i][1]]
			if (cell == 'X'): overall_X += 1
			elif (cell == 'O'): overall_O += 1
			else: overall_E += 1

		if (overall_E > 0):
			points = target - overall_E
			if (overall_X > 0 and overall_O == 0):
				X_lines += points
			elif (overall_O > 0 and overall_X == 0):
				O_lines += points

	if (X_lines > O_lines):
		return 1 if player == "X" else -1
	elif (X_lines < O_lines):
		return 1 if player == "O" else -1
	else: return 0

def ALPHA_BETA_SEARCH(player, board): # returns an action
	alpha = float('-inf')
	beta = float('inf')
	bestScore = float('-inf')
	moves = get_moves(board) # game.moves
	bestMove = moves[0]
	level = 1

	moves_dict = {}

    # find best action
	# print(moves)
	global max_depth
	if(len(moves) <= 50): max_depth=3
	elif(len(moves) <= 25): max_depth=4
	elif(len(moves) <= 12): max_depth=5
	for move in moves:
		moves_dict[move] = 0
		board[move[0]][move[1]] = player
		v = MINIMAX_VALUE(False, switch_player(player), board, alpha, beta, moves_dict, move, level)
		# print("ALPHA_BETA_SEARCH "+str(move)+" "+str(v))
		# print(moves_dict)
		board[move[0]][move[1]] = '-'
		# if ( v > bestScore or (v == bestScore and moves_dict[move] > moves_dict[bestMove]) ):
		if ( v > bestScore ):
			bestScore = v
			bestMove = move

	return bestMove


def MINIMAX_VALUE(is_max, player, board, alpha, beta, moves_dict, my_move, level): # returns
	terminal = is_terminal(my_player(), level)
	if (terminal is not None):
		#moves_dict[my_move] = min(terminal, moves_dict[my_move])
		# print("max")
		# print(terminal, level)
		return terminal

	if (level == max_depth): return evaluation(player)
	moves = get_moves(board) # game.moves
	level += 1

	if is_max:
	    # find maximum value
		v = float('-inf')
		# print("MAX_Tries:", end=" ")
		# print(moves)
		for move in moves:
			board[move[0]][move[1]] = player
			v = max(v, MINIMAX_VALUE(False, switch_player(player), board, alpha, beta, moves_dict, my_move, level))

			#moves_dict[my_move] += min_v
			# print(v, move)
			board[move[0]][move[1]] = '-'
			if v >= beta: return v
			alpha = max(alpha, v)

		#print("MAX_VALUE "+str(v))
	else:
	    # find minimum value
		v = float('inf')
		# print("MIN_Tries:", end=" ")
		# print(moves)
		for move in moves:
			board[move[0]][move[1]] = player
			v = min(v, MINIMAX_VALUE(True, switch_player(player), board, alpha, beta, moves_dict, my_move, level))
			
			#moves_dict[my_move] += max_v
			# print(v, move)
			board[move[0]][move[1]] = '-'
			if v <= alpha: return v
			beta = min(beta, v)

	# print("lvl: {}, utility: {}".format(level, v))
	# print(v)
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

board = [['X','O'],
		['-','-']]

board = [['O','-','O', '-'],
		['O','X','-','-'],
		['X','-','-','-'],
		['-','-','-','-']]

board = [['O','O','X', '-'],
		['X','X','O','-'],
		['O','O','-','X'],
		['-','-','-','-']]


board = [['-','-','O','-','-'],
         ['-','X','-','-','-'],
         ['-','-','-','-','-'],
         ['-','-','-','-','-'],
         ['-','-','-','-','-']]

# board = [['X','X','O'],
# 		['O','O','X'],
# 		['X','-','-']]

# board = [['O','X','O'],
# 		['-','X','-'],
# 		['-','O','-']]

# board = [['X', '-', 'O'],
# 		['-', 'O', '-'],
# 		['-', '-', 'X']]


# board = [['-','-','-'],
# 		['-','-','-'],
# 		['-','-','-']]

# board = [['O', 'O', 'X'],
# 		['-', 'X', '-'],
# 		['O', '-', '-']]
# print(board)
size=5
max_depth = 6

print(board)
this_player = 'X'
get_teminal_states(len(board), 3)
print(len(terminal_states))
my_turn = True

while(is_terminal(this_player, 1) == None):
	if my_turn:
		this_player = switch_player(this_player)
		next_move = ALPHA_BETA_SEARCH(this_player, board)
		board[next_move[0]][next_move[1]] = this_player
		my_turn = False
	else:
		this_player = switch_player(this_player)
		next_move = ALPHA_BETA_SEARCH(this_player, board)
		board[next_move[0]][next_move[1]] = this_player
		my_turn = True
	print(board)
