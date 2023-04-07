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
from helper import Distance

# Choose a UI

#from ui_default import UiDefault as UI
from ui_homer import UiHomer as UI
#from ui_dial import UiDial as UI
#from ui_flip import UiFlip as UI
#from ui_trek import UiTrek as UI
#from ui_roman import UiRoman as UI
#from ui_tape import UiTape as UI
#from ui_cyberpunk import UiCyberpunk as UI

# Setup the display
display = PicoGraphics(display=DISPLAY_ROUND_LCD_240X240, pen_type=PEN_RGB565)

SENSOR_TRIGGER_PIN = 4              # Trigger pin for the ultrasonic sensor
SENSOR_ECHO_PIN = 3                 # Echo pin for the ultrasonic sensor

class UltrasonicSensor:
    """Class for the ultrasonic sensor
        trigger - The trigger pin
        echo - The echo pin
    """
    # Speed of sound in meters per second
    speed_of_sound_mps = 343.2

    # Speed of sound in cm per microsecond
    speed_of_sound_cm_per_us = speed_of_sound_mps / 10000

    # Last distance measured
    distance = None

    def __init__(self, trigger, echo):
        """Initialise the sensor
            trigger - The trigger pin
            echo - The echo pin
        """
        self.trigger = Pin(trigger, Pin.OUT)
        self.echo = Pin(echo, Pin.IN)

    def measure(self) -> Distance:
        """Measure the distance to an object"""
        self.trigger.low()
        utime.sleep_us(2)
        self.trigger.high()
        utime.sleep_us(5)
        self.trigger.low()

        while self.echo.value() == 0:
            signaloff = utime.ticks_us()
        while self.echo.value() == 1:
            signalon = utime.ticks_us()

        timepassed = signalon - signaloff
        self.distance = Distance((timepassed * self.speed_of_sound_cm_per_us) / 2)

        return self.distance

# Main Program

# Create a new sensor
sensor = UltrasonicSensor(SENSOR_TRIGGER_PIN, SENSOR_ECHO_PIN)

# Create a new UI
ui = UI(display)

while True:

    # Measure the distance
    distance = sensor.measure()
    print("The distance from the object is {} mm".format(distance.getMm()))

    # Draw the UI
    ui.draw(distance)

    # Wait a second
    utime.sleep(1)
