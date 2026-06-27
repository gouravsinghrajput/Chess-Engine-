#  this contains the main function 

import pygame as pg 
import numpy as np 
from board import Board 

WIDTH = HEIGHT = 512
DIMENSIONS = 8 
SQ_SIZE = WIDTH // DIMENSIONS 

IMAGES = {}

def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = pg.image.load(f"images/{piece}.png")
        IMAGES[piece] = pg.transform.scale(IMAGES[piece], (SQ_SIZE, SQ_SIZE))


def draw_board(screen):
    colors = [pg.Color("white"), pg.Color("dark gray")]

    for row in range(8):
        for col in range(8):

            color = colors[(row + col) % 2]

            pg.draw.rect(
                screen,  
                color,
                (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
            )

def draw_pieces(screen, board):
    
    for row in range(8):
        for col in range(8):

            piece = board[row][col]

            if piece != "--":

                screen.blit(
                    IMAGES[piece],
                    col * SQ_SIZE, row * SQ_SIZE
                )

                
    