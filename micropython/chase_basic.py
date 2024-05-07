# micropython

import machine
import neopixel
import time

# Configuration Variables
pin_number = 9  # Adjust to the GPIO pin connected to your NeoPixel strip
num_leds = 59    # Total number of LEDs in the strip
num_lit_leds = 4 # Number of LEDs that are lit at the same time

# Setup the NeoPixel strip
np = neopixel.NeoPixel(machine.Pin(pin_number), num_leds)

def clear():
    for i in range(num_leds):
        np[i] = (0, 0, 0)
    np.write()

def bounce(num_lit_leds, delay):
    direction = 1
    position = 0

    while True:
        clear()

        # Light up LEDs based on current position
        for i in range(num_lit_leds):
            index = position + i
            if 0 <= index < num_leds:
                np[index] = (10, 10, 10)  # Set color to white, adjust RGB values as desired
                print(f"{np[index]=} at {index=}")

        np.write()
        time.sleep(delay)

        # Update the position
        position += direction

        # Change direction if reaching the end or start
        if position + num_lit_leds >= num_leds or position <= 0:
            direction *= -1

try:
    bounce(num_lit_leds, 1)  # Run bounce function with a delay of 0.1 seconds
except KeyboardInterrupt:
    clear()  # Turn off LEDs when stopping the program

