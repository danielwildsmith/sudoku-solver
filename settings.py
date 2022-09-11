import pygame
import sys

WIDTH = 700
HEIGHT = 600
GRID_SIZE = 450
GRID_TOPLEFT = [125, 75]
GAME_FONT = 'joystix.ttf'

BOARD = [
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
BOARD_SIZE = len(BOARD)
TILE_SIZE = GRID_SIZE / BOARD_SIZE

BACKGROUND_COLOR = '#edf6f7'
SELECTED_COLOR = '#7ba7c9'


# # helper functions
# def convert_row_col_to_pos(row, col):
#     return (GRID_TOPLEFT[0] + TILE_SIZE * row) + TILE_SIZE / 2, (GRID_TOPLEFT[1] + TILE_SIZE * col) + TILE_SIZE / 2
