
from neopixel import *

class Panel:

    def __init__(self, strip, idx, pixels):
        self.idx = idx
        self.pixels = pixels
        self.strip = strip
        self.leds = [Color(0, 0, 0) for i in range(pixels)]
        self.sideLen = self.pixels/4
        self.leftRange = [0, self.sideLen]
        self.topRange = [(self.sideLen) + 1, self.sideLen * 2]
        self.rightRange = [(self.sideLen * 2) + 1, self.sideLen * 3]
        self.bottomRange = [(self.sideLen * 3) + 1, self.pixels]
        self.leftFullRange = [0, self.sideLen * 1.5, self.pixels - self.sideLen/2, self.pixels]
        self.rightFullRange = [(self.sideLen * 1.5) + 1, self.pixels - self.sideLen/2 - 1]

    def setPixelColor(self, idx, c):
        self.strip.setPixelColor(self.idx*self.pixels+idx, c) 

    def setPanelColor(self, c):
        for i in range(0, self.pixels):
            self.strip.setPixelColor(self.idx*self.pixels+i, c)
            self.leds[i] = c

    def setRangeColor(self, b, e, c):
        for i in range(b, e):
            self.strip.setPixelColor(self.idx*self.pixels+i, c)
            self.leds[i] = c

    def setFullLeftColor(self, c):
        beginRange = int(self.leftFullRange[0])
        endRange = int(self.leftFullRange[1])
        self.setRangeColor(beginRange, endRange, c)
        beginRange = int(self.leftFullRange[2])
        endRange = int(self.leftFullRange[3])
        self.setRangeColor(beginRange, endRange, c)

    def setFullRightColor(self, c):
        beginRange = int(self.rightFullRange[0])
        endRange = int(self.rightFullRange[1])
        self.setRangeColor(beginRange, endRange, c)

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

    def rotateCW(self, n):
        rotated = [Color(0,0,0) for i in range(self.pixels)]

        for i in range(self.pixels):
            rotated[i] = self.leds[(i-n)%self.pixels]
        
        for i in range(self.pixels):
            self.strip.setPixelColor(self.idx*self.pixels+i, rotated[i])
            self.leds[i] = rotated[i]

    def rotateCCW(self, n):
        rotated = [Color(0,0,0) for i in range(self.pixels)]

        for i in range(self.pixels):
            rotated[i] = self.leds[(i+n)%self.pixels]
        
        for i in range(self.pixels):
            self.strip.setPixelColor(self.idx*self.pixels+i, rotated[i])
            self.leds[i] = rotated[i]
