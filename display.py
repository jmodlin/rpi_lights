
from neopixel import *
import time
import random
from panel import *

import argparse
import signal
import sys

def signal_handler(signal, frame):
        colorWipe(strip, Color(0,0,0))
        sys.exit(0)

def opt_parse():
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', action='store_true', help='clear the display on exit')
        args = parser.parse_args()
        if args.c:
                signal.signal(signal.SIGINT, signal_handler)

# LED strip configuration:
LED_COUNT      = 160      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

class Display:

    def __init__(self, strip, pCount, ppp):
        self.strip = strip
        
        self.panels = []
        for i in range(pCount):
            panels.append(Panel(strip, i, ppp))

        # How many panels are there?
        self.numPanels = len(self.panels)

    def update(self):
        self.strip.show()

    def clear(self):
        for i in range(self.numPanels):
            panel.setPanelColor(Color(0, 0, 0))
        self.strip.show()
        

        


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    opt_parse()

	# Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
    strip.begin()

    # Create display with 5 panels, 32 pixels per panel
    display = Display(strip, 5, 32)
        
    print ('Press Ctrl-C to quit.')
	            