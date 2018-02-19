# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import random
from panel import *

from neopixel import *

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

def panelOn(strip, idx, c=Color(255,255,255)):

    for j in range(idx * 32, idx * 32 + 32):
        strip.setPixelColor(j, c)

def panelOff(strip, idx):

    c = Color(0, 0, 0)
    for j in range(idx * 32, idx * 32 + 32):
        strip.setPixelColor(j, c)

def blinkPanels(strip, wait_ms=50):

    panelOff(strip, 0)
    panelOff(strip, 1)

    i = 0
    while True:
        panelOff(strip, 0)
        panelOff(strip, 1)
        if i%2 == 0:
            c = Color(255, 0, 0)
        else:
            c = Color(0, 255, 0)
        panelOn(strip, i%2, c)
        strip.show()
        i += 1
        print(i%2)
        time.sleep(wait_ms/1000.0)


def leftright(strip, wait_ms=10):

        c = Color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        for j in range(50):
                for i in range(0,8):
                        strip.setPixelColor(i, c)
                strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0,8):
                        strip.setPixelColor(i, Color(0, 0, 0))
                strip.show()
                
                for i in range(24,31):
                        strip.setPixelColor(i, c)
                strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(24,31):
                        strip.setPixelColor(i, Color(0, 0, 0))
                strip.show()

def gfunc(strip, wait_ms=10):

    for j in range(0,5):
        strip.setPixelColor(j*7, Color(255, 0, 0))
        strip.setPixelColor(j*7+1, Color(255, 127, 0))
        strip.setPixelColor(j*7+2, Color(255, 255, 0))
        strip.setPixelColor(j*7+3, Color(0, 255, 0))
        strip.setPixelColor(j*7+4, Color(0, 0, 255))
        strip.setPixelColor(j*7+5, Color(139, 0, 255))
        strip.setPixelColor(j*7+6, Color(0, 0, 0))

    strip.show()
    time.sleep(wait_ms/1000)


def blink(strip, wait_ms=10):
        c = Color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))

        for j in range(50):
                for i in range(strip.numPixels()):
                        strip.setPixelColor(i, c)
                strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(strip.numPixels()):
                        strip.setPixelColor(i, Color(0, 0, 0))
                strip.show()
                time.sleep(wait_ms/1000.0)

# Main program logic follows:
if __name__ == '__main__':
        # Process arguments
        opt_parse()

	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

        panels = []
        panels.append(Panel(strip, 0, 32))
        panels.append(Panel(strip, 1, 32))
        panels.append(Panel(strip, 2, 32))
        panels.append(Panel(strip, 3, 32))
        panels.append(Panel(strip, 4, 32))

	print ('Press Ctrl-C to quit.')
	while True:

                # Set top colors blue
                t = 0.1

                c = Color(0,0, 255)
                for p in panels:
                        p.setTopColor(c)
                        strip.show()
                        time.sleep(t)
                
                c = Color(255, 0, 0)
                for p in panels:
                        p.setBottomColor(c)
                        strip.show()
                        time.sleep(t)
                
                c = Color(0, 0, 255)
                for p in panels:
                        p.setLeftColor(c)
                        strip.show()
                        time.sleep(t)
                
                c = Color(255, 0, 0)
                for p in panels:
                        p.setRightColor(c)
                        strip.show()
                        time.sleep(t)

                # Rotate
                t = 0.01
                for i in range(5):
                        for i in range(32):
                                for p in panels:
                                        p.rotateCW(1)
                                strip.show()
                                time.sleep(t)

                        for i in range(32):
                                for p in panels:
                                        p.rotateCCW(1)
                                strip.show()
                                time.sleep(t)
                        
                # Clear
                t = 0.1
                time.sleep(1.5)
                c = Color(0, 0, 0)
                for p in panels:
                        p.setColor(c)
                        strip.show()
                        time.sleep(t)
                
                time.sleep(1.5)

                # Rainbow
                panels[0].setLeftColor(Color(255, 0 , 0))
                panels[0].setRightColor(Color(255, 127, 0))
                panels[1].setLeftColor(Color(255, 255 , 0))
                panels[1].setRightColor(Color(0, 255, 0))
                panels[2].setLeftColor(Color(0, 0 , 255))
                panels[2].setRightColor(Color(75, 0, 130))
                panels[3].setLeftColor(Color(148, 0 , 211))
                
                # Clear
                t = 0.1
                time.sleep(1.5)
                c = Color(0, 0, 0)
                for p in panels:
                        p.setColor(c)
                        strip.show()
                        time.sleep(t)
                
                time.sleep(1.5)
