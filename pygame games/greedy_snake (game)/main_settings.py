import pygame, os

class Settings:
    def __init__(self):
        self.width=1070
        self.height=860
        self.rows=40
        self.columns=40
        self.span=int((self.height-20)/self.rows)

        #开始游戏对应初始界面扳机, 游戏失败对应失败画面扳机, 暂停对应暂停扳机
        self.start_game=False
        self.game_failed=False
        self.game_paused=False
        self.bg_color=pygame.Color('white')
        #根据模式挑战帧率、存取历史最高分
        self.game_mode=''

        #文件夹保存地点
        self.game_folder=os.path.dirname(__file__)
        self.font_folder=os.path.join(self.game_folder, 'Fonts')

    def initialize(self):
        if self.game_mode=='normal':
            self.framerate=15
        elif self.game_mode=='fast':
            self.framerate=25

