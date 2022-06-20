import pygame
from pygame.rect import *
import time

from player import Player
from rec_player import RectPlayer
from star import Star

from joystick import Joystick
import RPi.GPIO as GPIO

# init global parameter
isActive = True
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
move = Rect(0,0,0,0)
time_dealy_4sec = 0
toggle = False
score = 0
IMG_PATH = "img/"

swt_channel = 0
vrx_channel = 1
vry_channel = 2
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
    global score
    score = 0
    recStar.restart()

def eventProcess(x, y, swt):
    #pygame.quit()

    if 0 <= x < 500:
        move.x = -1
    elif 500 <= x < 520:
        move.x = 0
    else:
        move.x = 1

    if 0 <= y < 500:
        move.y = -1
    elif 500 <= y < 520:
        move.y = 0
    else:
        move.y = 1

    if GPIO.input(SWITCH) == 0:
        restart()


player = Player(pygame).player

star = Star().createStar(pygame)

rectObject = RectPlayer(player.get_rect(), star, (SCREEN_WIDTH, SCREEN_HEIGHT))
recPlayer = rectObject.recPlayer
recStar = rectObject.recStar

if __name__ == "__main__":
    set_gpio()
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while isActive and not rectObject.isGameOver:
        # set gpio
        vrx_pos, vry_pos, swt_val = get_read_channels()

        SCREEN.fill((0,0,0))

        eventProcess(vrx_pos, vry_pos, swt_val)
        rectObject.movePlayer(move)
        SCREEN.blit(player, recPlayer)

        rectObject.moveStar()
        for i in range(len(star)):
            SCREEN.blit(star[i], rectObject.recStar[i])

        rectObject.isGameOver = rectObject.isCollision()
        score += 1

        pygame.display.flip()
        clock.tick(100)

        print("x : {} y : {} sw : {}".format(vrx_pos, vry_pos, swt_val))
 
