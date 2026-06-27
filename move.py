from main import main
from board import Board
from board import Position
import pygame as pg 

DIMENSIONS = 8 
WIDTH = HEIGHT = 512 
SQ_SIZE = WIDTH // DIMENSIONS 

board = Board()

main()

selected_piece = None
piece_position = None 

for event in pg.event.get():

    if event.type == pg.MOUSEBUTTONDOWN:

        x, y = pg.mouse.get_pos()

        row = x // SQ_SIZE
        col = y // SQ_SIZE

        # square = (row, col)

        if selected_piece is None:

            selected_piece = board[row][col]

            piece_position = (row, col)


        else:

            new_position = (row, col)

            board[piece_position[0]][piece_position[1]] = "--"

            board[new_position[0]][new_position[1]] = selected_piece

            selected_piece = None 
            piece_position = None


