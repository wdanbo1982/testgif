import pygame
from pygame.locals import *

class Sound():
    
    def __init__(self):
    
        pygame.mixer.init()  #��ʼ��������ģ��
        
        
    def bullet_sound(self):
        bullet_sound = pygame.mixer.Sound("bullet_sound.wav")
        bullet_sound.play()

    def bomb_sound(self):
        bomb_sound = pygame.mixer.Sound("bomb.wav")
        bomb_sound.play()
