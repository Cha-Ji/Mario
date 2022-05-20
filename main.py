from joystick import Joystick
import time

swt_channel = 0
vrx_channel = 1
vry_channel = 2

DELAY = 0.5

joystick = Joystick()

while True:
    vrx_pos = joystick.readChannel(vrx_channel)
    vry_pos = joystick.readChannel(vry_channel)
    swt_val = joystick.readChannel(swt_channel)

    print("VRx : {} VRy: {} SW: {}".format(vrx_pos, vry_pos, swt_val))
    time.sleep(DELAY)
