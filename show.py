# Stock libraries
import time
import random
import argparse
import signal
import sys

# LED library
from neopixel import *

# Custom objects
from panel import *
from animation import *
from animations import *
from display import *

class Show:

    def __init__(self, display, animations):
        self.display = display
        self.animations = animations
    
    def play(self):
        print('Starting show ...')
        for a in self.animations:
            a.begin()

    
# Main program logic follows:
if __name__ == '__main__':

    # Initialize display 
    display = Display(5, 32)

    # Initialize animations for show
    redblinky = Blink(display, Color(255,0,0), 10, 250)
    greenblinky = Blink(display, Color(0,255,0), 10, 250)
    kitt = Kitt(display, Color(255,0,0), 20, 150)
    animations = [redblinky, greenblinky, kitt]

    # Initialize show
    show = Show(display, animations)
    show.play()


    
