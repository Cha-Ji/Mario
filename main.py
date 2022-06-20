import pygame
from pygame.rect import *
import time

from model.player import Player
from model.rec_player import RectPlayer
from model.star import Star
from model.missile import Missile

from model.joystick import Joystick
import RPi.GPIO as GPIO

# init global parameter
isActive = True
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
move = Rect(0,0,0,0)
score = 0

swt_channel, vrx_channel, vry_channel = 0, 1, 2
SWITCH = 21

joystick = Joystick()
player = Player(pygame).player
star = Star().createStar(pygame)
missile = Missile().createMissile(pygame)

rectObject = RectPlayer(player.get_rect(), star, missile, (SCREEN_WIDTH, SCREEN_HEIGHT))

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
    rectObject.recStar.restart()

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
        rectObject.makeMissile()


def moveObject(SCREEN):
    global score

    vrx_pos, vry_pos, swt_val = get_read_channels()
    eventProcess(vrx_pos, vry_pos, swt_val)
    rectObject.movePlayer(move)
    SCREEN.blit(player, rectObject.recPlayer)

    rectObject.moveStar()
    for i in range(len(star)):
        SCREEN.blit(star[i], rectObject.recStar[i])

    rectObject.moveMissile()
    for i in range(len(missile)):
        SCREEN.blit(missile[i], rectObject.recMissile[i])

    rectObject.isGameOver = rectObject.isCollision()
    rectObject.isCollisionMissile()
    score += 1

if __name__ == "__main__":
    set_gpio()
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while isActive and not rectObject.isGameOver:
        SCREEN.fill((0,0,0))
        moveObject(SCREEN)

        pygame.display.flip()
        clock.tick(100)

