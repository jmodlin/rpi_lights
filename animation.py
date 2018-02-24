# Stock libraries
import time
import random
import signal
import sys

# Custom objects
from panel import *
from display import *

class Animation:

    def __init__(self, display):
        self.display = display
        
    def begin(self):
        print ('Starting ' + self.__class__.__name__ + ' animation')
        self.display.setBrightness(255)
        self.display.clear()
        
    def end(self):
        print ('Finishing ' + self.__class__.__name__ + ' animation')
        b = self.display.getBrightness()
        for i in range(b, -1, -1):
            self.display.setBrightness(i)
            self.display.update()
            time.sleep(0.007)
        self.display.clear()
        


# Main program logic follows:
if __name__ == '__main__':
        
	print ('Press Ctrl-C to quit.')

                