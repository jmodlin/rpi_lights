
import sys
import pygame
from pygame.locals import *


def quit():
    pygame.quit()

def main():
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

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((1,1))

print ('loading music file ...')
pygame.mixer.init()
pygame.mixer.music.load('/media/share/Game_Room.mp3')
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)
    for event in pygame.event.get():
        print event


print ('done')