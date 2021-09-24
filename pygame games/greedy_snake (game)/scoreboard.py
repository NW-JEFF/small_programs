import pygame,os

class Scoreboard:
    def __init__(self, settings, screen):
        self.settings=settings
        self.screen=screen

        try:
            with open('high_score_normal.txt', 'x') as f:
                f.write('0')
        except FileExistsError:
            pass
        try:
            with open('high_score_fast.txt', 'x') as f:
                f.write('0')
        except FileExistsError:
            pass

        self.high_score_normal=int(open('high_score_normal.txt').readline())
        self.high_score_fast = int(open('high_score_fast.txt').readline())
        self.restart()

        self.font=pygame.font.Font(os.path.join(self.settings.font_folder, 'AmericanTypewriter.ttc'), 30)

        self.prep_score()
        self.prep_high_score()

    def restart(self):
        self.score=0


    def prep_score(self):
        self.score_image=self.font.render('Score: '+'{:,}'.format(self.score), True, (0, 0, 0), None)
        self.score_image_rect=self.score_image.get_rect()
        self.score_image_rect.top=60
        self.score_image_rect.centerx=(self.settings.width-self.settings.height)//2+self.settings.height

    def prep_high_score(self):
        if self.settings.game_mode=='normal':
            self.high_score_image = self.font.render('Max: ' + '{:,}'.format(self.high_score_normal), True, (0, 0, 0), None)
            self.high_score_image_rect = self.high_score_image.get_rect()
            self.high_score_image_rect.top = 100
            self.high_score_image_rect.centerx = (self.settings.width - self.settings.height) // 2 + self.settings.height
        elif self.settings.game_mode=='fast':
            self.high_score_image = self.font.render('Max: ' + '{:,}'.format(self.high_score_fast), True, (0, 0, 0), None)
            self.high_score_image_rect = self.high_score_image.get_rect()
            self.high_score_image_rect.top = 100
            self.high_score_image_rect.centerx = (self.settings.width - self.settings.height) // 2 + self.settings.height
        else:
            self.high_score_image = self.font.render('Max: 0', True, (0, 0, 0), None)
            self.high_score_image_rect = self.high_score_image.get_rect()
            self.high_score_image_rect.top = 100
            self.high_score_image_rect.centerx = (self.settings.width - self.settings.height) // 2 + self.settings.height


    def show_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)