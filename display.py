
from neopixel import *
import time
import random
from panel import *

import argparse
import signal
import sys

# LED strip configuration:
LED_COUNT      = 160      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

class Display:

    def __init__(self, pCount, ppp):
        
        # Ensure LED_COUNT is correct
        LED_COUNT = (pCount * ppp)

        # Initialize LED strip
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        self.strip.begin()

        # Initialize panel objects
        self.panels = []
        for i in range(pCount):
            self.panels.append(Panel(self.strip, i, ppp))

        # How many panels are there?
        self.numPanels = len(self.panels)

        # Pixels per panel (ppp)
        self.pixelsPerPanel = ppp

    def setBrightness(self, brightness):
        if brightness >= 0 and brightness <= 255:
            self.strip.setBrightness(brightness)

    def getBrightness(self):
        return self.strip.getBrightness()

    def update(self):
        self.strip.show()

    def clear(self):
        for p in self.panels:
            p.setPanelColor(Color(0, 0, 0))
        self.strip.show()

