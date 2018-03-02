
import os
import sys
import pygame
from pygame.locals import *


def quit():
    print 'quiting !!'
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

os.environ["SDL_VIDEODRIVER"] = "dummy" # Removes ...

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((1,1))

print ('loading music file ...')
#pygame.mixer.init()
#pygame.mixer.music.load('/media/share/Game_Room.mp3')
#pygame.mixer.music.set_volume(0.8)
#pygame.mixer.music.play()
pygame.time.set_timer(USEREVENT+1, 5000)

while True:
    for event in pygame.event.get():
            if event.type == USEREVENT+1:
                quit()

#while pygame.mixer.music.get_busy(): 
#    pygame.time.Clock().tick(10)
    

#    for event in pygame.event.get():
#        print 'event -> ' + `event`


print ('done')