
import pygame
pygame.mixer.init()
pygame.mixer.music.load('/media/share/Game_Room.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue