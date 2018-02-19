
from neopixel import *

class POV:

    def __init__(self, strip, c):
        self.idx = idx
        self.pixels = pixels
        self.strip = strip
        self.leds = [Color(0, 0, 0) for i in range(pixels)]

        # 1st dimension = color ... 2nd dimension = tick
        # Start at TOP LEFT of letter

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
        
         



    