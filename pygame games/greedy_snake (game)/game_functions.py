import pygame, sys, os



def check_events(settings, screen, snake, button_normal, button_normal2, button_fast, button_fast2, scoreboard):
    #不让鼠标等事件影响键盘poll的判定
    for event in pygame.event.get([pygame.QUIT, pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN]):
        if event.type == pygame.QUIT:
            with open('high_score_normal.txt', 'w') as f:
                f.write(str(scoreboard.high_score_normal))
            with open('high_score_fast.txt', 'w') as f:
                f.write(str(scoreboard.high_score_fast))
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y=event.pos
            check_mouse_overlap(settings, screen, mouse_x, mouse_y, button_normal, button_normal2, button_fast, button_fast2)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y=event.pos
            check_button(settings, screen, event, pos_x, pos_y, button_normal, button_normal2, button_fast, button_fast2, scoreboard)
    #若用get会导致快速连拐时一次性修改多个方向再update,可能造成原地180转弯;若加用其他扳机则会造成拐弯不顺,因为get一次性获取所有队列,而poll没拿的仍会在
    event=pygame.event.poll()
    if event.type == pygame.KEYDOWN:
        check_keydown_events(settings, screen, event, snake, button_normal, button_fast, scoreboard)


def check_keydown_events(settings, screen, event, snake, button_normal, button_fast, scoreboard):
    if event.key == pygame.K_q:
        with open('high_score_normal.txt', 'w') as f:
            f.write(str(scoreboard.high_score_normal))
        with open('high_score_fast.txt', 'w') as f:
            f.write(str(scoreboard.high_score_fast))
        sys.exit()
    #暂停
    elif (not settings.game_paused) and (not settings.game_failed) and settings.start_game and event.key == pygame.K_SPACE:
        paused_msg = pygame.font.Font(os.path.join(settings.font_folder, 'AmericanTypewriter.ttc'), 40)
        paused_msg_image = paused_msg.render('PAUSED', True, (50, 50, 150), None)
        paused_msg_rect = paused_msg_image.get_rect()
        paused_msg_rect.center = ((settings.width - settings.height) // 2 + settings.height, 180)
        screen.blit(paused_msg_image, paused_msg_rect)
        settings.game_paused=True
    #解除暂停
    elif settings.game_paused and (not settings.game_failed) and settings.start_game and event.key == pygame.K_SPACE:
        settings.game_paused = False
    #方向控制
    elif settings.start_game and (not settings.game_failed) and (not settings.game_paused):
        if event.key == pygame.K_UP and snake.direction!=(0, settings.span) and snake.direction!=(0, -settings.span):
            snake.direction=(0, -settings.span)
        elif event.key == pygame.K_DOWN and snake.direction!=(0, -settings.span) and snake.direction!=(0, settings.span):
            snake.direction=(0, settings.span)
        elif event.key == pygame.K_RIGHT and snake.direction!=(-settings.span, 0) and snake.direction!=(settings.span,0):
            snake.direction=(settings.span, 0)
        elif event.key == pygame.K_LEFT and snake.direction!=(settings.span, 0) and snake.direction!=(-settings.span,0):
            snake.direction=(-settings.span, 0)
    #死亡界面按空格回到初始界面
    elif settings.game_failed and event.key == pygame.K_SPACE:
        #按空格返回初始界面,后台初始化蛇和分数
        refresh_background(settings, screen)
        button_normal.blit_me()
        button_fast.blit_me()
        scoreboard.restart()
        scoreboard.prep_score()
        snake.new_start()
        settings.game_failed=False
        settings.start_game=False



def check_mouse_overlap(settings, screen, mouse_x, mouse_y, button_normal, button_normal2, button_fast, button_fast2):
    #初始界面鼠标和按钮重合则显示放大版按钮
    if (not settings.start_game):
        if (not button_normal.mouse_on) and button_normal.font_rect.collidepoint(mouse_x,mouse_y):
            refresh_background(settings, screen)
            button_normal2.blit_me()
            button_fast.blit_me()
            button_normal.mouse_on=True
        elif button_normal.mouse_on and (not button_normal2.font_rect.collidepoint(mouse_x,mouse_y)):
            refresh_background(settings, screen)
            button_normal.blit_me()
            button_fast.blit_me()
            button_normal.mouse_on=False

        elif (not button_fast.mouse_on) and button_fast.font_rect.collidepoint(mouse_x,mouse_y):
            refresh_background(settings, screen)
            button_normal.blit_me()
            button_fast2.blit_me()
            button_fast.mouse_on=True
        elif button_fast.mouse_on and (not button_fast2.font_rect.collidepoint(mouse_x,mouse_y)):
            refresh_background(settings, screen)
            button_normal.blit_me()
            button_fast.blit_me()
            button_fast.mouse_on=False


def check_button(settings, screen, event, pos_x, pos_y, button_normal, button_normal2, button_fast, button_fast2, scoreboard):
    #检查初始界面点击按钮
    if (not settings.start_game) and event.button==1:
        if button_normal.mouse_on and button_normal2.font_rect.collidepoint(pos_x,pos_y):
            refresh_background(settings, screen)
            button_normal.mouse_on=False
            settings.game_mode='normal'
            scoreboard.prep_high_score()
            settings.initialize()
            settings.start_game=True
        elif button_fast.mouse_on and button_fast2.font_rect.collidepoint(pos_x,pos_y):
            refresh_background(settings, screen)
            button_fast.mouse_on = False
            settings.game_mode='fast'
            scoreboard.prep_high_score()
            settings.initialize()
            settings.start_game=True



def check_death(settings, screen, snake):
    #死亡检测
    if snake.head.left<10 or snake.head.top<10 or snake.head.right>(10+settings.height-20) or snake.head.bottom>(10+settings.height-20):
        fail_game(settings, screen)
    elif len(snake.body)>4:
        if snake.head.collidelistall(snake.body):
            fail_game(settings, screen)

def fail_game(settings, screen):
    #死亡讯息和死亡状态
    fail_msg1 = pygame.font.Font(os.path.join(settings.font_folder, 'AmericanTypewriter.ttc'), 50)
    fail_msg1_image=fail_msg1.render('YOU DIED', True, (0,0,0), None)
    fail_msg1_rect=fail_msg1_image.get_rect()
    fail_msg1_rect.center=(10 + (settings.height - 20) // 2, (settings.height - 20) // 2-20)
    fail_msg2 = pygame.font.Font(os.path.join(settings.font_folder, 'Arial.ttf'), 30)
    fail_msg2_image=fail_msg2.render('----press [Space] to restart game', True, (0,0,0), None)
    fail_msg2_rect=fail_msg2_image.get_rect()
    fail_msg2_rect.center=(10 + (settings.height - 20) // 2, (settings.height - 20) // 2+15)

    screen.blit(fail_msg1_image, fail_msg1_rect)
    screen.blit(fail_msg2_image, fail_msg2_rect)
    settings.game_failed=True



def refresh_background(settings, screen):
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((9, 9), (settings.height - 18, settings.height - 18)), 3)

def show_help(settings, screen):
    help_msg1 = pygame.font.Font(os.path.join(settings.font_folder, 'Arial.ttf'), 18)
    help_msg1_image = help_msg1.render('Press [Space] to pause', True, (50, 50, 50), None)
    help_msg1_rect = help_msg1_image.get_rect()
    help_msg1_rect.center = ((settings.width - settings.height) // 2 + settings.height, 400)
    screen.blit(help_msg1_image, help_msg1_rect)
    help_msg2 = pygame.font.Font(os.path.join(settings.font_folder, 'Arial.ttf'), 18)
    help_msg2_image = help_msg2.render('Press [q] to quit', True, (50, 50, 50), None)
    help_msg2_rect = help_msg2_image.get_rect()
    help_msg2_rect.center = ((settings.width - settings.height) // 2 + settings.height, 430)
    screen.blit(help_msg2_image, help_msg2_rect)

def update_screen(settings, screen, snake, scoreboard):
    refresh_background(settings, screen)
    show_help(settings, screen)
    snake.blit_me()
    scoreboard.show_score()