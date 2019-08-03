#coding:utf-8
#设置类设置初始化数据
class Settings():
    
    def __init__(self):
        
        #设置屏宽、屏高、背景色、游戏名
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = 230,230,230
        self.game_name = "shotting game"
        
        #设置帧频,帧频越小速度越慢
        self.framerate = 60
        
        #设置飞船加载信息
        self.ship_pic = "ship.gif"
        self.ship_w = 50
        self.ship_h = 50
        self.ship_c = 5
        
        #设置飞船的速度,最大飞船数
        self.ship_speed = 20
        self.ship_limit = 3
        
        #设置子弹大小，颜色，速度，最大子弹数
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_speed = 8
        self.bullet_allowed = 3
        
        #设置外星人加载信息
        self.alien_pic = "alien.gif"
        self.alien_w = 50
        self.alien_h = 50
        self.alien_c = 3
        
        #设置外星人x方向的速度,向下的速度，左右运动标志
        self.alien_speedx = 1
        self.fleet_drop_speed = 2
        self.fleet_direction = 1
        
        #设置游戏速度的节奏
        self.speedup_scale = 1.5
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    #初始化游戏设置 
    def initialize_dynamic_settings(self):
            
            self.ship_speed = 5
            self.bullet_speed = 6 
            self.alien_speedx = 1
            
            self.fleet_direction = 1
            
            self.alien_points = 50
         
    #提高设置速度
    def increase_speed(self):
             #self.ship_speed *= self.speedup_scale
             self.bullet_speed *= self.speedup_scale
             self.alien_speedx *= self.speedup_scale  
             
             self.alien_points = int(self.alien_points * self.score_scale)
           
