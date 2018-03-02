    
import os
import pygame

drivers = ('directfb', 'fbcon', 'svgalib')


def quit():
    print ('quiting!!')
    pygame.quit()

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

print 'Starting game loop ...'
while True:

    print pygame.time.get_ticks()

    for ev in pygame.event.get():
        print ('ev ->' + `ev`)
        if ev.type == KEYDOWN:
                print 'keydown -> ' + ev.key
                if ev.key == K_q:
                    quit()
    
 