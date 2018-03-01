
import sys
import pygame
from pygame.locals import *


def quit():
    sys.exit()

def main():
    pygame.init()
    i = 0

    while True:
        ev = pygame.event.poll()
        
        if ev.type == KEYDOWN:
                key_name = pygame.key.name(ev.key)
                if key_name == 'q':
                    quit()
    pygame.quit()

main()
