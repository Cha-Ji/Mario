from joystick import Joystick
from model.player import Player
from model.field import Field

import time
import pygame
import RPi.GPIO as GPIO

### global parameter
swt_channel = 0
vrx_channel = 1
vry_channel = 2
SWITCH = 27
DELAY = 0.5

color = [255, 255, 255]
size = [400, 300]
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()
boost_count = 0

joystick = Joystick()
player = Player()
field = Field()

def set_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(SWITCH, GPIO.IN, GPIO.PUD_UP)

def get_read_channels():
    return (joystick.readChannel(vrx_channel),
    joystick.readChannel(vry_channel),
    joystick.readChannel(swt_channel))
    
def set_directions(x, y, swt):
    if boost_count > 0:
        distance = 2
        boost_count -= 1
    else:
        distance = 1

    if 0 <= y < 500:
        field.move_back(1)
    elif 500 <= y < 1000:
        field.move_front(1 + distance)

    if 0 <= x < 500:
        field.turn_left(1)
    elif 500 <= x < 1000:
        field.turn_right(1)

def set_boost():
    boost_count = 5
    return
 
if __name__ == "__main__":
    set_gpio()
    pygame.init()

    while True:
        # set pygame
        clock.tick(10)
        screen.fill(color)

        # set gpio
        vrx_pos, vry_pos, swt_val = get_read_channels()
        switch = GPIO.input(switch)

        # run
        color = player.get_changed_color(vrx_pos, vry_pos, swt_val)
        set_directions(vrx_pos, vry_pos, swt_val)

        if GPIO.input(switch) == 0:
            set_boost()

        print("VRx : {} VRy: {} SW: {}".format(vrx_pos, vry_pos, swt_val))
        print("cur index: {}".format(field.cur_index))
        
        print("boost: {}".format(boost_count))
        pygame.display.update()
    
