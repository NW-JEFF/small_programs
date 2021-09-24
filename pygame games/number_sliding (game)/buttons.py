import pygame, os

class Button():
    def __init__(self, settings, screen):
        self.settings=settings
        self.screen=screen

        self.font = pygame.font.Font(os.path.join(settings.font_folder, 'AmericanTypewriter.ttc'), 32)

        self.image=self.font.render('Start', True, (0,0,0))
        self.rect=self.image.get_rect()

        self.rect.center=(self.settings.height-self.settings.edge_gap/2+(self.settings.width-self.settings.height)/2, self.settings.height/2+90)


    def draw_me(self):
        frame=pygame.Rect((self.rect.x-5,self.rect.y-5),(self.rect.w+10, self.rect.h+10))
        pygame.draw.rect(self.screen, (0, 0, 0), frame, 2)
        self.screen.blit(self.image, self.rect)


