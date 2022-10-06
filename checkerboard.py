import pygame
import sys
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "center"

board = (500, 500)
grid = (8, 8)
tile = (board[0]/grid[0], board[1]/grid[1])

black = pygame.Color(0, 0, 0)
white = pygame.Color("white")


def draw_board(board, grid, tile):
    s = pygame.display.set_mode(board)
    s.fill(black)
    for i in range(grid[0]):
        for j in range(grid[1]):
            if j % 2 == 0:
                if i % 2 == 0:
                    orig = (i*tile[0], j*tile[1])
                    square = (orig, tile)
                    pygame.draw.rect(s, white, square)
            else:
                if i % 2 == 1:
                    orig = (i*tile[0], j*tile[1])
                    square = (orig, tile)
                    pygame.draw.rect(s, white, square)


pygame.init()

s = pygame.display.set_mode(board)
draw_board(board, grid, tile)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
            pygame.quit()
            sys.exit()
