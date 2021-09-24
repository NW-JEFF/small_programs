import pygame, os
from pygame.sprite import Sprite


class Block(Sprite):
    def __init__(self, settings, screen, init_num):
        super().__init__()
        self.settings = settings
        self.screen = screen

        self.font_color = (109, 66, 31)
        self.bg_color = (219, 187, 130)
        #方块对应的数字
        self.num = init_num

        #4x4坐标
        self.coord = ((self.num + 3) % 4 + 1, (self.num - 1) // 4 + 1)
        #方块移动帧数
        self.frame=4
        #每帧动画的路径列表
        self.dest=[]

        self.font = pygame.font.Font(os.path.join(settings.font_folder, 'Charter.ttc'), 52)
        self.rect = pygame.Rect((0, 0), (self.settings.span, self.settings.span))
        self.prep_pos()


    def prep_pos(self):
        #修改位置至格点坐标
        self.rect.x = self.settings.edge_gap + self.settings.gap * self.coord[0] + self.settings.span * (
        self.coord[0] - 1)
        self.rect.y = self.settings.edge_gap + self.settings.gap * self.coord[1] + self.settings.span * (
        self.coord[1] - 1)


    def update(self):
        if self.dest:
            self.rect.topleft=self.dest.pop()




    def draw_me(self):
        #绘制矩形和数字
        pygame.draw.rect(self.screen, self.bg_color, self.rect)

        self.font_image = self.font.render(str(self.num), True, self.font_color)
        self.font_rect = self.font_image.get_rect()
        self.font_rect.centerx, self.font_rect.centery = self.rect.center
        self.screen.blit(self.font_image, self.font_rect)



