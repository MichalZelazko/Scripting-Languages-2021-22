import pygame
import os
import sys

black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()
pygame.key.set_repeat(10, 10)

scr = pygame.display.set_mode((500, 500))
win = scr.get_rect()

box = pygame.Rect(0, 0, 50, 50)
box.center = win.center

vec = [3, 5]
fps = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    box = box.move(vec)
    if box.left < win.left or box.right > win.right:
        vec[0] = -vec[0]
    if box.bottom > win.bottom or box.top < win.top:
        vec[1] = -vec[1]

    scr.fill(black)
    pygame.draw.rect(scr, white, box)
    pygame.display.flip()

    fps.tick(60)
