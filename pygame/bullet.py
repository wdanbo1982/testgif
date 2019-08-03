import pygame
from pygame.sprite import Sprite

#�ӵ��࣬�̳и���Sprite
class Bullet(Sprite):
    
    #��ʼ������
    def __init__(self,settings,screen,ship):
        super().__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0,0,settings.bullet_width,settings.bullet_height)  #�����ӵ�����
        self.rect.centerx = ship.rect.centerx  #�����ӵ�x�����λ���ڷɴ����м�λ��
        self.rect.top = ship.rect.top  #�����ӵ�y�����λ���ڷɴ��Ķ���
        self.y = float(self.rect.y)  #����y����ĸ�����
        self.color = settings.bullet_color  #�����ӵ�����ɫ
        self.speed = settings.bullet_speed  #�����ӵ����ٶ�
    
    #�����ӵ�y�����ϵ�λ��
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
        
    
    #�����ӵ�
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
