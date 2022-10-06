import pygame
import sys

# colors for fonts and objects
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 120, 255)

pygame.init()
pygame.key.set_repeat(10, 10)
pygame.display.set_caption("Pong game - Michał Żelazko 242149 CS2")

# main window
win_width = 900
win_height = 600
scr = pygame.display.set_mode((win_width, win_height))
win = scr.get_rect()

# moving objects
ball = pygame.Rect(0, 0, 30, 30)
ball.center = win.center
box1 = pygame.Rect(0, 0, 10, 60)
box1.midleft = (win_width * 0.02, win_height * 0.5)
box2 = pygame.Rect(0, 0, 10, 60)
box2.midright = (win_width * 0.98, win_height * 0.5)

# movement variables
vec = [1, 1]
fps = pygame.time.Clock()
step = 3

# gamemode variables
score1 = 0
score2 = 0
lives = 3
players = 0
program_stage = 1


def gamemode_choice():
    '''Start screen where you can choose the game mode
    pressing 1 results in choosing single-player mode
    pressing 2 results in choosing multi-player mode
    Movement controls for both modes are also mentioned'''
    global players
    global program_stage
    global score1
    global score2
    global lives
    scr.fill(black)
    menufont = pygame.font.SysFont('impact', 48)
    smallmenufont = pygame.font.SysFont('impact', 20)
    menu_text = menufont.render("Select the number of players", True, white)
    menu_text_box = menu_text.get_rect()
    menu_text_box.midtop = (win.width * 0.5, win.height * 0.05)
    menu_text_single = menufont.render("Single player - press 1", True, blue)
    menu_text_single_box = menu_text_single.get_rect()
    menu_text_single_box.center = (win.width * 0.5, win.height * 0.4)
    menu_text_multi = menufont.render("Two players - press 2", True, red)
    menu_text_multi_box = menu_text_multi.get_rect()
    menu_text_multi_box.midbottom = (win.width * 0.5, win.height * 0.6)
    menu_text_instructions = \
        smallmenufont.render("Movement: Player 1 - W & S \
                 Player 2 - Up & Down Arrows", True, white)
    menu_text_instructions_box = menu_text_instructions.get_rect()
    menu_text_instructions_box.midbottom = (win.width * 0.5, win.height * 0.9)

    scr.blit(menu_text, menu_text_box)
    scr.blit(menu_text_single, menu_text_single_box)
    scr.blit(menu_text_multi, menu_text_multi_box)
    scr.blit(menu_text_instructions, menu_text_instructions_box)

    key = pygame.key.get_pressed()
    if key[pygame.K_1]:
        players = 1
        program_stage = 2
    if key[pygame.K_2]:
        players = 2
        program_stage = 2


def difficulty_choice():
    '''Screen where you can choose the game difficulty
    The level of difficulty is based on the velocities
    of movement of the ball and the player box'''
    global vec
    global step
    global program_stage

    scr.fill(black)

    difficultyfont = pygame.font.SysFont('impact', 48)
    difficulty_text = \
        difficultyfont.render("Select the number of players", True, white)
    difficulty_text_box = difficulty_text.get_rect()
    difficulty_text_box.midtop = (win.width * 0.5, win.height * 0.05)

    difficulty_text_easy = \
        difficultyfont.render("Easy - press E", True, green)
    difficulty_text_easy_box = difficulty_text_easy.get_rect()
    difficulty_text_easy_box.center = (win.width * 0.5, win.height * 0.4)

    difficulty_text_normal = \
        difficultyfont.render("Normal - press N", True, blue)
    difficulty_text_normal_box = difficulty_text_normal.get_rect()
    difficulty_text_normal_box.center = (win.width * 0.5, win.height * 0.6)

    difficulty_text_hard = difficultyfont.render("Hard - press H", True, red)
    difficulty_text_hard_box = difficulty_text_hard.get_rect()
    difficulty_text_hard_box.center = (win.width * 0.5, win.height * 0.8)

    scr.blit(difficulty_text, difficulty_text_box)
    scr.blit(difficulty_text_easy, difficulty_text_easy_box)
    scr.blit(difficulty_text_normal, difficulty_text_normal_box)
    scr.blit(difficulty_text_hard, difficulty_text_hard_box)

    key = pygame.key.get_pressed()
    if key[pygame.K_e]:
        vec = [1, 1]
        step = 3
        program_stage = 3
    if key[pygame.K_n]:
        vec = [3, 3]
        step = 5
        program_stage = 3
    if key[pygame.K_h]:
        vec = [5, 5]
        step = 7
        program_stage = 3


def endgame_screen():
    '''Screen showing:
    For single-player mode: the score
    For multi-player mode: the winner of the game
    And enabling to exit the game by clicking ESC
    '''
    global players
    global program_stage
    global score1
    global score2
    global lives
    scr.fill(black)
    endfont = pygame.font.SysFont('impact', 48)
    if lives == 0:
        end_text = \
            endfont.render("You lost. Your score: " + str(score1), True, white)
        end_text_box = end_text.get_rect()
        end_text_box.midtop = (win.width * 0.5, win.height * 0.05)
    elif score2 > score1:
        end_text = endfont.render("Player 2 won!", True, white)
        end_text_box = end_text.get_rect()
        end_text_box.midtop = (win.width * 0.5, win.height * 0.05)
    elif score1 > score2:
        end_text = endfont.render("Player 1 won!", True, white)
        end_text_box = end_text.get_rect()
        end_text_box.midtop = (win.width * 0.5, win.height * 0.05)
    end_text_replay = \
        endfont.render("Thank you for playing my game!", True, blue)
    end_text_replay_box = end_text_replay.get_rect()
    end_text_replay_box.center = (win.width * 0.5, win.height * 0.4)
    end_text_exit = endfont.render("Exit - press ESC", True, red)
    end_text_exit_box = end_text_exit.get_rect()
    end_text_exit_box.midbottom = (win.width * 0.5, win.height * 0.6)

    scr.blit(end_text, end_text_box)
    scr.blit(end_text_replay, end_text_replay_box)
    scr.blit(end_text_exit, end_text_exit_box)

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        program_stage = 5


def multiplayer():
    '''Game mode for 2 players playing against each other
    Players score by hitting the wall behind the opponent's box'''
    global box1
    global box2
    global ball
    global score1
    global score2
    global program_stage
    scr.fill(black)
    pygame.draw.rect(scr, white, box1)
    pygame.draw.rect(scr, white, box2)
    pygame.draw.rect(scr, white, ball)

    scorefont = pygame.font.SysFont('impact', 48)
    score_text = \
        scorefont.render(str(score1) + " : " + str(score2), True, red)

    score_text_box = score_text.get_rect()
    score_text_box.midtop = (win.width * 0.5, win.height * 0.05)

    scr.blit(score_text, score_text_box)

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        box1 = box1.move(0, -step)
    if key[pygame.K_s]:
        box1 = box1.move(0, step)
    if box1.top < win.top:
        box1.top = win.top
    if box1.bottom > win.bottom:
        box1.bottom = win.bottom
    if key[pygame.K_UP]:
        box2 = box2.move(0, -step)
    if key[pygame.K_DOWN]:
        box2 = box2.move(0, step)
    if box2.top < win.top:
        box2.top = win.top
    if box2.bottom > win.bottom:
        box2.bottom = win.bottom

    ball = ball.move(vec)
    if ball.left < win.left:
        score2 += 1
        if score2 < 3:
            ball.center = win.center
            pygame.time.delay(500)
        else:
            program_stage = 4
    if ball.right > win.right:
        score1 += 1
        if score1 < 3:
            ball.center = win.center
            pygame.time.delay(500)
        else:
            program_stage = 4
    if ball.bottom > win.bottom or ball.top < win.top:
        vec[1] = -vec[1]
    if ball.left < box1.right and \
       abs(ball.centery - box1.centery) < (ball.h + box1.h)/2:
        vec[0] = -vec[0]
    if ball.right > box2.left and \
       abs(ball.centery - box2.centery) < (ball.h + box2.h)/2:
        vec[0] = -vec[0]


def singleplayer():
    '''Game mode for 1 player playing against the wall
    Player scores by hitting the wall opposite to his box'''
    global box1
    global ball
    global lives
    global program_stage
    global score1

    scr.fill(black)

    singlefont = pygame.font.SysFont('impact', 48)
    lives_text = singlefont.render("Lives: " + str(lives), True, red)
    lives_text_box = lives_text.get_rect()
    lives_text_box.midtop = (win.width * 0.5, win.height * 0.05)

    score_text = singlefont.render("Score: " + str(score1), True, green)
    score_text_box = score_text.get_rect()
    score_text_box.midtop = (win.width * 0.5, win.height * 0.9)

    scr.blit(lives_text, lives_text_box)
    scr.blit(score_text, score_text_box)
    pygame.draw.rect(scr, white, box1)
    pygame.draw.rect(scr, white, ball)

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        box1 = box1.move(0, -step)
    if key[pygame.K_s]:
        box1 = box1.move(0, step)
    if box1.top < win.top:
        box1.top = win.top
    if box1.bottom > win.bottom:
        box1.bottom = win.bottom

    ball = ball.move(vec)
    if ball.left < win.left:
        lives -= 1
        if lives > 0:
            ball.midright = (win_width * 0.98, win_height * 0.5)
            pygame.time.delay(500)
        else:
            program_stage = 4

    if ball.right > win.right:
        vec[0] = -vec[0]
        score1 += 1
    if ball.bottom > win.bottom or ball.top < win.top:
        vec[1] = -vec[1]
    if ball.left < box1.right and \
       abs(ball.centery-box1.centery) < (ball.h+box1.h)/2:
        vec[0] = -vec[0]


def main():
    '''Main function executing the program'''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if program_stage == 1:
            gamemode_choice()
        if program_stage == 2:
            difficulty_choice()
        if program_stage == 3:
            if players == 1:
                singleplayer()
            elif players == 2:
                multiplayer()
        if program_stage == 4:
            endgame_screen()
        if program_stage == 5:
            sys.exit()
        pygame.display.flip()

        fps.tick(240)


if __name__ == "__main__":
    main()
