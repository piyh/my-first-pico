import machine
import neopixel
import time

# Configuration Variables
pin_number = 0  # Adjust to the GPIO pin connected to your NeoPixel strip
num_leds = 59    # Total number of LEDs in the strip
num_lit_leds = 6 # Number of LEDs that are lit at the same time

# Setup the NeoPixel strip
np = neopixel.NeoPixel(machine.Pin(pin_number), num_leds)

def clear():
    for i in range(num_leds):
        np[i] = (0, 0, 0)
    np.write()

def interpolate_color(start_color, end_color, step, max_steps):
    # Interpolate RGB values
    s_red, s_green, s_blue = start_color
    e_red, e_green, e_blue = end_color
    red = int(s_red + (e_red - s_red) * step / max_steps)
    green = int(s_green + (e_green - s_green) * step / max_steps)
    blue = int(s_blue + (e_blue - s_blue) * step / max_steps)
    return (red, green, blue)

def bounce(num_lit_leds, delay):
    direction = 1
    position = 0

    # Define start and end colors for the gradient
    color_forward_start = (128, 0, 128)  # Purple
    color_forward_end = (255, 0, 0)      # Red
    color_backward_start = (255, 0, 0)   # Red
    color_backward_end = (128, 0, 128)   # Purple

    while True:
        clear()

        # Light up LEDs based on current position with gradient
        for i in range(num_lit_leds):
            index = position + i
            if 0 <= index < num_leds:
                if direction == 1:
                    color = interpolate_color(color_forward_start, color_forward_end, i, num_lit_leds - 1)
                else:
                    color = interpolate_color(color_backward_start, color_backward_end, i, num_lit_leds - 1)
                np[index] = color

        np.write()
        time.sleep(delay)

        # Update the position
        position += direction

        # Change direction if reaching the end or start
        if position + num_lit_leds >= num_leds or position <= 0:
            direction *= -1

try:
    bounce(num_lit_leds, 0.1)  # Run bounce function with a delay of 0.1 seconds
except KeyboardInterrupt:
    clear()  # Turn off LEDs when stopping the program
