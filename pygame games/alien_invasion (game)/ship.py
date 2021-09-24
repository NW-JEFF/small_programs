import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings ,screen, ship_size):
        super().__init__()
        self.screen=screen
        a=pygame.image.load('images/ship.bmp')
        self.image=pygame.transform.scale(a, ship_size)

        self.ai_settings=ai_settings

        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.center=float(self.rect.centerx)

        self.moving_right=False
        self.moving_left = False

        self.fire=False
        self.bullet_gap=0

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx=self.center


    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center=self.screen_rect.centerx

