#游戏的主程序
import pygame
from settings import Settings
from ship import Ship
import game_fuc as gf
from bullet import Bullet
from game_stats import GameStates
from button import Button
from scoreboard import Scoreboard
from sound import Sound
from bomb import Bomb

pygame.init()  #初始化pygame里的所有模块
settings = Settings()  #实例化一个设置对象
screen = pygame.display.set_mode(
            (settings.screen_width,settings.screen_height))  #设置屏幕大小
pygame.display.set_caption(settings.game_name)  #设置窗口名

play_button = Button(settings,screen,"Play") #创建一个开始游戏按钮实例 

ships = pygame.sprite.Group()  #创建一个飞船精灵组
ship = Ship(screen)  #实例化一个飞船对象
ship.load(settings.ship_pic,settings.ship_w,settings.ship_h,settings.ship_c)
#加载飞船图片
ships.add(ship)  #添加飞船到精灵组

bullets = pygame.sprite.Group()  #创建一个子弹精灵组

aliens = pygame.sprite.Group()  #创建一个外星人精灵组
alien_num_x = gf.get_alien_num_x(settings)  #设置一行多少个外星人
alien_rows = gf.get_alien_rows(settings)  #设置几行外星人
gf.create_fleet(settings,screen,aliens,alien_num_x,alien_rows)  #创建一群外星人

stats = GameStates(settings) #创建游戏信息实例

sb = Scoreboard(settings,screen,stats)  #创建一个记分牌

sound = Sound()  #创建声音实例

bomb = Bomb(screen)  #创建爆炸实例
# ~ bomb.load("bomb.gif",50,50,5)
# ~ bombs = pygame.sprite.Group()
# ~ bombs.add(bomb)

framerate = pygame.time.Clock()  #创建一个时钟 

#开始游戏
while True:   
    framerate.tick(settings.framerate)  #设置帧频
    ticks = pygame.time.get_ticks()  #获取当前时间,帧频越小前后的时间差越大
    
    gf.check_events(settings,screen,sb,ship,bullets,stats,play_button,aliens,alien_num_x,alien_rows,sound)  #监听事件
    
    screen.fill((settings.bg_color))  #设置背景色,放循环体内是因为每次都要重绘屏幕
    
    
    
    if stats.game_active:
        gf.group_update(ticks,screen,settings,stats,ship,ships,bullets,aliens,
                    alien_num_x,alien_rows,play_button,sb,sound,bomb)  #设置精灵组


    
    #如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
        
    
    pygame.display.update()

    
