import pygame
import random

class Snake:
    def __init__(self, settings, screen, body_length):
        self.screen=screen
        self.settings=settings
        self.body_length=body_length

        self.new_start()

        self.head_color=pygame.Color(0,128,128,100)
        self.body_color=pygame.Color(128,138,135,100)
        self.food_color=pygame.Color('gold')

        self.food=pygame.Rect((0,0), (self.settings.span, self.settings.span))
        self.regenerate_food()


    def new_start(self):
        #默认从中下开始向上走
        head_pos=(10+self.settings.span*(self.settings.columns//2),10+(self.settings.rows//2+10)*self.settings.span)
        head_size=(self.settings.span, self.settings.span)
        self.head=pygame.Rect(head_pos, head_size)
        self.body=[]
        for n in range(self.body_length):
            body_rect=pygame.Rect((head_pos[0], head_pos[1]+(n+1)*self.settings.span),head_size)
            self.body.append(body_rect)
        self.direction=(0, -self.settings.span)

    def regenerate_food(self):
        #在非蛇区域生成食物
        self.rand_x=random.randint(0, self.settings.columns-1)
        self.rand_y=random.randint(0, self.settings.rows-1)
        food_pos = (10 + self.rand_x * self.settings.span, 10 + self.rand_y * self.settings.span)
        self.food.topleft = food_pos
        while self.food == self.head or self.food in self.body:
            self.rand_x = random.randint(0, self.settings.columns - 1)
            self.rand_y = random.randint(0, self.settings.rows - 1)
            food_pos = (10 + self.rand_x * self.settings.span, 10 + self.rand_y * self.settings.span)
            self.food.topleft = food_pos


    def update(self, scoreboard, eat_music):
        #身体最后一节移到最初并删除 来实现移动, 吃到食物则不删除且加分且重新生成食物
        if self.body:
            self.body.insert(0, self.body[-1].copy())
            x=self.head.centerx - self.body[0].centerx
            y=self.head.centery - self.body[0].centery
            self.body[0].move_ip(x,y)
            self.head.move_ip(self.direction[0], self.direction[1])
            if self.head.centerx==self.food.centerx and self.head.centery==self.food.centery:
                eat_music.play()
                self.increase_score(scoreboard)
                self.regenerate_food()
            else:
                self.body.pop()
        else:
            self.head.move_ip(self.direction[0],self.direction[1])


    def blit_me(self):
        pygame.draw.rect(self.screen, self.head_color, self.head)
        for body in self.body:
            pygame.draw.rect(self.screen, self.body_color, body)
        pygame.draw.rect(self.screen, self.food_color, self.food)


    def increase_score(self, scoreboard):
        #在边缘2倍得分, 角落4倍得分
        x_edge = (self.rand_x == 0 or self.rand_x == self.settings.columns - 1) and 0 < self.rand_y < self.settings.rows - 1
        y_edge = (self.rand_y == 0 or self.rand_y == self.settings.rows - 1) and 0 < self.rand_x < self.settings.columns - 1
        x_corner = self.rand_x == self.rand_y == 0 or (self.rand_x == 0 and self.rand_y == self.settings.rows - 1)
        y_corner = (self.rand_x == self.settings.columns - 1 and self.rand_y == 0) or (
            self.rand_x == self.settings.columns - 1 and self.rand_y == self.settings.rows - 1)

        if x_edge or y_edge:
            scoreboard.score += 2 * self.settings.framerate * 5

        elif x_corner or y_corner:
            scoreboard.score += 4 * self.settings.framerate * 5

        else:
            scoreboard.score += self.settings.framerate * 5

        self.check_high_score(scoreboard)
        scoreboard.prep_score()


    def check_high_score(self, scoreboard):
        if self.settings.game_mode=='normal':
            if scoreboard.score> scoreboard.high_score_normal:
                scoreboard.high_score_normal=scoreboard.score
                scoreboard.prep_high_score()
        elif self.settings.game_mode=='fast':
            if scoreboard.score> scoreboard.high_score_fast:
                scoreboard.high_score_fast=scoreboard.score
                scoreboard.prep_high_score()