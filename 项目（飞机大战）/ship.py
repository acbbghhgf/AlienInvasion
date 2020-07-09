import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    # 管理飞船部分行为
    def __init__(self, ai_settings, screen):
        # 继承初始化
        super(Ship, self).__init__()
        # 初始化飞船并设置其初始位置
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # 将每艘新产生的飞船放在屏幕底部正中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        # 根据移动标志调整位置
        # 更新飞船的 center值而不是rect值
        '''
        if self.moving_right:
            #self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
            if self.center > self.screen_rect.width:
                self.center -= self.ai_settings.ship_speed_factor
        if self.moving_left:
            #self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor
            if self.center < 0:
                self.center += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        '''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        
    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        # 居中飞船位置
        self.center = self.screen_rect.centerx