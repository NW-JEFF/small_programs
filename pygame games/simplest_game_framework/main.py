import pygame
import game_functions as gf




def main():
    pygame.init()
    screen=pygame.display.set_mode((800, 600))
    pygame.display.set_caption('test')
    clock=pygame.time.Clock()


    while True:
        gf.check_events()
        gf.update_screen(screen, clock)



main()