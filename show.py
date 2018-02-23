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
    kitt = Kitt(display, Color(255,0,0), 20, 300)

    colors = [Color(212, 36, 38), Color(36, 214, 211), Color(39, 214, 36), Color(211, 36, 214), Color(122, 36, 214), Color(255, 255, 255), Color(255, 255, 255)]
    shimmer = Shimmer(display, colors, 150, 400)

    #animations = [redblinky, greenblinky, kitt]
    animations = [shimmer]

    # Initialize show
    show = Show(display, animations)
    show.play()


    
