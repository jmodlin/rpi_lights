import os, sys
from pygame.locals import *
import pygame.display
# set SDL to use the dummy NULL video driver, 
#   so it doesn't need a windowing system.
os.environ["SDL_VIDEODRIVER"] = "aalib"
os.putenv('SDL_VIDEODRIVER', 'fbcon')

if 1:
    #some platforms might need to init the display for some parts of pygame.

    
    pygame.display.init()
    #screen = pygame.display.set_mode((1,1))
    pygame.time.set_timer(USEREVENT+1, 5000)

def quit():
    print ('quiting!!')
    pygame.quit()

if __name__ == "__main__":
    
    print ('starting game loop ...')
    while True:
        for event in pygame.event.get():
            if event.type == USEREVENT+1:
                quit()

