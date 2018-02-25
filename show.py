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
    kitt = Kitt(display, Color(255,0,0), 5, 200)

    #colors = [Color(212, 36, 38), Color(36, 214, 211), Color(39, 214, 36), Color(211, 36, 214), Color(122, 36, 214), Color(255, 255, 255), Color(255, 255, 255)]
    #colors = [Color(212, 36, 38), Color(36, 214, 211), Color(39, 214, 36), Color(211, 36, 214)]
    colors = [Color(0, 255, 10), Color(255, 215, 0)]
    
    # Christmas colors
    xmasColors = [Color(255, 0, 0), Color(0, 255, 0), Color(212, 36, 38), Color(36, 214, 211), Color(39, 214, 36), Color(211, 36, 214), Color(122, 36, 214)]

    # Halloween colors
    halloweenColors = [Color(247, 95, 28), Color(136, 30, 228), Color(133, 226, 31)]

    # St. Patrick's Day colors    
    stPatColors = [Color(0,255,10), Color(255,215,0), Color(255,215,0), Color(0,255,10)]

    
    shimmer1 = Shimmer(display, stPatColors, 50, 600)
    breath = Breathing(display, stPatColors[:2], 1000, 20)
    rocker = Rotator(display, stPatColors[0], stPatColors[1], False, 5, 100)
    shimmer2 = Shimmer(display, stPatColors[:2], 50, 600)

    xmasshimmer1 = Shimmer(display, xmasColors, 50, 600)
    xmasbreath = Breathing(display, xmasColors[:2], 1000, 20)
    xmasrocker = Rotator(display, xmasColors[0], xmasColors[1], False, 5, 100)
    xmasshimmer2 = Shimmer(display, xmasColors[:2], 50, 600)

    halloshimmer1 = Shimmer(display, halloweenColors, 50, 600)
    hallobreath = Breathing(display, halloweenColors[:2], 1000, 20)
    hallorocker = Rotator(display, halloweenColors[0], halloweenColors[1], False, 5, 100)
    halloshimmer2 = Shimmer(display, halloweenColors[:2], 50, 600)

    w = Whiteness(display, 500, 10)

    #animations = [rocker, shimmer1, breath, shimmer2, xmasrocker, xmasshimmer1, xmasbreath, xmasshimmer2, hallorocker, halloshimmer1, hallobreath, halloshimmer2]
    #animations = [rocker, shimmer1, breath, shimmer2]
    animations = [w]
    
    # Initialize show
    show = Show(display, animations)

    while True:
        print ('Press Ctrl-C to quit.')
        show.play()


    
