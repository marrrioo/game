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

sc = pygame.display.set_mode((W, H))
sc_rect = sc.get_rect()
pygame.display.set_caption("Класс Rect")

hero = pygame.image.load('rat&eg.png')
hero_rect = hero.get_rect()

ground = pygame.image.load('fon.png')
ground = pygame.transform.scale(ground,(ground.get_rect().width*6,ground.get_rect().height//2))            # изменять размеры картинки в surface
ground_rect = ground.get_rect()

ground_rect.bottom = sc_rect.bottom

hero_rect.bottom = ground_rect.top

ris1 = pygame.image.load('ris1.png')
ris1_rect = ris1.get_rect()

speed = 5

first = True

while True:
    for event in pygame.event.get():                           #pygame.event.get() - события, которые уже произошли
        # print(event)
        if event.type == pygame.QUIT:
            exit()

        
    keys = pygame.key.get_pressed()                         #pygame.key.get_pressed() - кнопки, которые нажаты в данный момент
    pygame.display.update()
    if keys[pygame.K_LEFT]:
            hero_rect.x -= speed
    if keys[pygame.K_RIGHT]:
            hero_rect.x += speed
    if keys[pygame.K_UP]:
            hero_rect.y -= speed
    if keys[pygame.K_DOWN]:
            hero_rect.y += speed                      


    sc.fill(WHITE)
    clock.tick(FPS)