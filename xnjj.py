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
player_rect = player.get_rect(center=(400, 300))

komnataob = pg.image.load('belikomnat.png')
komnataob_rect = komnataob.get_rect()
komnataob = pg.transform.scale(komnataob,(komnataob.get_rect().width*8,komnataob.get_rect().height*6))

komnata1 = pg.image.load('komnata.png')
komnata1_rect = komnata1.get_rect(topleft=(480, -135))

FPS = 60 # число кадров в секунду
clock = pg.time.Clock()


p=0
mnem= False
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    collide = pg.Rect.colliderect(player_rect, komnata1_rect)
    kpressed = pg.key.get_pressed()
    if mnem == False:
        win.fill((0, 0, 0))
        win.blit(background, background_rect)
        win.blit(komnata1, komnata1_rect)
        win.blit(player, player_rect)
        win.blit(background2, background_rect)

        if kpressed[pg.K_UP]:
            print(collide)
            if background_rect.top!=player_rect.top:
                copy_rect = komnata1_rect.copy()
                copy_rect.y += 5
                can = pg.Rect.colliderect(player_rect, copy_rect)
                if can is False:
                    background_rect.y += 5
                    komnata1_rect.y += 5
                
        if kpressed[pg.K_DOWN]:
            print(collide)
            if  background_rect.bottom != player_rect.bottom:
                copy_rect = komnata1_rect.copy()
                copy_rect.y -= 5
                can = pg.Rect.colliderect(player_rect, copy_rect)
                if can is False:
                    background_rect.y -= 5
                    komnata1_rect.y -= 5
            
        if kpressed[pg.K_LEFT]:
            print(collide)
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
    print(komnata1_rect.centerx)
    if kpressed[108] and 450>komnata1_rect.centerx>340:
        mnem=True
    
    elif mnem == True:
            win.fill((0, 0, 0))
            win.blit(komnataob, komnataob_rect)
            win.blit(player, player_rect)
            if kpressed[pg.K_UP]:
                if komnataob_rect.top!=player_rect.top:
                    # copy_rect = komnata1_rect.copy()
                    # copy_rect.y += 5
                    # can = pg.Rect.colliderect(player_rect, copy_rect)
                    # if can is False:
                        komnataob_rect.y += 5

                
            if kpressed[pg.K_DOWN]:
            #     print(collide)
                if  komnataob_rect.bottom != player_rect.bottom:
            #         copy_rect = komnata1_rect.copy()
            #         copy_rect.y -= 5
            #         can = pg.Rect.colliderect(player_rect, copy_rect)
            #         if can is False:
            #             background_rect.y -= 5
                        komnataob_rect.y -= 5
                
            if kpressed[pg.K_LEFT]:
            #     print(collide)
                if komnataob_rect.left != player_rect.left:
            #         copy_rect = komnata1_rect.copy()
            #         copy_rect.x += 5
            #         can = pg.Rect.colliderect(player_rect, copy_rect)
            #         if can is False:
            #             background_rect.x += 5
                        komnataob_rect.x += 5

            if kpressed[pg.K_RIGHT]:
                if komnataob_rect.right != player_rect.right:
            #         copy_rect = komnata1_rect.copy()
            #         copy_rect.x -= 5
            #         can = pg.Rect.colliderect(player_rect, copy_rect)
            #         if can is False:
            #             background_rect.x -= 5
                        komnataob_rect.x -= 5
            # while True:
            



    # win.fill((10, 0, 30))
    # win.blit(background, background_rect)
    # win.blit(komnata1, komnata1_rect)
    # win.blit(player, player_rect)
    # win.blit(background2, background_rect)

    pg.display.update()
    clock.tick(FPS)
