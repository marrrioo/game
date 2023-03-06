import pygame as pg
import sys
import random as rnd

pg.init()
WIDTH = 480
HEIGHT = 600
FPS = 60
win = pg.display.set_mode((WIDTH, HEIGHT))
win_rect = win.get_rect()
background = pg.image.load("fonorm.png").convert()  # фон типа пол
background_rect = background.get_rect(topleft=(320, -270))  # такое положение обязательно, почему оно такое в душе не
background2 = pg.image.load("2fon.png")  # фонарики ......:.>

player = pg.image.load('pixil-frame-0 (2).png')

komnata1 = pg.image.load('komnata.png')
komnata1_rect = komnata1.get_rect(topleft=(480, -135))

FPS = 60 # число кадров в секунду
clock = pg.time.Clock()

player_rect = player.get_rect(center=(400, 300))
p=0


class Player(pg.sprite.Sprite):
    def init(self):

        pg.sprite.Sprite.init(self)
        self.image = player
        self.rect = self.image.get_rect()
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -8
        if keystate[pg.K_RIGHT]:
            self.speedx = 8
        if keystate[pg.K_UP]:
            self.speedy = -8
        if keystate[pg.K_DOWN]:
            self.speedy = 8

        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        self.rect.y += self.speedy
        if self.rect.right > HEIGHT:
            self.rect.right = HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0


class Komnata(pg.sprite.Sprite):
    def init(self):
        pg.sprite.Sprite.init(self)
        self.image = komnata1
        self.rect = self.image.get_rect()
        self.rect.x = 480
        self.rect.y = -135
        self.speedy = 0
        self.speedx = 0

    # def update(self):
    #     self.rect.x += self.speedx
    #     self.rect.y += self.speedy
    #     if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
    #         self.rect.x = random.randrange(WIDTH - self.rect.width)
    #         self.rect.y = random.randrange(-100, -40)
    #         self.speedy = random.randrange(1, 8)
all_sprites = pg.sprite.Group()
player = Player()
komnata = Komnata()
all_sprites.add(player)
all_sprites.add(komnata)

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    # collide = pg.Rect.colliderect(player_rect, komnata1_rect)
    # kpressed = pg.key.get_pressed()
    # if kpressed[pg.K_UP]:
    #     p=1
    # elif kpressed[pg.K_DOWN]:
    #     p=2
    # elif kpressed[pg.K_LEFT]:
    #     p=3
    # elif kpressed[pg.K_RIGHT]:
    #     p=4
    # elif kpressed[108]:
    #     p=5
    # print(p)
    # if p==1:
    #     win.fill((0, 0, 0))
    #     win.blit(background, background_rect)
    #     win.blit(komnata1, komnata1_rect)
    #     win.blit(player, player_rect)
    #     win.blit(background2, background_rect)
    #     if background_rect.top!=player_rect.top:
    #         copy_rect = komnata1_rect.copy()
    #         copy_rect.y += 5
    #         can = pg.Rect.colliderect(player_rect, copy_rect)
    #         if can is False:
    #             background_rect.y += 5
    #             komnata1_rect.y += 5
    #         p=0
    # elif p==2:
    #     win.fill((0, 0, 0))
    #     win.blit(background, background_rect)
    #     win.blit(komnata1, komnata1_rect)
    #     win.blit(player, player_rect)
    #     win.blit(background2, background_rect)
    #     if  background_rect.bottom != player_rect.bottom:
    #         copy_rect = komnata1_rect.copy()
    #         copy_rect.y -= 5
    #         can = pg.Rect.colliderect(player_rect, copy_rect)
    #         if can is False:
    #             background_rect.y -= 5
    #             komnata1_rect.y -= 5
    #         p=0
    # elif p==3:
    #     win.fill((0, 0, 0))
    #     win.blit(background, background_rect)
    #     win.blit(komnata1, komnata1_rect)
    #     win.blit(player, player_rect)
    #     win.blit(background2, background_rect)
    #     if background_rect.left != player_rect.left:
    #         copy_rect = komnata1_rect.copy()
    #         copy_rect.x += 5
    #         can = pg.Rect.colliderect(player_rect, copy_rect)
    #         if can is False:
    #             background_rect.x += 5
    #             komnata1_rect.x += 5
    #         p=0
    # elif p==4:
    #     win.fill((0, 0, 0))
    #     win.blit(background, background_rect)
    #     win.blit(komnata1, komnata1_rect)
    #     win.blit(player, player_rect)
    #     win.blit(background2, background_rect)
    #     if background_rect.right != player_rect.right:
    #         copy_rect = komnata1_rect.copy()
    #         copy_rect.x -= 5
    #         can = pg.Rect.colliderect(player_rect, copy_rect)
    #         if can is False:
    #             background_rect.x -= 5
    #             komnata1_rect.x -= 5
    #         p=0
    # elif p==5:
    #     win.blit(background, background_rect)
    #     win.blit(player, player_rect)
    # # win.fill((10, 0, 30))
    # # win.blit(background, background_rect)
    # # win.blit(komnata1, komnata1_rect)
    # # win.blit(player, player_rect)
    # # win.blit(background2, background_rect)





    all_sprites.update()

    # Рендеринг
    win.fill((0,0,0))
    all_sprites.draw(win)
    # После отрисовки всего, переворачиваем экран
    pg.display.flip()

    pg.display.update()
    clock.tick(FPS)