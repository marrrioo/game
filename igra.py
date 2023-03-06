import pygame as pg
import sys
import random as rnd

pg.init()

win = pg.display.set_mode((800, 600))
win_rect = win.get_rect()
background = pg.image.load("fonorm.png").convert()  # фон типа пол
background_rect = background.get_rect(topleft=(320, -270))  # такое положение обязательно, почему оно такое в душе не 
background2 = pg.image.load("2fon.png")  # фонарики ......:.>

player = pg.image.load('pixil-frame-0 (2).png')
copyplayer = pg.image.load('pixil-frame-0 (2).png')
komnata1 = pg.image.load('komnata.png')
komnata1_rect = komnata1.get_rect(topleft=(480, -135))

FPS = 60 # число кадров в секунду
clock = pg.time.Clock()

player_rect = player.get_rect(center=(400, 300))
copyplayer_rect = player_rect.copy()
copy

komnataob = pg.image.load('pixil-frame-0.png')
komnataob = pg.transform.scale(komnataob,(komnataob.get_rect().width*8,komnataob.get_rect().height*6))
komnataob_rect = komnata1.get_rect()
a = False
while a == False:
    win.fill((10, 0, 30))
    win.blit(background, background_rect)
    win.blit(komnata1, komnata1_rect)
    win.blit(player, player_rect)
    win.blit(background2, background_rect)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    collide = pg.Rect.colliderect(player_rect, komnata1_rect)
    kpressed = pg.key.get_pressed()
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
    if kpressed[108]:
            if komnata1_rect.bottom+4 == player_rect.top:
                print('upuuu')
                a = True
                player_rect = player.get_rect(bottom=(400, 600))
                x = 1
    pg.display.update()
    clock.tick(FPS)

if x == 1:
    print('x')



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    kpressed = pg.key.get_pressed()

    win.fill((10, 0, 30))
    win.blit(komnataob, komnataob_rect)
    win.blit(player, player_rect)
    win.blit
    if kpressed[pg.K_UP] and komnataob_rect.top!=player_rect.top:
            player_rect.y -= 5

    if kpressed[pg.K_DOWN]:
        if  komnataob_rect.bottom != player_rect.bottom:
                player_rect.y += 5

    if kpressed[pg.K_LEFT]:
        if komnataob_rect.left != player_rect.left:
                player_rect.x -= 5

    if kpressed[pg.K_RIGHT]:
        if komnataob_rect.right != player_rect.right:
                player_rect.x += 5
    pg.display.update()
    clock.tick(FPS)




