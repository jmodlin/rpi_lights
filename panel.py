
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
            self.strip.setPixelColor(i, c)

    def setLeftColor(self, c):
        beginRange = self.idx*self.pixels
        endRange = self.idx*self.pixels + self.pixels/4
        self.setRangeColor(beginRange, endRange, c)

    def setTopColor(self, c):
        beginRange = self.idx*self.pixels + self.pixels/4
        endRange = self.idx*self.pixels + self.pixels/4 + self.pixels/4
        self.setRangeColor(beginRange, endRange, c)

    def setRightColor(self, c):
        beginRange = self.idx*self.pixels + 2*self.pixels/4
        endRange = self.idx*self.pixels + 2*self.pixels/4 + self.pixels/4
        self.setRangeColor(beginRange, endRange, c)
    
    def setBottomColor(self, c):
        beginRange = self.idx*self.pixels + 3*self.pixels/4
        endRange = self.idx*self.pixels + 3*self.pixels/4 + self.pixels/4
        self.setRangeColor(beginRange, endRange, c)


        
    