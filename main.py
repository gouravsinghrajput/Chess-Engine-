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


def draw_board():
    