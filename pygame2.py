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

step = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                box = box.move(-step, 0)
            if event.key == pygame.K_RIGHT:
                box = box.move(step, 0)
            if event.key == pygame.K_UP:
                box = box.move(0, -step)
            if event.key == pygame.K_DOWN:
                box = box.move(0, step)
    if box.left < win.left:
        box.left = win.left
    if box.top < win.top:
        box.top = win.top
    if box.right > win.right:
        box.right = win.right
    if box.bottom > win.bottom:
        box.bottom = win.bottom
    scr.fill(black)
    pygame.draw.rect(scr, white, box)
    pygame.display.flip()
