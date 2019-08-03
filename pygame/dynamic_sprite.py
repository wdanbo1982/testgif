import pygame
from pygame.sprite import Sprite
from pygame.locals import *

#动态精灵类继承Sprite类,实现动态的图片，移动图片，设置图片的位置
class DynamicSprite(Sprite): 
     
    #创建构造函数,初始化变量,加载图片
    def __init__(self,surface):  
        super().__init__()  #继承父类构造函数
        self.surface = surface  #设置表层
        self.image = None
        self.frame = -1
        self.first_frame = 0
        self.old_frame = -1
        self.last_time = 0
        
    
    #加载图片，要知道帧图片的宽，高，和列数    
    def load(self,filename,width,height,columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.columns = columns
        self.rect =Rect(0,0,width,height)
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) -1
        
    #循环播放帧图片
    def update(self,current_time,rate = 200):
        
        if current_time > self.last_time + rate:
            #print(current_time)
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time
            
        if self.frame != self.old_frame:
            #print(self.frame,self.old_frame)
            frame_x = (self.frame % self.columns) * self.frame_width
            #print("frame_x:",frame_x,self.frame)
            frame_y = (self.frame // self.columns) * self.frame_height
            #print("frame_y:",frame_y,self.frame)
            rect = Rect(frame_x,frame_y,self.frame_width,self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame
            
    #移动实例
    def _getx(self):
        return self.rect.x
    
    def _setx(self,value):
        self.rect.x = value
    
    pos_x = property(_getx,_setx)
    
    def _gety(self):
        return self.rect.y
    
    def _sety(self,value):
        self.rect.y = value
        
    pos_y = property(_gety,_sety)
    
    #设置实例位置
    def _getpos(self):
        return self.rect.topleft
    
    def _setpos(self,pos):
        self.rect.topleft = pos
        
    position = property(_getpos,_setpos)



    
