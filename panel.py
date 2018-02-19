
from neopixel import *

class Panel:

    def __init__(self, strip, idx, pixels):
        print ('Panel initialized')
        self.idx = idx
        self.pixels = pixels
        self.strip = strip
        self.leds = [Color(0, 0, 0) for i in range(pixels)]

    def setColor(self, c):
        for i in range(0, self.pixels):
            self.strip.setPixelColor(self.idx*self.pixels+i, c)
            self.leds[i] = c

    def setRangeColor(self, b, e, c):
        for i in range(b, e):
            self.strip.setPixelColor(self.idx*self.pixels+i, c)
            self.leds[i] = c

    def setLeftColor(self, c):
        beginRange = 0
        endRange = self.pixels/4
        self.setRangeColor(beginRange, endRange, c)

    def setTopColor(self, c):
        beginRange = self.pixels/4
        endRange = self.pixels/4 + self.pixels/4
        self.setRangeColor(beginRange, endRange, c)

    def setRightColor(self, c):
        beginRange = 2*self.pixels/4
        endRange = 2*self.pixels/4 + self.pixels/4
        self.setRangeColor(beginRange, endRange, c)
    
    def setBottomColor(self, c):
        beginRange = 3*self.pixels/4
        endRange = 3*self.pixels/4 + self.pixels/4
        self.setRangeColor(beginRange, endRange, c)

    def rotateColor(self, n):
        rotated = [Color(0,0,0) for i in range(self.pixels)]

        for i in range(self.pixels):
            rotated[i] = self.leds[(i+n)%self.pixels]
        
        for i in range(self.pixels):
            self.strip.setPixelColor(self.idx*self.pixels+i, c)
            self.leds[i] = c






        
    