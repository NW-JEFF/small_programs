import pygame
from settings import Settings
from number_blocks import Block
from pygame.sprite import Group
import game_functions as gf




def main():
    pygame.init()
    settings=Settings()
    screen=pygame.display.set_mode((settings.width, settings.height))
    pygame.display.set_caption('数字华容道')
    clock=pygame.time.Clock()

    #构建方块组
    blocks=Group()
    for n in range(15):
        block=Block(settings, screen, n+1)
        blocks.add(block)
    blank=Block(settings, screen, 16)

    gf.new_puzzle(blocks)


    while True:
        gf.check_events(blocks, blank)
        blocks.update()
        gf.update_screen(settings, screen, clock, blocks)



main()