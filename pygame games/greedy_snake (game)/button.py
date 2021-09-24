import pygame,os
import pygame.freetype

class Button():
    def __init__(self, settings, screen, font_style, size, font_color, bg_color, font_center):
        self.settings=settings
        self.screen=screen
        self.mouse_on=False

        self.font_color=font_color
        self.bg_color=bg_color
        self.font_center=font_center

        self.font=pygame.font.Font(os.path.join(self.settings.font_folder,'{}'.format(font_style)), size)

    def draw_msg(self, msg):
        self.font_image=self.font.render(msg, True, self.font_color, self.bg_color)
        self.font_rect=self.font_image.get_rect()
        self.font_rect.centerx,self.font_rect.centery=self.font_center


    def blit_me(self):
        self.screen.blit(self.font_image, self.font_rect)




