    
import os
import pygame
from pygame.locals import *

drivers = ('directfb', 'fbcon', 'svgalib')


def quit():
    if pipe:
        pipe.close()
        print ('Closing pipe')
    print ('quiting!!')
    #pygame.quit()


found = False
for driver in drivers:
    print "Trying \'" + driver + "\'",
    if not os.getenv('SDL_VIDEODRIVER'):
        os.putenv('SDL_VIDEODRIVER',driver)
    try:
        pygame.display.init()
    except pygame.error:
        print 'failed'
        continue
    found = True
    break
if not found:
    raise Exception('No suitable video driver found.')


print "success"
size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

pygame.time.set_timer(USEREVENT+1, 5000)

# Set up pipe queue
pipe_path = "/tmp/lights"
if not os.path.exists(pipe_path):
    os.mkfifo(pipe_path)
pipe_fd = os.open(pipe_path, os.O_RDONLY | os.O_NONBLOCK)

pipe = os.fdopen(pipe_fd)

print 'Starting game loop ...'
while True:

    # Check pipe queue for message ...
    message = pipe.read()
    if message:
        print("Message received: '%s'" % message)

    for event in pygame.event.get():

        print ('ev ->' + `event`)
        if event.type == USEREVENT+1:
                quit()
        if event.type == KEYDOWN:
                print 'keydown -> ' + event.key
                if event.key == K_q:
                    quit()


    
if pipe:
    print 'end .. closing pipe'
    pipe.close()
