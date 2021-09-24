import pygame, sys


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(screen, clock):
    screen.fill((255,255,255))
    pygame.display.update()
    clock.tick(60)