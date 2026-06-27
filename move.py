from main import main
from board import Board
from board import Position
import pygame as pg 

DIMENSIONS = 8 
WIDTH = HEIGHT = 512 
SQ_SIZE = WIDTH // DIMENSIONS 

x, y = pg.mouse.get_pos()

row = x // SQ_SIZE
col = y // SQ_SIZE

square = (row, col)

