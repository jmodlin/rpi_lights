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

    def __init__(self, display):        
        self.display = display
    
    def begin(self):
        self.display.clear()
        for i in range(15):
            for p in self.display.panels:
                p.setPanelColor(Color(255,0,0))
            self.display.update()
            time.sleep(2.0)
            self.display.clear()
            time.sleep(2.0)

    def end(self):
        self.display.clear()
        
