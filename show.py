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
from blink import *
from display import *

class Show:

    def __init__(self, display, animations):
        self.display = display
        self.animations = animations
    
    def play(self):
        print('starting show ...')
        for a in self.animations:
            a.begin()

    
# Main program logic follows:
if __name__ == '__main__':

    # Initialize display 
    display = Display(5, 32)

    # Initialize animations for show
    blinky = Blink(display)
    animations = [blinky]

    # Initialize show
    show = Show(display, animations)
    show.play()


    
