
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
            if ev.type == KEYDOWN:
                    key_name = pygame.key.name(ev.key)
                    print 'keydown -> ' + `key_name`
                    if key_name == 'q':
                        quit()
        
    pygame.quit()

main()
