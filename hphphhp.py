import pygame as pg
import sys

pg.init()
f_sys = pg.font.SysFont('arial', 20)

win = pg.display.set_mode((800, 600))
win_rect = win.get_rect()
background = pg.image.load("fonorm.png").convert()  # фон типа пол
background_rect = background.get_rect(topleft=(320, -270))  # такое положение обязательно, почему оно такое в душе не еб
background2 = pg.image.load("2fon.png")  # фонарики ......:.>

player = pg.image.load('pixil-frame-0 (2).png')

komnata1 = pg.image.load('komnata.png')
komnata1_rect = komnata1.get_rect(topleft=(480, -135))

FPS = 60 # число кадров в секунду
clock = pg.time.Clock()

player_rect = player.get_rect(center=(400, 300))

while 1:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    kpressed = pg.key.get_pressed()

    print(komnata1_rect.bottom)
    print(player_rect.top)

    if kpressed[pg.K_UP]:
        if background_rect.top!=player_rect.top:
            copy_rect = komnata1_rect.copy()
            copy_rect.y += 5
            can = pg.Rect.colliderect(player_rect, copy_rect)
            if can is False:
                background_rect.y += 5
                komnata1_rect.y += 5

    if kpressed[pg.K_DOWN]:
        if  background_rect.bottom != player_rect.bottom:
            copy_rect = komnata1_rect.copy()
            copy_rect.y -= 5
            can = pg.Rect.colliderect(player_rect, copy_rect)
            if can is False:
                background_rect.y -= 5
                komnata1_rect.y -= 5
        
    if kpressed[pg.K_LEFT]:
        if background_rect.left != player_rect.left:
            copy_rect = komnata1_rect.copy()
            copy_rect.x += 5
            can = pg.Rect.colliderect(player_rect, copy_rect)
            if can is False:
                background_rect.x += 5
                komnata1_rect.x += 5

    if kpressed[pg.K_RIGHT]:
        if background_rect.right != player_rect.right:
            copy_rect = komnata1_rect.copy()
            copy_rect.x -= 5
            can = pg.Rect.colliderect(player_rect, copy_rect)
            if can is False:
                background_rect.x -= 5
                komnata1_rect.x -= 5

    if komnata1_rect.bottom+4 == player_rect.top:
        # print('Написать букву, чтобы войти (L)')
        # font = pg.font.SysFont('Calibri', 45)
        #     text1 = font.render(game_over, True, WHITE, 5)
        #     text_rect = text1.get_rect()
        #     text_x = sc.get_width() / 2 - text_rect.width / 2
        #     text_y = sc.get_height() / 2 - text_rect.height / 2
        #     sc.blit(text1, [text_x, text_y])





    win.fill((10, 0, 30))
    win.blit(background, background_rect)
    win.blit(komnata1, komnata1_rect)
    win.blit(player, player_rect)
    win.blit(background2, background_rect)

    pg.display.update()
    clock.tick(FPS)