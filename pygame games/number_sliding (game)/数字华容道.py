import pygame, os
from settings import Settings
from number_blocks import Block
from buttons import Button
from time_rank import Rank
from pygame.sprite import Group
import game_functions as gf




def main():
    pygame.init()
    settings=Settings()
    screen=pygame.display.set_mode((settings.width, settings.height))
    pygame.display.set_caption('数字华容道')
    clock=pygame.time.Clock()

    #创建方块编组和数字
    num_list=list(range(1,16))
    blocks=Group()
    blank=Block(settings, screen, 16)
    gf.new_puzzle(settings, screen, num_list, blocks, blank)

    button=Button(settings, screen)
    button.draw_me()

    rank=Rank(settings, screen)
    rank.draw_me()

    #初始化计时器
    timer=0

    #加载图片素材
    bg_image_original=pygame.image.load(os.path.join(settings.game_folder, '遮布.png')).convert_alpha()
    bg_image = pygame.transform.scale(bg_image_original, (settings.height-2*settings.edge_gap, settings.height-2*settings.edge_gap))


    while True:
        gf.check_events(settings, screen, num_list, blocks, blank, button)

        if settings.start and (not settings.win):
            blocks.update()
            gf.check_win(settings, blocks, rank)
            timer=round((float(pygame.time.get_ticks()-settings.t0)/1000), 2)


        gf.update_screen(settings, screen, blocks, button, rank, bg_image, clock, timer)



main()