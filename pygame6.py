import pygame
import sys

black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
pygame.init()
scr = pygame.display.set_mode((600, 600))
win = scr.get_rect()

box = pygame.Rect(0, 0, 50, 50)
box.center = win.center

vec = [3, 5]
vec2 = [1, 2]
fps = pygame.time.Clock()

myfont = pygame.font.Font('freesansbold.ttf', 48)
msg = myfont.render("The Game !!!", True, red)

msg_box = msg.get_rect()
msg_box.center = win.center

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    msg_box = msg_box.move(vec2)
    if msg_box.left < win.left or msg_box.right > win.right:
        vec2[0] = -vec2[0]
    if msg_box.bottom > win.bottom or msg_box.top < win.top:
        vec2[1] = -vec2[1]
    box = box.move(vec)
    if box.left < win.left or box.right > win.right:
        vec[0] = -vec[0]
    if box.bottom > win.bottom or box.top < win.top:
        vec[1] = -vec[1]

    scr.fill(black)
    pygame.draw.rect(scr, white, box)
    scr.blit(msg, msg_box)

    pygame.display.flip()

    fps.tick(100)
