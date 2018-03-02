import os, sys

# set SDL to use the dummy NULL video driver, 
#   so it doesn't need a windowing system.
os.environ["SDL_VIDEODRIVER"] = "dummy"


import pygame.transform


if 1:
    #some platforms might need to init the display for some parts of pygame.
    import pygame.display
    os.putenv('SDL_VIDEODRIVER', 'fbcon')
    pygame.display.init()
    screen = pygame.display.set_mode((1,1))



def quit():
    pygame.quit()

if __name__ == "__main__":
    
    while True:
        for event in pygame.event.get():
            if event.type == USEREVENT+1:
                quit()

