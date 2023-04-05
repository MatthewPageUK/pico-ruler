"""
    ____  _      __                           ______         ____  __      _           __
   / __ \(_)____/ /_____ _____  ________     /_  __/___     / __ \/ /_    (_)__  _____/ /_
  / / / / / ___/ __/ __ `/ __ \/ ___/ _ \     / / / __ \   / / / / __ \  / / _ \/ ___/ __/
 / /_/ / (__  ) /_/ /_/ / / / / /__/  __/    / / / /_/ /  / /_/ / /_/ / / /  __/ /__/ /_
/_____/_/____/\__/\__,_/_/ /_/\___/\___/    /_/  \____/   \____/_.___/_/ /\___/\___/\__/
                                                                    /___/

 Raspberry Pi Pico-W ultrasonic distance meter.
 Displays distance to object in cm and inches.

 Firmware requirements:
    Micropython with Pimoroni Picographics library

 Hardare requirements:
    Raspberry Pi Pico-W
    1.3" SPI Round LCD Screen (240x240)
    Ultrasonic sensor (HC-SR04)
    10 x M2 x 4mm screws

 Default screen wiring:
    CS to GP17
    SCK to GP18
    MOSI to GP19
    DC to GP16
    BL to GP20

 Ultrasonic wiring:
    Trigger to GP4
    Echo to GP3
    GND to any ground pin
    VCC to 3.5v out

 By           - Matthew Page
 Credit       - Everyone who came before and wrote a how to guide
 Version      - 0.1
 Release date - 5th April 2023
"""
from machine import Pin
import utime
from picographics import PicoGraphics, DISPLAY_ROUND_LCD_240X240, PEN_RGB565
import jpegdec

# Setup the display
display = PicoGraphics(display=DISPLAY_ROUND_LCD_240X240, pen_type=PEN_RGB565)

WIDTH = display.get_bounds()[0]     # Screen width
HEIGHT = display.get_bounds()[1]    # Screen height
MIDX = int(WIDTH/2)                 # Middle of the screen
MIDY = int(WIDTH/2)                 # Middle of the screen
BG = display.create_pen(90, 25, 70)
GREEN = display.create_pen(50, 255, 50)

# Setup the ultrasonic sensor pins
trigger = Pin(4, Pin.OUT)
echo = Pin(3, Pin.IN)

# Create a new JPEG decoder for our PicoGraphics
j = jpegdec.JPEG(display)

# Open the JPEG file
j.open_file("back.jpg")

while True:

    # Ping
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()

    # Wait for echo
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()

    # Time and distance
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2

    print("The distance from object is ",distance,"cm")

    # Decode the JPEG
    j.decode(0, 0, jpegdec.JPEG_SCALE_FULL, dither=True)

    display.set_pen(GREEN)

    # Display the distance in cm
    text = "{distance:0.2f}".format(distance=distance)
    twidth = display.measure_text(text, 3)
    xpos = int((WIDTH - twidth) / 2)
    display.text(text, xpos, 90, 200, 3)

    # Display the distance in inches
    text = "{distance:0.2f}".format(distance=distance/2.54)
    twidth = display.measure_text(text, 3)
    xpos = int((WIDTH - twidth) / 2)
    display.text(text, xpos, 133, 200, 3)

    # Update the display
    display.update()

    utime.sleep(1)
