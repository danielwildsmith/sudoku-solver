board = [
	[0, 0, 9, 1, 3, 0, 6, 0, 0],
	[0, 0, 2, 5, 9, 0, 0, 0, 0],
	[0, 5, 8, 0, 6, 0, 2, 0, 0],
	[1, 0, 0, 0, 0, 7, 0, 0, 6],
	[0, 0, 0, 0, 0, 0, 0, 2, 0],
	[0, 2, 0, 0, 0, 3, 0, 7, 9],
	[4, 0, 0, 0, 0, 0, 9, 6, 0],
	[0, 7, 0, 0, 0, 0, 0, 0, 5],
	[9, 8, 1, 2, 0, 0, 0, 3, 7]
]


# solve method (backtracking)
# base case: board is full (cannot find empty space)


# is_valid method


# find_empty_space method


def display_board(_board):
	for i in range(len(_board)):
		if i % 3 == 0 and i != 0:
			print('- - - - - - - - - - - - ')
		for j in range(len(_board[0])):
			if j % 3 == 0:
				print('| ', end='')

			if j == 8:
				print(_board[i][j])
			else:
				print(str(_board[i][j]) + ' ', end='')


display_board(board)
