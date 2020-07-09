import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

'''
def check_events(settings, ship):
    # 响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
                #ship.rect.centerx += 50
                #if ship.rect.centerx > settings.screen_width:
                #    ship.rect.centerx -= 50
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
                #ship.rect.centerx -= 50
                #if ship.rect.centerx < 0:
                    #ship.rect.centerx += 50
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
'''

def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一个新子弹，并加入编组bullets
    # 判断当前子弹数量
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keydown_events(event, ai_settings, screen, stats, ship, bullets):
    # 响应按键按下
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入编组bullets中
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        # 退出程序
        sys.exit()
    elif event.key == pygame.K_t:
        # 暂停游戏或者继续游戏
        if stats.game_active:
            stats.game_active = False
        else:
            stats.game_active = True
        

def check_keyup_events(event, ship):
    # 响应按键松开
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        
def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    # 在玩家单击play按钮时开始游戏
    button_cliend = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_cliend and not stats.game_active:
        # 重置游戏参数
        ai_settings.initialize_dynamic_settings()
        
        # 隐藏光标
        pygame.mouse.set_visible(False)
        
        # 重置游戏统计信息
        stats.reset_stats()
        #sb.prep_score()
        #sb.show_score()
        sb.reset_prep()
        stats.game_active = True
        
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        
        # 创建一群新外星人并将飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
    
def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    # 响应按键和鼠标事件 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 鼠标按下事件
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        
            
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    # 更新屏幕上的图像，并切换到新屏幕
    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    
    # 在飞船和外星人后面重新绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    
    # 显示得分
    sb.show_score()
    
    # 如果游戏处于非活动状态，则绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # 更新子弹的位置
    bullets.update()
    
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    # 检查是否有子弹与外星人发送碰撞
    check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
            
def check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    
    if collisions:
        # 有被击中的外星人
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
            sb.prep_score()
        # 检查是否新记录
        check_high_score(stats, sb)

    # 检查是否需要再次添加外星人
    if len(aliens) == 0:
        # 删除现有子弹并新建新的外星人群
        bullets.empty()
        ai_settings.increase_speed()
        # 提高等级
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)

        
    

def get_number_aliens_x(ai_settings, alien_width):
    # 计算每行可容纳的外星人个数
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
    
def get_number_rows(ai_settings, ship_height, alien_height):
    # 计算屏幕可容纳多少行外星人
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
    
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # 创建一个外星人并将其放在当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    
def create_fleet(ai_settings, screen, ship, aliens):
    # 创建外星人群
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    # 创建外星人群
    for row_number in range(number_rows):
    # 创建第一行外星人
        for alien_number in range(number_aliens_x):
            # 创建第一个外星人并加入当前行
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
    
def check_fleet_edges(ai_settings, aliens):
    # 有外星人到达边缘时采取相应措施
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    # 整群外星人下移，并改变移动方向
    for alien in aliens:
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    # 响应外星人撞到飞船
    # 将 ships_left 减 1
    if stats.ships_left > 0:
        stats.ships_left -= 1
        # 更新记分牌
        sb.prep_ships()
    
        # 清空外星人列表和子弹列表，相当于清屏
        aliens.empty()
        bullets.empty()
    
        # 创建一群新的外星人，并将飞船放置到屏幕底部中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
    
        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    # 更新外星人群中所有的外星人的位置
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)


def check_high_score(stats, sb):
    # 检查是否诞生了新的最高记录
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
