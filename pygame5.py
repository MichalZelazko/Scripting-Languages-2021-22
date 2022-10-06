import pygame
import os
import sys

black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()
pygame.key.set_repeat(10, 10)

scr = pygame.display.set_mode((500, 500))
win = scr.get_rect()

box1 = pygame.Rect(0, 0, 50, 50)
box1.center = win.center
box2 = pygame.Rect(0,0,10,60)
box2.midleft = win.midleft

vec = [1, -2]
fps = pygame.time.Clock()
step = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                box2 = box2.move(0, -step)
            if event.key == pygame.K_DOWN:
                box2 = box2.move(0, step)

    box1 = box1.move(vec)
    if not win.contains(box1):
        vec[0] = -vec[0]
        vec[1] = -vec[1]
    if box1.colliderect(box2):
        vec[0] = -vec[0]
        vec[1] = -vec[1]

    scr.fill(black)
    pygame.draw.rect(scr,white,box1)
    pygame.draw.rect(scr,white,box2)
    pygame.display.flip()

    fps.tick(260)
