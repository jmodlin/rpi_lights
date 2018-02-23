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

                # 200 / 1000 * (1 - (0/5)) =200  
                #150/1000 * (1 - 0/5)

                # 0

                # (self.ms/1000.0) * (1.0 - ((numPanels - (p+1)) * 1.0))
                # 200 / 1000 * (1 - (1/5))
                # 0.2 * 1 - 1/5 = .8
                # 1 - 2/5 = .6
                # 1 - 3/5 
                delay = (self.ms/1000.0) * ((p+1)/(self.display.numPanels * 1.0))
                print('p->' + `p` + ' .. delay->' + `delay`)
                time.sleep(delay)
            time.sleep(self.ms/4/1000.0)
            # Going down the panels
            for p in range(self.display.numPanels-1, -1, -1):
                if p < (self.display.numPanels-1):
                    self.display.panels[p+1].setPanelColor(Color(0,0,0))
                self.display.panels[p].setPanelColor(self.color)
                self.display.update()
                # 1.0 - 4/5 = .2
                # 1 - .6 = .4
                # 1 - .4 = .6
                # 1 - .2 = .8
                delay = (self.ms/1000.0) * (1.0 - (p/(self.display.numPanels * 1.0)))
                print('p->' + `p` + ' .. delay->' + `delay`)
                time.sleep(delay)
            time.sleep(self.ms/4/1000.0)

    def end(self):
        self.display.clear()
        
