from dynamic_sprite import DynamicSprite
from pygame.locals import *


#飞船类继承DynamicSprite类
class Ship(DynamicSprite):  
    
    #创建构造函数
    def __init__(self,screen):   
        super().__init__(screen)  #继承父类的构造函数
        self.screen = screen
        self.screen_rect = screen.get_rect()  #获取屏幕矩形
        self.moving_right = False  #设置移动左边标志
        self.moving_left = False  #设置移动右边标志
     
    #加载飞船，并重置飞船的初始位置
    def load(self,filename,width,height,columns):
        super().load(filename,width,height,columns)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.rect = Rect(self.rect.left,self.rect.top,width,height)
        #self.position = (self.rect.left,self.rect.top)
    
    #更新飞船位置
    def update(self,current_time,settings):
        super().update(current_time)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.pos_x += settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.pos_x -= settings.ship_speed
    
    #重置飞船到中心位置
    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
