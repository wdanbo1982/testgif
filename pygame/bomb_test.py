from dynamic_sprite import DynamicSprite
from pygame.locals import *
import pygame

class BombTest(DynamicSprite):
    
    def __init__(self,screen):
        super().__init__(screen)
        
        self.screen = screen
        self.framerate = pygame.time.Clock()
        self.visible = True
    
    def load(self,filename,width,height,columns):
        super().load(filename,width,height,columns)
        
    def update(self,current_time,rate = 200):
        super().update(current_time)
        #print(self.frame)
        
        # ~ if self.frame == 4:
            # ~ self.visible = False
            
            
        for i in range(5):
            
            self.framerate.tick(30)
            self.frame = i
            print(self.frame)
            
            #if self.frame != 4:
            frame_x = (self.frame % self.columns) * self.frame_width
            print("frame_x:",frame_x,self.frame)
            frame_y = (self.frame // self.columns) * self.frame_height
            print("frame_y:",frame_y,self.frame)
            rect = Rect(frame_x,frame_y,self.frame_width,self.frame_height)
            self.image = self.master_image.subsurface(rect)
           
            
                
              
