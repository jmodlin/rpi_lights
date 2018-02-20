
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
        self.strip = strip
        
        self.letters = []
        for letter in range(65, 91):
                self.letters.append(chr(letter))

        # 1st dimension = tick ... 2nd dimension = color
        # Start at TOP LEFT of letter
        ###
        # D
        #   #### 
        #   #   #
        #   #   #
        #   #   #
        #   #### 
        self.letter['D'] = { (tick, color): 0 for tick in range(5) for color in range(5) }
        self.letter['D'] = {
                                (0, 0): c, (0, 1): c, (0, 2): c, (0, 3): c, (0, 4): c, 
                                (1, 0): c, (1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): c, 
                                (2, 0): c, (2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): c, 
                                (3, 0): c, (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): c, 
                                (4, 0): 0, (4, 1): c, (4, 2): c, (4, 3): c, (4, 4): 0 }

        # I
        #   ##### 
        #     #   
        #     #   
        #     #  
        #   ##### 
        self.letter['I'] = { (tick, color): 0 for tick in range(5) for color in range(5) }
        self.letter['I'] = {
                                (0, 0): c, (0, 1): 0, (0, 2): 0, (0, 3): 0, (0, 4): c, 
                                (1, 0): c, (1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): c, 
                                (2, 0): c, (2, 1): c, (2, 2): c, (2, 3): c, (2, 4): c, 
                                (3, 0): c, (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): c, 
                                (4, 0): c, (4, 1): 0, (4, 2): 0, (4, 3): 0, (4, 4): c }

        # L
        #   # 
        #   #   
        #   #   
        #   #   
        #   ##### 
        self.letter['L'] = { (tick, color): 0 for tick in range(5) for color in range(5) }
        self.letter['L'] = {
                                (0, 0): c, (0, 1): c, (0, 2): c, (0, 3): c, (0, 4): c, 
                                (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): c, 
                                (2, 0): 0, (2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): c, 
                                (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): c, 
                                (4, 0): 0, (4, 1): 0, (4, 2): 0, (4, 3): 0, (4, 4): c }

        # M
        #   #   #
        #   ## ##
        #   # # #
        #   #   #
        #   #   #
        self.letter['M'] = { (tick, color): 0 for tick in range(5) for color in range(5) }
        self.letter['M'] = {
                                (0, 0): c, (0, 1): c, (0, 2): c, (0, 3): c, (0, 4): c, 
                                (1, 0): 0, (1, 1): c, (1, 2): 0, (1, 3): 0, (1, 4): 0, 
                                (2, 0): 0, (2, 1): 0, (2, 2): c, (2, 3): 0, (2, 4): 0, 
                                (3, 0): 0, (3, 1): c, (3, 2): 0, (3, 3): 0, (3, 4): 0, 
                                (4, 0): c, (4, 1): c, (4, 2): c, (4, 3): c, (4, 4): c }

        # N
        #   #   #
        #   ##  #
        #   # # #
        #   #  ##
        #   #   #
        self.letter['N'] = { (tick, color): 0 for tick in range(5) for color in range(5) }
        self.letter['N'] = {
                                (0, 0): c, (0, 1): c, (0, 2): c, (0, 3): c, (0, 4): c, 
                                (1, 0): 0, (1, 1): c, (1, 2): 0, (1, 3): 0, (1, 4): 0, 
                                (2, 0): 0, (2, 1): 0, (2, 2): c, (2, 3): 0, (2, 4): 0, 
                                (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): c, (3, 4): 0, 
                                (4, 0): c, (4, 1): c, (4, 2): c, (4, 3): c, (4, 4): c }
        
        # O
        #    ### 
        #   #   #
        #   #   #
        #   #   #
        #    ### 
        self.letter['O'] = { (tick, color): 0 for tick in range(5) for color in range(5) }
        self.letter['O'] = {
                                (0, 0): 0, (0, 1): c, (0, 2): c, (0, 3): c, (0, 4): 0, 
                                (1, 0): c, (1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): c, 
                                (2, 0): c, (2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): c, 
                                (3, 0): c, (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): c, 
                                (4, 0): 0, (4, 1): c, (4, 2): c, (4, 3): c, (4, 4): 0 }


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
                
                #MODLIN\
                buff = 'MODLIN'
                for letter in buff:
                        for i in range(1):
                                for tick in range(5):
                                        for p in range(5):
                                                panels[p].setColor(pov.letters[letter][tick, p])
                                        strip.show()
                                        time.sleep(1.0)

                                for tick in range(4, -1, -1):
                                        for p in range(5):
                                                panels[p].setColor(pov.letters[letter][tick, p])
                                        strip.show()
                                        time.sleep(1.0)

                        for p in panels:
                                p.setColor(Color(0, 0, 0))
                        strip.show()
                        time.sleep(2.0)
 



    