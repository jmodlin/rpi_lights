# Stock libraries
import time
import random
import signal
import sys
import math
import datetime 

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
        
        # Finished
        self.end()

    def end(self):
        Animation.end(self)
        
class Rotator(Animation):

    def __init__(self, display, c1, c2, rocker, iterations, ms):
        Animation.__init__(self, display)
        self.color1 = c1
        self.color2 = c2
        self.rocker = rocker
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
            
            for r in range(self.display.pixelsPerPanel):
                for p in self.display.panels:
                        p.rotateCW(1)
                self.display.update()
                time.sleep(self.ms/1000.0)

            if self.rocker:
                for r in range(self.display.pixelsPerPanel):
                    for p in self.display.panels:
                            p.rotateCCW(1)
                    self.display.update()
                    time.sleep(self.ms/1000.0)
            
        # Finished
        self.end()

    def end(self):
        Animation.end(self)

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
                time.sleep(delay)
            # Going down the panels
            for p in range(self.display.numPanels-1, -1, -1):
                if p < (self.display.numPanels-1):
                    self.display.panels[p+1].setPanelColor(Color(0,0,0))
                self.display.panels[p].setPanelColor(self.color)
                self.display.update()
                delay = (self.ms/1000.0) * (1.0 - (p/(self.display.numPanels * 1.0)))
                time.sleep(delay)

        # Finished
        self.end()

    def end(self):
        Animation.end(self)
        
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
        
        # Finished
        self.end()
            
    def end(self):
        Animation.end(self)

class Whiteness(Animation):

    def __init__(self, display, iterations, ms):
        Animation.__init__(self, display)
        self.iterations = iterations
        self.ms = ms

    def begin(self):
        Animation.begin(self)
 
        # Set light colors
        c = Color(255, 0, 0, 0)
        for p in self.display.panels:
            p.setPanelColor(c)
           
        # Start increase/decrease brightness
        for i in range(iterations):
            
            for p in self.display.panels:
                c = Color(255, 0, 0, i%255)
                p.setPanelColor(c)
                
            self.display.update()
            time.sleep(self.ms/1000.0)
            
        # Finished
        self.end()
            
    def end(self):
        Animation.end(self)

class Breathing(Animation):

    def __init__(self, display, colors, iterations, ms):
        Animation.__init__(self, display)
        self.colors = colors
        self.iterations = iterations
        self.ms = ms

    def begin(self):
        Animation.begin(self)
 
        # Set light colors
        c = 0
        for p in self.display.panels:
            p.setPanelColor(self.colors[c%len(self.colors)])
            c += 1

        # Start increase/decrease brightness
        i = 0 
        start = datetime.datetime.now()
        while i < self.iterations:
            
            # Breathing calculation - Thanks to Sean Voisen
            # URL - http://sean.voisen.org/blog/2011/10/breathing-led-with-arduino/
            elapsed_ms = (datetime.datetime.now() - start) .total_seconds() * 1000
            brightness = int((math.exp(math.sin(elapsed_ms/2000.0*math.pi)) - 0.36787944) * 108.0)
            self.display.setBrightness(brightness)
            self.display.update()
            time.sleep(self.ms/1000.0)
            i += 1

        # Finished
        self.end()
            
    def end(self):
        Animation.end(self)