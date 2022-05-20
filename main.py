from joystick import Joystick
import time
import pygame

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
pygame.init()

while True:
    clock.tick(10)
    screen.fill(color)
    vrx_pos = joystick.readChannel(vrx_channel)
    vry_pos = joystick.readChannel(vry_channel)
    swt_val = joystick.readChannel(swt_channel)

    print("VRx : {} VRy: {} SW: {}".format(vrx_pos, vry_pos, swt_val))
    color[0] = 0 if vrx_pos > 500 else 255
    color[1] = 0 if vry_pos > 500 else 255
    color[2] = 0 if swt_val > 500 else 255
    
    pygame.display.update()
