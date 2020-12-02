from random import randint
import pygame
import random
from pygame import time

from pygame.constants import WINDOWEVENT
from pygame.event import clear
#print("Jeanette is a gorgous babe")
White =(255,255,255)
Brown =(50,0,0)
Black = (0,0,0)

class Lady(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image=pygame.image.load("Lady2.png").convert()
        self.image.set_colorkey(White)
        self.rect = self.image.get_rect()
class Thomas(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image=pygame.image.load("Lady2.png").convert()
        self.image.set_colorkey(White)
        self.rect = self.image.get_rect()
class Diesel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image=pygame.image.load("diesel.png").convert()
        self.image.set_colorkey(White)
        self.rect = self.image.get_rect()

class Coal(pygame.sprite.Sprite):
    def __init__(self, color,width,height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(Brown)
        self.image.set_colorkey(White)
        pygame.draw.ellipse(self.image, color, [0,0, width, height])
        self.rect = self.image.get_rect()


def LadyMovement():
    global xPlayer
    global yPlayer
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if xPlayer < 0 or xPlayer > screen_width:
            if xPlayer < 0:
                xPlayer = screen_width
            if xPlayer > screen_width:
                xPlayer = 0
        else:
            xPlayer = xPlayer - 2
    if keys[pygame.K_RIGHT]:
        if xPlayer < 0 or xPlayer > screen_width:
            if xPlayer < 0:
                xPlayer = screen_width
            if xPlayer > screen_width:
                xPlayer = 0
        else:
            xPlayer = xPlayer + 2
    if keys[pygame.K_UP]:
        if yPlayer < 0 or yPlayer > screen_height:
            if yPlayer < 0:
                yPlayer = screen_height
            if yPlayer > screen_height:
                yPlayer = 0
        else:
            yPlayer = yPlayer-2
    if keys[pygame.K_DOWN]:
        if yPlayer < 0 or yPlayer > screen_height:
            if yPlayer < 0:
                yPlayer = screen_height
            if yPlayer > screen_height:
                yPlayer = 0
        else:
            yPlayer =yPlayer +2


def ChaseMovement():
    global xPlayer
    global yPlayer
    global xDiesel
    global yDiesel
    global coalCollected
    speed = randint(0,2)
    yDiesel = 100
    yPlayer = 100
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        xPlayer = xPlayer- 6
        coalCollected =- 1
    if keys[pygame.K_t]:
        xDiesel = xDiesel+6
        coalCollected =-3
    if xPlayer < 0 or xPlayer > screen_width:
            if xPlayer < 0:
                xPlayer = screen_width
            if xPlayer > screen_width:
                xPlayer = 0
    else:
        xPlayer = xPlayer - 1
    if xDiesel < 0 or xDiesel > screen_width:
            if xDiesel < 0:
                xDiesel = screen_width
            if xDiesel > screen_width:
                xDiesel = 0
    else:
        xDiesel = xDiesel - speed
            

pygame.init()
screen_width = 626
screen_height = 469
screen = pygame.display.set_mode([screen_width, screen_height])
all_sprites = pygame.sprite.Group()
chase_sprites = pygame.sprite.Group()
coal_sprites = pygame.sprite.Group()
PlayerLady = Lady()
ComputerDiesel= Diesel()
ComputerThomas = Thomas()
bg =pygame.image.load("backgroundTunnel.jpg")
all_sprites.add(PlayerLady)

for i in range(50):
    coalpiece = Coal(Brown, 5, 5)
    coalpiece.rect.x = random.randrange(screen_width)
    coalpiece.rect.y = random.randrange(screen_height)

    coal_sprites.add(coalpiece)
    all_sprites.add(coalpiece)

#This loop is the driver for the first part of the game.
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
coalCollected = 0
done =False
xPlayer = 500
yPlayer = 70
xDiesel = 800
yDiesel = 70
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done =True
    Time = (pygame.time.get_ticks()/1000)
    bg =pygame.image.load("backgroundTunnel.jpg")
    screen.blit(bg,(0,0))
    LadyMovement()
    PlayerLady.rect.x = xPlayer
    PlayerLady.rect.y = yPlayer
    coal_collect_list = pygame.sprite.spritecollide(PlayerLady, coal_sprites, True)
    for collect in coal_collect_list:
        coalCollected +=1
    scoreDisplay = myfont.render(str(coalCollected), True, (255,255,255))
    screen.blit(scoreDisplay, (50,400))
    Timer = myfont.render(str(Time), True, (255,255,255))
    screen.blit(Timer, (520,50))
    all_sprites.draw(screen)
    if Time >15:
        done = True
    pygame.display.flip()

#Second part of the game. This while loop handles the chase scene.
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done =True
    myfont2 = pygame.font.SysFont('Times New Roman', 10)
    screen_width = 1000
    screen_height = 250
    screen = pygame.display.set_mode([screen_width, screen_height])
    bg =pygame.image.load("entirebackground.png")
    screen.blit(bg,(0,0))
    image = pygame.Surface([20,20]).convert_alpha()
    image.fill((255,255,255))
    image.scroll(1,0)
    chase_sprites.add(PlayerLady)
    chase_sprites.draw(screen)
    PlayerLady.rect.x = 800
    PlayerLady.rect.y = 400
    #chase_sprites.add(ComputerThomas)
    chase_sprites.add(ComputerDiesel)
    ChaseMovement()
    PlayerLady.rect.x = xPlayer
    PlayerLady.rect.y = yPlayer
    ComputerDiesel.rect.x = xDiesel
    ComputerDiesel.rect.y = yDiesel 
    crashedHer = pygame.sprite.collide_rect(PlayerLady, ComputerDiesel)
    if crashedHer or coalCollected == 0:
        Text = myfont.render("Game Over", True, (255,255,255))
        screen.blit(Text, (300,300))
    pygame.display.flip()