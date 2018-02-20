
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

class POV:

    def __init__(self, strip, c):
        self.idx = idx
        self.pixels = pixels
        self.strip = strip
        self.leds = [Color(0, 0, 0) for i in range(pixels)]

        # 1st dimension = tick ... 2nd dimension = color
        # Start at TOP LEFT of letter

        # D
        #   #### 
        #   #   #
        #   #   #
        #   #   #
        #   #### 
        self.D = [0 for i in range(5)][0 for i in range(5)]
        self.D[0] = [c for i in range(5)]
        self.D[1][0] = c
        self.D[1][4] = c
        self.D[2][0] = c
        self.D[2][4] = c
        self.D[3][0] = c
        self.D[3][4] = c
        self.D[4] = [c for i in range(1, 3, 1)]

        # I
        #   ##### 
        #     #   
        #     #   
        #     #  
        #   ##### 
        self.I = [0 for i in range(5)][0 for i in range(5)]
        self.I[0][0] = c
        self.I[0][4] = c
        self.I[1][0] = c
        self.I[1][4] = c
        self.I[2] = [c for i in range(5)]
        self.I[3][0] = c
        self.I[3][4] = c
        self.I[4][0] = c
        self.I[4][4] = c

        # L
        #   # 
        #   #   
        #   #   
        #   #   
        #   ##### 
        self.L = [0 for i in range(5)][0 for i in range(5)]
        self.L[0] = [c for i in range(5)]
        self.L[1][4] = c
        self.L[2][4] = c
        self.L[3][4] = c
        self.L[4][4] = c

        # M
        #   #   #
        #   ## ##
        #   # # #
        #   #   #
        #   #   #
        self.M = [0 for i in range(5)][0 for i in range(5)]
        self.M[0] = [c for i in range(5)]
        self.M[1][1] = c
        self.M[2][2] = c
        self.M[3][1] = c
        self.M[4] = [c for i in range(5)]

        # N
        #   #   #
        #   ##  #
        #   # # #
        #   #  ##
        #   #   #
        self.N = [0 for i in range(5)][0 for i in range(5)]
        self.N[0] = [c for i in range(5)]
        self.N[1][1] = c
        self.N[2][2] = c
        self.N[3][3] = c
        self.N[4] = [c for i in range(5)]
        
        # O
        #    ### 
        #   #   #
        #   #   #
        #   #   #
        #    ### 
        self.O = [0 for i in range(5)][0 for i in range(5)]
        self.O[0] = [c for i in range(1, 3, 1)]
        self.O[1][0] = c
        self.O[1][4] = c
        self.O[2][0] = c
        self.O[2][4] = c
        self.O[3][0] = c
        self.O[3][4] = c
        self.O[4] = [c for i in range(1, 3, 1)]



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

        pov = POV(strip, Color(255, 0, 0))
        
	print ('Press Ctrl-C to quit.')
	while True:
                
                for i in range(20):
                        for tick in range(5):
                                for p in range(5):
                                        panels[p].setColor(pov.M[tick][p])
                                strip.show()
                                time.wait(1)

                        for tick in range(4, -1, -1):
                                for p in range(5):
                                        panels[p].setColor(pov.M[tick][p])
                                strip.show()
                                time.wait(1)

                for p in panels:
                        p.setColor(Color(0, 0, 0))
                strip.show()
                time.wait(5.0)
 



    