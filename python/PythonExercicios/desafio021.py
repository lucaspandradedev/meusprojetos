import pygame
pygame.mixer.init()
pygame.mixer.music.load('de021.mp3')
pygame.mixer.music.play(loops=0,start=0.0)
while(pygame.mixer.music):pass



'''pygame.init()
pygame.mixer.music.load('17.mp3')
pygame.mixer.music.play(loops=2,start=110.0)
while(pygame.mixer.music):pass'''

'''import pygame
pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass'''