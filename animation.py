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
        self.display.clear()
        
    def end(self):
        self.display.clear()
        


# Main program logic follows:
if __name__ == '__main__':
        
	print ('Press Ctrl-C to quit.')

                