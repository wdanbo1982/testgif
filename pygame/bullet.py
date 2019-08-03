import pygame
from pygame.sprite import Sprite

#子弹类，继承父类Sprite
class Bullet(Sprite):
    
    #初始化变量
    def __init__(self,settings,screen,ship):
        super().__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0,0,settings.bullet_width,settings.bullet_height)  #设置子弹矩形
        self.rect.centerx = ship.rect.centerx  #设置子弹x方向的位置在飞船的中间位置
        self.rect.top = ship.rect.top  #设置子弟y方向的位置在飞船的顶端
        self.y = float(self.rect.y)  #设置y方向的浮点数
        self.color = settings.bullet_color  #设置子弹的颜色
        self.speed = settings.bullet_speed  #设置子弹的速度
    
    #更新子弹y方向上的位置
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
        
    
    #绘制子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
