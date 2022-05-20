import spidev
import os
import time

swt_channel = 0
vrx_channel = 1
vry_channel = 2

delay = 0.5

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

def readChannel(channel):
    val = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((val[1] & 3) << 8) + val[2]
    return data

while True:
    vrx_pos = readChannel(vrx_channel)
    vry_pos = readChannel(vry_channel)
    swt_val = readChannel(swt_channel)

    print("VRx : {} VRy: {} SW: {}".format(vrx_pos, vry_pos, swt_val))
    time.sleep(delay)
