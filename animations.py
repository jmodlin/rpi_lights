# Stock libraries
import time
import random
import signal
import sys

# Custom objects
from panel import *
from animation import *
from display import *

class Blink(Animation):

    def __init__(self, display, c, iterations, ms):
        Animation.__init__(self, display)
        self.color = c
        self.iterations = iterations
        self.ms = ms

    def begin(self):
        Animation.begin(self)
        for i in range(self.iterations):
            for p in self.display.panels:
                p.setPanelColor(self.color)
            self.display.update()
            time.sleep(self.ms/1000.0)
            self.display.clear()
            time.sleep(self.ms/1000.0)

    def end(self):
        self.display.clear()
        
class Rocker(Animation):

    def __init__(self, display, c1, c2, iterations, ms):
        Animation.__init__(self, display)
        self.color1 = c1
        self.color2 = c2
        self.iterations = iterations
        self.ms = ms

    def begin(self):
        Animation.begin(self)

        for p in self.display.panels:
                p.setLeftColor(self.color1)
                p.setTopColor(self.color1)
                p.setRightColor(self.color2)
                p.setBottomColor(self.color2)
            self.display.update()

        for i in range(self.iterations):
            
            for r in range(self.display.numPixels):
                for p in panels:
                        p.rotateCW(1)
                self.display.update()
                time.sleep(self.ms/1000.0)

            for r in range(self.display.numPixels):
                for p in panels:
                        p.rotateCCW(1)
                self.display.update()
                time.sleep(self.ms/1000.0)

    def end(self):
        self.display.clear()

class Kitt(Animation):

    def __init__(self, display, color, iterations, ms):
        Animation.__init__(self, display)
        self.color = color
        self.iterations = iterations
        self.ms = ms

    def begin(self):
        Animation.begin(self)
        
        for i in range(self.iterations):
            # Going up the panels
            for p in range(self.display.numPanels):
                if p > 0:
                    self.display.panels[p-1].setPanelColor(Color(0,0,0))
                self.display.panels[p].setPanelColor(self.color)
                self.display.update()
                delay = (self.ms/1000.0) * ((p+1)/(self.display.numPanels * 1.0))
                print('p->' + `p` + ' .. delay->' + `delay`)
                time.sleep(delay)
            # Going down the panels
            for p in range(self.display.numPanels-1, -1, -1):
                if p < (self.display.numPanels-1):
                    self.display.panels[p+1].setPanelColor(Color(0,0,0))
                self.display.panels[p].setPanelColor(self.color)
                self.display.update()
                delay = (self.ms/1000.0) * (1.0 - (p/(self.display.numPanels * 1.0)))
                print('p->' + `p` + ' .. delay->' + `delay`)
                time.sleep(delay)

    def end(self):
        self.display.clear()
        
class Shimmer(Animation):

    def __init__(self, display, colors, iterations, ms):
        Animation.__init__(self, display)
        self.colors = colors
        self.iterations = iterations
        self.ms = ms

    def begin(self):
        Animation.begin(self)
 
        pos = 0
        for i in range(self.iterations):
    
            c = pos
            for p in self.display.panels:
                
                lColor = (c)%len(self.colors) 
                rColor = (c+1)%len(self.colors)
                
                p.setFullLeftColor(self.colors[lColor])
                p.setFullRightColor(self.colors[rColor])
                c += 2    

            pos += 1
            self.display.update()
            time.sleep(self.ms/1000.0)
            
    def end(self):
        self.display.clear()