import pygame                                               # импорт библиотеки

pygame.init()

W = 900
H = 900

sc = pygame.display.set_mode((W, H))                        # регулировать размер дисплея (900 на 900/600 на 400)
pygame.display.set_caption("События от клавиатуры")         # название экрана


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60                                                    # число кадров в секунду
clock = pygame.time.Clock()

surf = pygame.Surface((25,25))


x = W // 2
y = H // 2
x2 = W // 6
y2 = H // 6

speed = 1
# shirina = 100

first = True

while True:
    for event in pygame.event.get():                           #pygame.event.get() - события, которые уже произошли
        # print(event)
        if event.type == pygame.QUIT:
            exit()
        # elif event == 1:
        #     first = True
        #     second = False
        # # else:
        # #     first = False
        # #     first = True
        # elif event == 2:
        #     # second = True
        #     first = False

        
    sc.fill(WHITE)
    kv1 = pygame.draw.rect(sc, BLUE, (x, y, 50, 70))   
    kv2 = pygame.draw.rect(sc, GREEN, (x2, y2, 80, 90))


    keys = pygame.key.get_pressed()                         #pygame.key.get_pressed() - кнопки, которые нажаты в данный момент
    if keys[49]:
        first = True
    elif keys[50]:
        first = False

    second  = True
    third = True
    forth = True
    fifth = True

    if first == True:
        pygame.display.update()
        if keys[pygame.K_LEFT]:
            second = ((x != x2+50+10) and (y2 != y+10))
            if second:
                x -= speed

        if keys[pygame.K_RIGHT]:
            third = ((x+50+10 != x2) and (y+70+10 != y2))
            if third:
                x += speed
        if keys[pygame.K_UP]:
            forth = ((x2 != x+10) and (y2 != y+70 +10))
            if forth:
                y -= speed
        if keys[pygame.K_DOWN]:
            fifth = ((x2 != x+10) and(y2 != y+90+10))
            if fifth:
                y += speed

    if first == False:
        pygame.display.update()                         
        if keys[pygame.K_LEFT]:                                 
            x2 -= speed
        if keys[pygame.K_RIGHT]:
            x2 += speed
        if keys[pygame.K_UP]:
            y2 -= speed
        if keys[pygame.K_DOWN]:
            y2 += speed
        # shirina -=5

    # if keys[49]:
    #     sc.fill(WHITE)
    #     pygame.draw.rect(sc, BLUE, (x, y, 10, 20))      
    #     pygame.display.update()



    clock.tick(FPS)


            # first1 = (x-10) 
            # first2 = (x2+80)
            # second = (y+70)
            # # third = 
            # print(x - 10)
            # print(x2 + 80)
            # print(y + 70)
            # print(y2)
            # if ((x != first2) and (second != y2)) or ((x == first2) and (second != y2)) or ((x!=first2) and (second == y2)):
            # if ((x != first2) and ((y+70) != y2)):
            # #     print('можно')


                        # if (x != (x2+80)):              #and (y2+90) == y)
            #     print('можно')                             
            #     x -= speed
            # elif (y+70) != y2:
            #     print('можно1')                             
            #     x -= speed
            # elif (y2+80) != y:
            #     print('можно2')
            #     x-=speed
            # else:
            #     print('низя')
            #     x = x