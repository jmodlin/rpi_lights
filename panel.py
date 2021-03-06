
from neopixel import *

class Panel:

    def __init__(self, strip, idx, pixels):
        self.idx = idx
        self.pixels = pixels
        self.strip = strip
        self.leds = [Color(0, 0, 0) for i in range(pixels)]
        self.sideLen = self.pixels/4
        self.leftRange = [0, self.sideLen-1]
        self.topRange = [self.sideLen, int(self.sideLen * 2 - 1)]
        self.rightRange = [int(self.sideLen * 2), int(self.sideLen * 3 - 1)]
        self.bottomRange = [int(self.sideLen * 3), int(self.pixels-1)]
        self.leftFullRange = [0, int(self.sideLen * 1.5 - 1), int(self.pixels - self.sideLen/2), self.pixels-1]
        self.rightFullRange = [int((self.sideLen * 1.5)), int(self.pixels - self.sideLen/2 - 1)]

    def setPixelColor(self, idx, c):
        self.strip.setPixelColor(self.idx*self.pixels+idx, c) 

    def setPanelColor(self, c):
        for i in range(0, self.pixels):
            self.strip.setPixelColor(self.idx*self.pixels+i, c)
            self.leds[i] = c

    def setRangeColor(self, b, e, c):
        for i in range(b, e+1):
            self.strip.setPixelColor(self.idx*self.pixels+i, c)
            self.leds[i] = c

    def setFullLeftColor(self, c):
        beginRange = self.leftFullRange[0]
        endRange = self.leftFullRange[1]
        self.setRangeColor(beginRange, endRange, c)
        beginRange = self.leftFullRange[2]
        endRange = self.leftFullRange[3]
        self.setRangeColor(beginRange, endRange, c)

    def setFullRightColor(self, c):
        beginRange = self.rightFullRange[0]
        endRange = self.rightFullRange[1]
        self.setRangeColor(beginRange, endRange, c)

    def setLeftColor(self, c):
        beginRange = self.leftRange[0]
        endRange = self.leftRange[1]
        self.setRangeColor(beginRange, endRange, c)

    def setTopColor(self, c):
        beginRange = self.topRange[0]
        endRange = self.topRange[1]
        self.setRangeColor(beginRange, endRange, c)

    def setRightColor(self, c):
        beginRange = self.rightRange[0]
        endRange = self.rightRange[1]
        self.setRangeColor(beginRange, endRange, c)
    
    def setBottomColor(self, c):
        beginRange = self.bottomRange[0]
        endRange = self.bottomRange[1]
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
