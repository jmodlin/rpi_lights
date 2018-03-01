
import sys
import pygame
from pygame.locals import *


def quit():
    pygame.quit()

def main():
    pygame.init()

    print 'Starting game loop ...'
    while True:
    
        print pygame.time.get_ticks()

        for ev in pygame.event.get():
            print ('ev ->' + `ev`)
            if ev.type == KEYDOWN:
                    print 'keydown -> ' + ev.key
                    if ev.key == K_q:
                        quit()
        
    pygame.quit()


print ('loading music file ...')
pygame.mixer.init()
pygame.mixer.music.load('/media/share/Game_Room.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)

print ('done')