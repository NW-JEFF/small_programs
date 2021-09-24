import pygame, os
from main_settings import Settings
import game_functions as gf
from snake import Snake
from button import Button
from scoreboard import Scoreboard
#import time

def main():
    pygame.init()
    settings=Settings()
    screen=pygame.display.set_mode((settings.width, settings.height))
    pygame.display.set_caption('贪吃蛇')
    clock=pygame.time.Clock()

    snake=Snake(settings, screen, 2)
    scoreboard=Scoreboard(settings, screen)

    eat_music=pygame.mixer.Sound(os.path.join(settings.game_folder,'eat.wav'))


    #更新初始界面
    gf.refresh_background(settings, screen)

    font_pos1 = (10 + (settings.height - 20) // 2, (settings.height - 20) // 2 - 40)
    font_pos2 = (10 + (settings.height - 20) // 2, (settings.height - 20) // 2 + 40)
    button_normal = Button(settings, screen, 'AmericanTypewriter.ttc', 40, (61, 133, 210), None, font_pos1)
    button_fast = Button(settings, screen, 'AmericanTypewriter.ttc', 40, (171, 63, 60), None, font_pos2)
    button_normal2 = Button(settings, screen, 'AmericanTypewriter.ttc', 42, (91, 163, 235), None, (font_pos1[0],font_pos1[1]-3))
    button_fast2 = Button(settings, screen, 'AmericanTypewriter.ttc', 42, (196, 93, 90), None, (font_pos2[0],font_pos2[1]-3))
    button_normal2.draw_msg('Normal')
    button_fast2.draw_msg('Fast')
    button_normal.draw_msg('Normal')
    button_normal.blit_me()
    button_fast.draw_msg('Fast')
    button_fast.blit_me()

    #start = time.clock()

    while True:

        gf.check_events(settings, screen, snake, button_normal, button_normal2, button_fast, button_fast2, scoreboard)

        if settings.start_game and (not settings.game_failed) and (not settings.game_paused):
            snake.update(scoreboard, eat_music)
            gf.update_screen(settings, screen, snake, scoreboard)
            gf.check_death(settings, screen, snake)

        pygame.display.update()
        if settings.game_mode:
            clock.tick(settings.framerate)

        #print(time.clock()-start)
        #start=time.clock()

main()