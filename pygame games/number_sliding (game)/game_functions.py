import pygame, sys, random, os, re
from number_blocks import Block


def check_events(settings, screen, num_list, blocks, blank, button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(settings, event, blocks, blank)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_start_button(settings, screen, num_list, blocks, event, button, blank)


def check_start_button(settings, screen, num_list, blocks, event, button, blank):
    if button.rect.collidepoint(event.pos):
        if not settings.start:
            settings.start=True
            settings.win=False
            settings.t0=pygame.time.get_ticks()
        elif settings.start:
            new_puzzle(settings, screen, num_list, blocks, blank)
            settings.win=False
            settings.t0 = pygame.time.get_ticks()



def check_keydown_events(settings, event, blocks, blank):
    if event.key == pygame.K_q:
        sys.exit()
    elif settings.start and (not settings.win) and event.key == pygame.K_RIGHT:
        cut_last_move(blocks)
        move_right(blocks, blank)
    elif settings.start and (not settings.win) and event.key == pygame.K_LEFT:
        cut_last_move(blocks)
        move_left(blocks, blank)
    elif settings.start and (not settings.win) and event.key == pygame.K_UP:
        cut_last_move(blocks)
        move_up(blocks, blank)
    elif settings.start and (not settings.win) and event.key == pygame.K_DOWN:
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




def check_win(settings, blocks, rank):
    count=0
    for block in blocks:
        if not block.dest and block.num==(block.coord[1]-1)*4+block.coord[0]:
            count+=1
    if count==15:
        #比较用时, 保存最高记录
        timer=round((float(pygame.time.get_ticks()-settings.t0)/1000), 2)
        for n in range(1,4):
            if timer<float(rank.rank[-n]):
                # 检测小数位, 不足则补0
                pat = re.compile(r'\.(\d*)')
                m = pat.search(str(timer))
                if len(m.group(1)) < 2: show_time = str(timer) + '0'
                else: show_time = str(timer)
                #前移排名
                if n==1:
                    rank.rank[-n-2]=rank.rank[-n-1]
                    rank.rank[-n - 1] = rank.rank[-n]
                if n==2: rank.rank[-n - 1] = rank.rank[-n]
                rank.rank[-n]=show_time

                with open('rank.txt','w') as f:
                    f.write(rank.rank[0]+', '+rank.rank[1]+', '+rank.rank[2])
                break
        settings.win=True


def show_win_screen(settings, screen, bg_image):
    screen.blit(bg_image, (settings.edge_gap, settings.edge_gap))
    draw_text(settings, screen, 'Congratulations!', (0, 0, 10), (settings.height//2, settings.height//2), 60)


def draw_text(settings, screen, text, font_color, pos, size):
    font = pygame.font.Font(os.path.join(settings.font_folder, 'AmericanTypewriter.ttc'), size)
    font_image = font.render(text, True, font_color)
    font_rect = font_image.get_rect()
    font_rect.center = pos
    screen.blit(font_image, font_rect)




def new_puzzle(settings, screen, num_list, blocks, blank):
    #仅当逆序数对是偶数时有解, 考虑序对是因为邻换是最简乱序状态; 左右移动空格不改变逆序对奇偶, 上下则相当于做等于列数的邻换, 而只有单空格时最简只能三轮换
    blocks.empty()
    random.shuffle(num_list)
    while parity_odd(num_list):
        random.shuffle(num_list)

    for n in range(1, 16):
        block=Block(settings, screen, n)
        blocks.add(block)
        block.num=num_list[n-1]

    blank.coord=(4,4)
    blank.prep_pos()


def parity_odd(num_list):
    count=0
    copy=num_list.copy()
    for n in range(15):
        for i in range(0, 15-1-n):
            if copy[i]>copy[i+1]:
                copy[i], copy[i+1] = copy[i+1], copy[i]
                count+=1
    if count%2==0: return False
    else: return True




def refresh_background(settings, screen):
    screen.fill((255,255,255))
    adjust=settings.edge_gap-1
    pygame.draw.rect(screen, (0,0,0), pygame.Rect((adjust, adjust), (settings.height-adjust*2, settings.height-adjust*2)), 3)


def update_screen(settings, screen, blocks, button, rank, bg_image, clock, timer):
    refresh_background(settings, screen)
    #显示耗时
    if settings.start:
        pos=(settings.height - settings.edge_gap / 2 + (settings.width - settings.height) / 2, settings.height / 2 - 220)
        #检测小数位, 不足则补0
        pat=re.compile(r'\.(\d*)')
        m=pat.search(str(timer))
        if len(m.group(1)) < 2: show_time=str(timer)+'0'
        else: show_time=str(timer)
        draw_text(settings, screen, show_time, (5,5,90), pos, 30)

    if settings.start:
        for block in blocks:
            block.draw_me()
    button.draw_me()
    rank.draw_me()
    #显示胜利屏幕
    if settings.win:
        show_win_screen(settings, screen, bg_image)
    pygame.display.update()
    clock.tick(60)

