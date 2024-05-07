#micropython

import time
#import network
#import socket
import machine
import neopixel

start = time.ticks_ms()
powerLed = machine.Pin("LED", machine.Pin.OUT)

#ssid = '<>'
#password = '<>'

num_leds = 1
sleepInterval = 1

#def connect():
#    #Connect to WLAN
#    wlan = network.WLAN(network.STA_IF)
#    wlan.active(True)
#    wlan.connect(ssid, password)
#    while wlan.isconnected() == False:
#        print('Waiting for connection...')
#        time.sleep(1)
#    print(wlan.ifconfig())
#    end = time.ticks_ms()
#    print(f"{end-start} milliseconds to get wifi")


def activateNeopixels(r,g,b):
    np = neopixel.NeoPixel(machine.Pin(1), num_leds)
    
    for i in range(num_leds):
        np[i] = (r,g,b)
        print(f"{np[i]=}")

        if i > 0:
            np[i] = (0,0,0)
            print(f"{np[i]=}")
    np.write()
    print("wrote neopixel")



def main():

    #try:
    #    connect()
    #except KeyboardInterrupt:
    #    machine.reset()

    while True:
        activateNeopixels(255, 0, 0)
        
        # blink board LED 
        powerLed.value(1)
        time.sleep(sleepInterval)
        powerLed.value(0)
        time.sleep(sleepInterval)


main()


