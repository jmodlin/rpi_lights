
import pygame
from pygame.locals import *

def main():
    pygame.init()
    i = 0

    while True:
        ev = pygame.event.poll()

        if ev.type == QUIT
            break
        
        if event.type == KEYDOWN:
                key_name = pygame.key.name(event.key)
                print key_name
    pygame.quit()

main()
