import pygame
import os
import sys
import random
import math
'''
#os.environ['SDL_VIDEO_WINDOW_POS']="100,100"
os.environ['SDL_VIDEO_WINDOW_POS']="center"
win = (900, 600)
white = pygame.Color("white")
pygame.init()
s = pygame.display.set_mode(win)
s.fill(white)
pygame.display.set_caption('Hello World!')
#pygame.display.set_mode(size,pygame.FULLSCREEN)
#pygame.display.set_mode(size,pygame.NOFRAME)

for i in range(300):
    rgb = random.randint(0, 0xFFFFFFFF)
    color = pygame.color.Color(rgb)

    size = (random.randint(10,50), random.randint(10,50))
    orig = (random.randint(0, win[0]), random.randint(0, win[1]))

    rect = (orig, size)
    pygame.draw.rect(s, color, rect)
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
            pygame.quit()
            sys.exit()'''

os.environ['SDL_VIDEO_WINDOW_POS']="center"
win = (500, 500)
white = pygame.Color("white")
pygame.init()
s = pygame.display.set_mode(win)
s.fill(white)
pygame.display.set_caption('Hello World!')
#pygame.display.set_mode(size,pygame.FULLSCREEN)
#pygame.display.set_mode(size,pygame.NOFRAME)

circles = []

for i in range(10):
    rgb = random.randint(0, 0xFFFFFFFF)
    color = pygame.color.Color(rgb)
    
    radius = (random.randint(5,40))
    x = random.randint(radius, win[0]-radius)
    y = random.randint(radius, win[1]-radius)
    orig = (x, y)

    collision = False

    for x0,y0,r0 in circles:
        d = math.sqrt((x0 - x)**2 + (y0 - y)**2)
        if (d < r0 + radius):
            collision = True
            break
    
    if not collision:
        pygame.draw.circle(s, color, orig, radius)
        pygame.display.flip()
        circles.append((x,y,radius))
        i += 1

while True:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
            pygame.quit()
            sys.exit()