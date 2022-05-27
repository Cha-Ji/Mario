from joystick import Joystick
import time
import pygame
from model.player import Player

### global parameter
swt_channel = 0
vrx_channel = 1
vry_channel = 2
DELAY = 0.5

color = [255, 255, 255]
size = [400, 300]
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()

joystick = Joystick()
player = Player()
field = Field()

pygame.init()

while True:
    clock.tick(10)
    screen.fill(color)
    vrx_pos, vry_pos, swt_val = get_read_channels()
    color = player.get_changed_color(vrx_pos, vry_pos, swt_val)
    set_directions(vrx_pos, vry_pos, swt_val)

    print("VRx : {} VRy: {} SW: {}".format(vrx_pos, vry_pos, swt_val))
    print("cur index: {}".format(field.cur_index))
    
    pygame.display.update()

def get_read_channels():
    return (joystick.readChannel(vrx_channel),
    joystick.readChannel(vry_channel),
    joystick.readChannel(swt_channel))
    
def set_directions(x, y, swt):
    if 0 <= y < 500:
        field.move_back(1)
    elif 500 <= y < 1000:
        field.move_front(2)
        
        

    
