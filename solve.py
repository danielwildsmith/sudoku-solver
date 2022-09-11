# board = [
#     [0, 0, 9, 1, 3, 0, 6, 0, 0],
#     [0, 0, 2, 5, 9, 0, 0, 0, 0],
#     [0, 5, 8, 0, 6, 0, 2, 0, 0],
#     [1, 0, 0, 0, 0, 7, 0, 0, 6],
#     [0, 0, 0, 0, 0, 0, 0, 2, 0],
#     [0, 2, 0, 0, 0, 3, 0, 7, 9],
#     [4, 0, 0, 0, 0, 0, 9, 6, 0],
#     [0, 7, 0, 0, 0, 0, 0, 0, 5],
#     [9, 8, 1, 2, 0, 0, 0, 3, 7]
# ]

# solve 2D-array method (backtracking)
# def solve_board(_board):
#     test_space = find_empty_space(_board)
#     # base case: board is full (cannot find empty space)
#     if not test_space:
#         return True
#     else:
#         row = test_space[0]
#         col = test_space[1]
#
#     for i in range(1, 10):
#         if is_valid_move(_board, i, (row, col)):
#             _board[row][col] = i
#
#             # recursive step:
#             # if board is solved (full), return true and exit recursion
#             if solve_board(_board):
#                 return True
#
#             # set back to 0 and backtrack to loop iteration if the board can't be completed with that value
#             _board[row][col] = 0
#     # if no value works, backtrack to previous filled space
#     return False
    

# is_valid method
def is_valid_move(tile_board, value, pos):
    # is the same value in that row?
    for i in range(len(tile_board[0])):
        if value == tile_board[pos[0]][i].value and pos[1] != i:
            return False
   
    # that column?
    for i in range(len(tile_board)):
        if value == tile_board[i][pos[1]].value and pos[0] != i:
            return False
    
    # that 3x3 grid?
    # first, what grid is it in?
    grid_location = [int(pos[0] / 3), int(pos[1] / 3)]
    grid_topleft = [grid_location[0] * 3, grid_location[1] * 3]
    for i in range(grid_topleft[0], grid_topleft[0] + 3):
        for j in range(grid_topleft[1], grid_topleft[1] + 3):
            if tile_board[i][j].value == value and i != pos[0] and j != pos[1]:
                return False
    
    return True


# find_empty_space method
def find_empty_space(tile_board):
    for i in range(len(tile_board)):
        for j in range(len(tile_board[0])):
            if tile_board[i][j].value == 0:
                return i, j


def display_board(_board):
    for i in range(len(_board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - ')
        for j in range(len(_board[0])):
            if j % 3 == 0 and j != 0:
                print('| ', end='')
            
            if j == 8:
                print(_board[i][j].value)
            else:
                print(str(_board[i][j].value) + ' ', end='')

#
# display_board(board)
# print('---------------------------------------------')
# solve_board(board)
# display_board(board)
