import pygame as pg
import sys
import random as rnd

pg.font.init()

pg.init()

BLACK=(0,0,0)
RED=(255,0,0)
f1 = pg.font.Font(None, 36)
hp_agro = 250
text1 = f1.render(str(hp_agro), True,(180, 0, 0))
 
f2 = pg.font.SysFont('serif', 48)
text2 = f2.render("Kill", False,(0, 180, 0))
 
win = pg.display.set_mode((800, 600))
win_rect = win.get_rect()
background = pg.image.load("fonorm.png").convert()  # фон типа пол
background_rect = background.get_rect(topleft=(320, -270))  # такое положение обязательно, почему оно такое в душе не 
background2 = pg.image.load("2fon.png")  # фонарики ......:.>

player = pg.image.load('pixil-frame-0 (2).png')
player_rect = player.get_rect(center=(400, 300))

komnataob = pg.image.load('belikomnat.png')
komnataob_rect = komnataob.get_rect(topleft=(100,-230))

komnata1 = pg.image.load('komnata.png')
komnata1_rect = komnata1.get_rect(topleft=(480, -135))

xx = 0
yy = 0

k = 0

class Agrochel:
    def __init__(self, xx, yy, path):
        self.surface = pg.image.load(path)
        self.rect = self.surface.get_rect(topleft=(15,0))
        self.speedx = 0

    def update(self,surf):
        global xx
        global yy
        # la = komnataob_rect.colliderect(agroch.rect)
        self.speedy = rnd.randrange(-20,40)
        self.speedx = rnd.randrange(-20,40)
        if self.rect.left-player_rect.right>1:
           self.rect.x -= self.speedx
            
        if player_rect.left-self.rect.right>1:
            self.rect.x += self.speedx
            
        if self.rect.top-player_rect.bottom>1:
            self.rect.y -= self.speedy
        if player_rect.top-self.rect.bottom>1:
            self.rect.y += self.speedy

        xx = self.rect.x
        yy = self.rect.y
            

# all_sprites = pg.sprite.Group()
# agrs = pg.sprite.Group()
# for i in range(8):
#     m = Agrochel()
#     all_sprites.add(m)
#     agrs.add(m)

agroch = Agrochel(400, 300,'agrochel.png')
# agroch = pg.transform.scale(win,(agroch.rect.width*8,agroch.rect.height*6))

# mobs = pg.sprite.Group()
# for i in range(8):
#     m = Mob()
#     mobs.add(m)

# Mob(400, 300,'pixil-frame-0 (2).png')

die=0
v=0
l=0
p=0
n=0
# list = [l,p,v,n]
# rv = rnd.choice(list)
# print(rv)

rl = rnd.randint(1,3)
rv = rnd.randint(1,3)
rp = rnd.randint(1,3)
rn = rnd.randint(1,3)
print(rl,rv,rp,rn, 'random')

aaaaa=5
mnem=True
asasa=False
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

    if kpressed[108] and 450>komnata1_rect.centerx>340:
        mnem=True
    

    while mnem == True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            elif event.type == pg.MOUSEMOTION:
                position = pg.mouse.get_pos()
                x, y = position
                # print(x, 'XXXX')
                # print(y, 'YYYY')
                # print("Позиция мыши: ", event.pos)

            if event.type == pg.KEYDOWN:
                if event.key == 108:
                    asasa = True

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                # print(xx, yy, 'glaz')
                # print(x, y, 'mouse')
                # if (x >= xx + 100) and (y >= yy + 200):
                if x - 100 < xx < x + 100:
                    if y - 100 < yy < y < y + 100:
                        print('ура победа')
                        hp_agro -= 10
                        print(hp_agro)

            # if event.type==pg.KEYDOWN:
            #     if event.key==108:
            #         asasa=True

        text1 = f1.render(str(hp_agro), True, (180, 0, 0))
        agroch.update(komnataob)
        
        kpressed = pg.key.get_pressed()

        if kpressed[pg.K_UP]:
            if komnataob_rect.top-10!=player_rect.top:
                if komnataob_rect.top-10!=agroch.rect.top:
                    komnataob_rect.y += 5
                    agroch.rect.y+=5
                

        if kpressed[pg.K_DOWN]:
            if  komnataob_rect.bottom != player_rect.bottom:
                komnataob_rect.y -= 5
                agroch.rect.y-=5
            
        if kpressed[pg.K_LEFT]:
            if komnataob_rect.left-10 != player_rect.left:
                komnataob_rect.x += 5
                agroch.rect.x+=5

        if kpressed[pg.K_RIGHT]:
            if komnataob_rect.right != player_rect.right:
                komnataob_rect.x -= 5
                agroch.rect.x-=5

        surf_alpha1 = pg.Surface((800, 600))
        pg.draw.rect(surf_alpha1, BLACK, (0, 0, 800, 600))
        surf_alpha1.set_alpha(64)
        surf_alpha2 = pg.Surface((800, 600))
        pg.draw.rect(surf_alpha2, BLACK, (0, 0, 800, 600))
        surf_alpha2.set_alpha(128)
        surf_alpha3 = pg.Surface((800, 600))
        pg.draw.rect(surf_alpha3, BLACK, (0, 0, 800, 600))
        # surf_alpha.set_alpha(128)
        colors = [surf_alpha1,surf_alpha2,surf_alpha3,surf_alpha2,surf_alpha1]

    
                
        if asasa==True and 70>komnataob_rect.y>-55 and 361>komnataob_rect.x>325:
            l+=1
            print(l,v,p,n)
            for i in colors:
                print(i)
                win
                win.blit(i,win_rect)
                pg.display.update(win.get_rect())
                pg.time.delay(100)
            komnataob_rect.topleft=(-130,15)
            
            asasa=False
        elif asasa==True and 85>komnataob_rect.y>-50 and -100>komnataob_rect.x>-151:
            p+=1
            print(l,v,p,n)
            for i in colors:
                print(i)
                win
                win.blit(i,win_rect)
                pg.display.update(win.get_rect())
                pg.time.delay(100)
            komnataob_rect.topleft=(335,15)
            asasa=False
        elif asasa==True and 261>komnataob_rect.y>220 and 160>komnataob_rect.x>25:
            v+=1
            print(l,v,p,n)
            for i in colors:
                print(i)
                win
                win.blit(i,win_rect)
                pg.display.update(win.get_rect())
                pg.time.delay(100)

            komnataob_rect.topleft=(100,-230)
            asasa=False
        elif asasa==True and -220>komnataob_rect.y>-251 and 155>komnataob_rect.x>45:
            n+=1
            print(l,v,p,n)
            for i in colors:
                print(i)
                win
                win.blit(i,win_rect)
                pg.display.update(win.get_rect())
                pg.time.delay(100)
            komnataob_rect.topleft=(100,240)
            asasa=False
       
        
            
        win.fill((0, 0, 0))
        win.blit(komnataob,komnataob_rect)
        win.blit(player, player_rect)
        if hp_agro == 0 and k < 30:
            win.blit(text2, (10, 100))
            k += 1
            hp_agro = 250
            rl = rnd.randint(1,3)
            rv = rnd.randint(1,3)
            rp = rnd.randint(1,3)
            rn = rnd.randint(1,3)
            hp = 250
            v=0
            l=0
            p=0
            n=0
            print(rl,rv,rp,rn, 'random')
            # //////


        # if hp_agro == 0:
            # rl = rnd.randint(0,3)
            # rv = rnd.randint(0,3)
            # rp = rnd.randint(0,3)
            # rn = rnd.randint(0,3)
            # hp = 250
            # v=0
            # l=0
            # p=0
            # n=0
            # print(rl,rv,rp,rn, 'random')
        # if hp_agro == 250:
        #     rl = rnd.randint(0,3)
        #     rv = rnd.randint(0,3)
        #     rp = rnd.randint(0,3)
        #     rn = rnd.randint(0,3)
        #     hp = 250
        #     v=0
        #     l=0
        #     p=0
        #     n=0
        #     print(rl,rv,rp,rn, 'random')

            # if hp_agro == 0:

            # win.blit(text2, (10, 100))

        if (rl == l) and (hp_agro>0):
        # if l==1:
            win.blit(text1, (10, 50))
            # win.blit(text2, (10, 100))
            # print(agroch.rect.top,komnataob_rect.top)
            win.blit(agroch.surface,agroch.rect)
            # win.blit(agroch.surface,(agroch.rect.x-500,agroch.rect.y-200))
           

        pg.display.flip()
        pg.time.wait(3) 

    pg.display.flip()
    pg.time.wait(3)               

