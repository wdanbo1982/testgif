import pygame
from pygame.locals import *


class Bomb(object):
    
    def __init__(self,screen):
        
        self.screen = screen
        
   
        self.image = pygame.image.load("bomb.gif").convert_alpha()
        image_rect = self.image.get_rect()
        self.rect = pygame.Rect(0,0,50,50)
        
        self.position = [200,0]
        
        self.visible = False
        self.last_time = 0
        self.framerate = pygame.time.Clock()
    def set_pos(self,x,y):
        self.position[0] = x
        self.position[1] = y
        
 
    def update(self):
        for i in range(5):
          
            #self.framerate.tick(6)
            self.rect.x = i * 50
            #print(self.rect.x,i)
            if self.rect.x >= 200:
                self.rect.x = 0
                self.visible = False
                #print(self.visible)
            self.rect = Rect(self.rect.x,0,50,50)
            self.screen.blit(self.image,(self.position[0],self.position[1]),self.rect)
            #pygame.display.flip()
            
    
