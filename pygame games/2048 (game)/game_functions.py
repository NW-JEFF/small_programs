import pygame, sys, random


def check_events(blocks, blank):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, blocks, blank)


def check_keydown_events(event, blocks, blank):
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_RIGHT:
        cut_last_move(blocks)
        move_right(blocks, blank)
    if event.key == pygame.K_LEFT:
        cut_last_move(blocks)
        move_left(blocks, blank)
    if event.key == pygame.K_UP:
        cut_last_move(blocks)
        move_up(blocks, blank)
    if event.key == pygame.K_DOWN:
        cut_last_move(blocks)
        move_down(blocks, blank)


def move_right(blocks, blank):
    # 左边有方块就为其添加帧路径
    if blank.coord[0] - 1 > 0:
        for block in blocks:
            if block.coord == (blank.coord[0] - 1, blank.coord[1]):
                block.coord = blank.coord
                # 倒着添加每帧移动路径
                frame_dist = (blank.rect.x - block.rect.x) / block.frame
                for n in range(block.frame):
                    block.dest.append((blank.rect.x - frame_dist * n, blank.rect.y))
                blank.coord = (blank.coord[0] - 1, blank.coord[1])
                blank.prep_pos()
                break

def move_left(blocks, blank):
    # 右边有方块就为其添加帧路径
    if blank.coord[0] + 1 < 5:
        for block in blocks:
            if block.coord == (blank.coord[0] + 1, blank.coord[1]):
                block.coord = blank.coord
                # 倒着添加每帧移动路径
                frame_dist = (blank.rect.x - block.rect.x) / block.frame
                for n in range(block.frame):
                    block.dest.append((blank.rect.x - frame_dist * n, blank.rect.y))
                blank.coord = (blank.coord[0] + 1, blank.coord[1])
                blank.prep_pos()
                break

def move_up(blocks, blank):
    # 下边有方块就为其添加帧路径
    if blank.coord[1] + 1 < 5:
        for block in blocks:
            if block.coord == (blank.coord[0], blank.coord[1]+1):
                block.coord = blank.coord
                # 倒着添加每帧移动路径
                frame_dist = (blank.rect.y - block.rect.y) / block.frame
                for n in range(block.frame):
                    block.dest.append((blank.rect.x, blank.rect.y - frame_dist * n))
                blank.coord = (blank.coord[0], blank.coord[1]+1)
                blank.prep_pos()
                break

def move_down(blocks, blank):
    # 左边有方块就为其添加帧路径
    if blank.coord[1] - 1 > 0:
        for block in blocks:
            if block.coord == (blank.coord[0], blank.coord[1]-1):
                block.coord = blank.coord
                # 倒着添加每帧移动路径
                frame_dist = (blank.rect.y - block.rect.y) / block.frame
                for n in range(block.frame):
                    block.dest.append((blank.rect.x, blank.rect.y - frame_dist * n))
                blank.coord = (blank.coord[0], blank.coord[1]-1)
                blank.prep_pos()
                break


def cut_last_move(blocks):
    #若还有移动中的方块, 使其立即到位
    for block in blocks:
        if block.dest:
            # 坐标早已更新,因此可以直接修改位置并情况路径列表
            block.prep_pos()
            block.dest.clear()









def new_puzzle(blocks):
    num_list=list(range(15))
    random.shuffle(num_list)
    for block in blocks:
        block.num=num_list.pop()+1


def refresh_background(settings, screen):
    screen.fill((255,255,255))
    adjust=settings.edge_gap-1
    pygame.draw.rect(screen, (0,0,0), pygame.Rect((adjust, adjust), (settings.height-adjust*2, settings.height-adjust*2)), 3)


def update_screen(settings, screen, clock, blocks):
    refresh_background(settings, screen)
    for block in blocks:
        block.draw_me()
    pygame.display.update()
    clock.tick(60)

