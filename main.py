import pygame
import random
from pygame.rect import *
import time

from joystick import Joystick
import RPi.GPIO as GPIO

# init global parameter
isActive = True
isGameOver = False
toggle = False

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
move = Rect(0,0,0,0)
time_delay_500ms = 0
time_dealy_4sec = 0
score = 0
IMG_PATH = "img/"

swt_channel, vrx_channel, vry_channel = 0, 1, 2
SWITCH = 27
DELAY = 0.5

joystick = Joystick()

def set_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(SWITCH, GPIO.IN, GPIO.PUD_UP)

def get_read_channels():
    return (joystick.readChannel(vrx_channel),
    joystick.readChannel(vry_channel),
    joystick.readChannel(swt_channel))

def restart():
    global isGameOver, score

    isGameOver = False
    score = 0
    for i in range(len(star)):
        recStar[i].y = -1

def event_process(x, y, swt):
    #pygame.quit()
    move.x = -1 if 0 <= x < 500 else 1 if 520 < x else 0
    move.y = -1 if 0 <= y < 500 else 1 if 520 < y else 0

    if GPIO.input(SWITCH) == 0:
        restart()

def move_player():
    if not isGameOver:
        recPlayer.x += move.x
        recPlayer.y += move.y

    if recPlayer.x < 0:
        recPlayer.x = 0

    if recPlayer.x > SCREEN_WIDTH-recPlayer.width:
        recPlayer.x = SCREEN_WIDTH-recPlayer.width

    if recPlayer.y < 0:
        recPlayer.y = 0

    if recPlayer.y > SCREEN_HEIGHT-recPlayer.height:
        recPlayer.y = SCREEN_HEIGHT-recPlayer.height

    SCREEN.blit(player, recPlayer)

def time_delay500ms():
    global time_delay_500ms

    if time_delay_500ms > 5:
        time_delay_500ms = 0
        return True

    time_delay_500ms += 1
    return False

def make_star():
    if isGameOver:
        return

    if time_delay500ms():
        idex = random.randint(0, len(star)-1)
        if recStar[idex].y == -1:
            recStar[idex].x = random.randint(0, SCREEN_WIDTH)
            recStar[idex].y = 0

def move_star():
    make_star()

    for i in range(len(star)):
        if recStar[i].y == -1:
            continue

        if not isGameOver:
            recStar[i].y += 1

        if recStar[i].y > SCREEN_HEIGHT:
            recStar[i].y = 0

        SCREEN.blit(star[i], recStar[i])

def check_collision():
    global score, isGameOver

    if isGameOver:
        return

    for rec in recStar:
        if rec.y == -1:
            continue

        if rec.top < recPlayer.bottom and recPlayer.top < rec.bottom and rec.left < recPlayer.right and recPlayer.left < rec.right:
            print('충돌')
            isGameOver = True
            break

    score += 1

def blinking():
    global time_dealy_4sec, toggle

    time_dealy_4sec += 1
    if time_dealy_4sec > 40:
        time_dealy_4sec = 0
        toggle = ~toggle

    return toggle

def setText():
    mFont = pygame.font.SysFont("arial",20, True, False)
    SCREEN.blit(mFont.render(
        f'score : {score}', True, 'green'), (10, 10, 0, 0))

    if isGameOver and blinking():
        SCREEN.blit(mFont.render(
            'Game Over!!', True, 'red'), (150, 300, 0, 0))
        SCREEN.blit(mFont.render(
            'press R - Restart', True, 'red'), (140, 320, 0, 0))

player = pygame.image.load(IMG_PATH + 'player.png')
player = pygame.transform.scale(player,(20,30))
recPlayer = player.get_rect()
recPlayer.centerx = (SCREEN_WIDTH/2)
recPlayer.centery = (SCREEN_HEIGHT/2)

star = [pygame.image.load(IMG_PATH + 'star.png') for i in range(40)]
recStar = [None for i in range(len(star))]

for i in range(len(star)):
    star[i] = pygame.transform.scale(star[i], (20, 20))
    recStar[i] = star[i].get_rect()
    recStar[i].y = -1

if __name__ == "__main__":
    set_gpio()
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # TODO: lcd screen

    while isActive:
        # set gpio
        vrx_pos, vry_pos, swt_val = get_read_channels()

        SCREEN.fill((0,0,0))
        event_process(vrx_pos, vry_pos, swt_val)
        move_player()
        move_star()
        check_collision()
        #setText()
        pygame.display.flip()
        clock.tick(100)

        print("x : {} y : {} sw : {}".format(vrx_pos, vry_pos, swt_val))

