#主程的函数
import pygame
from sys import exit
from bullet import Bullet
from alien import Alien
from time import sleep
from pygame.locals import *


#按键响应
def check_keydown_event(event,settings,screen,ship,bullets,sound):
    
    #当按下左右箭头键时，设置移动标志为真
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    
    #当按下空格键时，发射子弹  
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings,screen,ship,bullets)
        sound.bullet_sound()
        
#发射子弹，实例化一个子弹，并把子弹添加到子弹组，子弹数小于最大子弹数          
def fire_bullet(settings,screen,ship,bullets):
    if len(bullets) < settings.bullet_allowed:
        bullet = Bullet(settings,screen,ship)
        bullets.add(bullet)


#松开响应
def check_keyup_event(event,ship):
    
    #当松开左右箭头键时，则设置移动标志为假
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left= False

#响应Play按钮事件
def check_play_button(settings,screen,stats,sb,play_button,ship,aliens,bullets,
        alien_num_x,alien_rows,mouse_x,mouse_y):
    #单击Play按钮开始游戏
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)  #隐藏光标
        settings.initialize_dynamic_settings()  #重置游戏初始设置
        stats.reset_stats()  #重置飞船信息
        stats.game_active = True  #开始游戏
        
        sb.prep_score()   #重置记分牌
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        
        aliens.empty()  #清空外星人
        bullets.empty()  #清空子弹
        
        create_fleet(settings,screen,aliens,alien_num_x,alien_rows)  #创建新的外星人
        ship.center_ship()  #飞船重置底部居中

#监听鼠标和键盘事件
def check_events(settings,screen,sb,ship,bullets,stats,play_button,aliens,alien_num_x,alien_rows,sound):
    
    #监听事件
    for event in pygame.event.get():
        
        #按关闭图标退出游戏
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        #鼠标单击Play按钮响应事件
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos() #获取鼠标坐标点
            check_play_button(settings,screen,stats,sb,play_button,ship,aliens,bullets,alien_num_x,alien_rows,mouse_x,mouse_y)
        
        #按键响应事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,settings,screen,ship,bullets,sound)
        
        #松开响应事件
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)
            
    key = pygame.key.get_pressed()  #获取按键值
    
    #按Esc键退出游戏
    if key[pygame.K_ESCAPE]:
        exit()
    
    # ~ #控制飞船左右移动
    # ~ if key[pygame.K_RIGHT]:
        # ~ if ship.rect.right < screen_rect.right:
            # ~ ship.speedx += ship.speed
    # ~ if key[pygame.K_LEFT]:
        # ~ if ship.speedx > 0 :
            # ~ ship.speedx -= ship.speed
    
#更新子弹
def bullets_update(bullets):
    
    #更新子弹的位置
    bullets.update()  
    #删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

#设置外星人一行的个数
def get_alien_num_x(settings):
    available_space_x = settings.screen_width - ( 2 * settings.alien_w)
    alien_num_x = int(available_space_x / ( 2 * settings.alien_w))
    return alien_num_x

#设置外星人的行数
def get_alien_rows(settings):
    available_space_y = settings.screen_height - 3 * settings.alien_h - settings.ship_h
    alien_rows = int(available_space_y / ( 2 * settings.alien_h))
    return alien_rows

#创建外星人
def create_alien(screen,settings,aliens,alien_num,alien_rows):
    alien = Alien(screen,settings)
    alien.load(settings.alien_pic,settings.alien_w,settings.alien_h,settings.alien_c)
    alien.pos_x = settings.alien_w + 2 * settings.alien_w * alien_num
    alien.pos_y = settings.alien_h  + 2 * settings.alien_h * alien_rows
    aliens.add(alien)

#创建一群外星人
def create_fleet(settings,screen,aliens,alien_num_x,alien_rows):
    for alien_rows in range(alien_rows):
        for alien_num in range(alien_num_x):
            create_alien(screen,settings,aliens,alien_num,alien_rows)
 
#检测外星人是否与屏幕边缘相撞
def check_fleet_edges(settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings,aliens)
            break

#外星人与屏幕边缘相撞，所有外星人向下移动,并改变它们的方向
def change_fleet_direction(settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1

#检测子弹与外星人的碰撞
def check_bullet_alien_collisions(settings,screen,bullets,aliens,
                        alien_num_x,alien_rows,sb,stats,sound,bomb):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True) #碰撞检测

    
    if collisions:
        
        for aliens in collisions.values():
            stats.score += settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)  #检查最高分
        
        sound.bomb_sound()
        
        
        # ~ for alien in aliens:
            # ~ bomb.rect = Rect(alien.rect.x,alien.rect.y,50,50)
            # ~ print(bomb.rect)
            # ~ #if bomb.visible:
                
            # ~ bombs.update(ticks)
            # ~ bombs.draw(screen)
          
        bomb.visible = True
        for alien in aliens:
            bomb.set_pos(alien.rect.x,alien.rect.y)
            if bomb.visible:
                bomb.update()
 
            
            
            
        
    #如果外星人为空，删除现有的所有子弹并新建一群外星人
    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()
        create_fleet(settings,screen,aliens,alien_num_x,alien_rows)
        
        stats.level += 1
        sb.prep_level()
   
        
#响应外星人撞到飞船
def ship_hit(settings,stats,screen,sb,ship,aliens,bullets,alien_num_x,alien_rows):
    
    if stats.ships_left >0:
        stats.ships_left -= 1  #飞船总数减1
        
        sb.prep_ships()
        
        aliens.empty()  #清空外星人
        bullets.empty()  #清空子弹列表
    
        create_fleet(settings,screen,aliens,alien_num_x,alien_rows)  #创建一群新的外星人
        ship.center_ship()  #重置飞船到底端中心位置
    
        sleep(1)  #暂停
    
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

#检测外星人到屏幕底部    
def check_aliens_bottom(settings,stats,screen,sb,ship,aliens,bullets,alien_num_x,alien_rows):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings,stats,screen,sb,ship,aliens,bullets,alien_num_x,alien_rows)
            break

#检查是否诞生了新的最高分
def check_high_score(stats,sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
    

#设置精灵组
def group_update(ticks,screen,settings,stats,ship,ships,bullets,aliens,
                    alien_num_x,alien_rows,play_button,sb,sound,bomb):
    
    sb.show_score(ticks)  #显示计分牌
    
    bullets_update(bullets)  #更新子弹
    check_bullet_alien_collisions(settings,screen,bullets,aliens,
                                alien_num_x,alien_rows,sb,stats,sound,bomb)  #检测子弹与外星人的碰撞
        
    ships.update(ticks,settings)  #更新飞船图
    ships.draw(screen)  #绘制飞船
    
    check_fleet_edges(settings,aliens)  #查测外星人是否与屏幕边缘相撞，如果相撞则更新整个外星人的位置
    aliens.update(ticks)  # 更新外星人
    aliens.draw(screen)  #绘制外星人
    
    # ~ if bomb.visible:
        # ~ bombs.update(ticks,settings)
        # ~ bombs.draw(screen)


   
    #飞船与外星人碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(settings,stats,screen,sb,ship,aliens,bullets,alien_num_x,alien_rows)
        #print("ship hit")
    
    #外星人碰到屏幕底部
    check_aliens_bottom(settings,stats,screen,sb,ship,aliens,bullets,alien_num_x,alien_rows)
 
    

