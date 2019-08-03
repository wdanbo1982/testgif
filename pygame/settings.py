#coding:utf-8
#���������ó�ʼ������
class Settings():
    
    def __init__(self):
        
        #�����������ߡ�����ɫ����Ϸ��
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = 230,230,230
        self.game_name = "shotting game"
        
        #����֡Ƶ,֡ƵԽС�ٶ�Խ��
        self.framerate = 60
        
        #���÷ɴ�������Ϣ
        self.ship_pic = "ship.gif"
        self.ship_w = 50
        self.ship_h = 50
        self.ship_c = 5
        
        #���÷ɴ����ٶ�,���ɴ���
        self.ship_speed = 20
        self.ship_limit = 3
        
        #�����ӵ���С����ɫ���ٶȣ�����ӵ���
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_speed = 8
        self.bullet_allowed = 3
        
        #���������˼�����Ϣ
        self.alien_pic = "alien.gif"
        self.alien_w = 50
        self.alien_h = 50
        self.alien_c = 3
        
        #����������x������ٶ�,���µ��ٶȣ������˶���־
        self.alien_speedx = 1
        self.fleet_drop_speed = 2
        self.fleet_direction = 1
        
        #������Ϸ�ٶȵĽ���
        self.speedup_scale = 1.5
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    #��ʼ����Ϸ���� 
    def initialize_dynamic_settings(self):
            
            self.ship_speed = 5
            self.bullet_speed = 6 
            self.alien_speedx = 1
            
            self.fleet_direction = 1
            
            self.alien_points = 50
         
    #��������ٶ�
    def increase_speed(self):
             #self.ship_speed *= self.speedup_scale
             self.bullet_speed *= self.speedup_scale
             self.alien_speedx *= self.speedup_scale  
             
             self.alien_points = int(self.alien_points * self.score_scale)
           
