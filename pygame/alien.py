import pygame
from dynamic_sprite import DynamicSprite

#外星人类继承DynamicSprite类
class Alien(DynamicSprite):
    
    #初始化变量
    def __init__(self,screen,settings):
        super().__init__(screen)
        self.screen = screen
        self.settings = settings
    
    #更新外星人的位置
    def update(self,current_time):
        super().update(current_time)
        
        self.rect.x += self.settings.alien_speedx * self.settings.fleet_direction
        
    #检测外星人与屏幕边缘是否发生碰撞
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
