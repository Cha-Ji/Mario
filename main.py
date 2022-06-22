import pygame
import RPi.GPIO as GPIO
from controller import Controller

# init global parameter
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
swt_channel, vrx_channel, vry_channel = 0, 1, 2
SWITCH = 21


def set_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(SWITCH, GPIO.IN, GPIO.PUD_UP)


if __name__ == "__main__":
    set_gpio()
    pygame.init()
    clock = pygame.time.Clock()
    controller = Controller()

    while not controller.isGameOver:
        controller.move_object()
        pygame.display.flip()
        clock.tick(100)
