
import sys
import pygame
from pygame.locals import *


def quit():
    pygame.quit()

def main():
    pygame.init()

    print 'Starting game loop ...'
    while True:
    
        for ev in pygame.event.get():
            print ('ev ->' + `ev`)
            if ev.type == KEYDOWN:
                    print 'keydown -> ' + ev.key
                    if ev.key == K_q:
                        quit()
        
    pygame.quit()

main()
