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
                #150-(i/5/1000)
                #150/1000*(0/5)
                delay = (self.ms/1000.0)*((i+1)/self.display.numPanels)
                time.sleep(delay)
            time.sleep(self.ms/4/1000.0)
            # Going down the panels
            for p in range(self.display.numPanels-1, -1, -1):
                if p < (self.display.numPanels-1):
                    self.display.panels[p+1].setPanelColor(Color(0,0,0))
                self.display.panels[p].setPanelColor(self.color)
                self.display.update()
                delay = (self.ms/1000.0)*((self.iterations-i+1)/self.display.numPanels)
                time.sleep(delay)
            time.sleep(self.ms/4/1000.0)

    def end(self):
        self.display.clear()
        
