import pygame
import random
import math
from pygame import mixer
pygame.init()
clock=pygame.time.Clock()

gamewindow=pygame.display.set_mode((800,800))
pygame.display.set_caption("Space War")
icon=pygame.image.load('D:/Coding/python/ufo.png')
pygame.display.set_icon(icon)
playerimage=pygame.image.load('D:/Coding/python/App-launch-spaceship-icon.png')
playerx=335
playery=650
imagellow=pygame.image.load('D:/Coding/python/spa.jpg')
bulletimage=pygame.image.load('D:/Coding/python/weapon54321.png')
bulletx=0
bullety=650
bulletxvelocity=0
bulletyvelocity=4
bulletstate="ready"
mixer.music.load('D:/Coding/python/Alan Walker - Darkside (Instrumental on Screen).mp3')
mixer.music.play(-1)
running=True
fps=200
velocity_x=0
velocity_y=0

enemyimage=[]
enemyx=[]
enemyy=[] 
enemyvelocityx=[]                                                                       
enemyvelocityy=[]
red=(255,0,0)


numenemy=6


score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 84)
textX = 10
testY = 10



for i in range(numenemy):
    enemyimage.append(pygame.image.load('D:/Coding/python/space-ship-3-icon (1).png'))
    enemyx.append(random.randint(0,635))
    enemyy.append(random.randint(50,150))
    enemyvelocityx.append(2)
    enemyvelocityy.append(40)
    
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    gamewindow.blit(over_text, (200, 250))

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    gamewindow.blit(score, (x, y))
 
def player(x,y):
    gamewindow.blit(playerimage,(x,y))
def enemy(x,y,i):
    gamewindow.blit(enemyimage[i],(x,y))
def bullet(x,y):
    global bulletstate
    bulletstate="fire"
    gamewindow.blit(bulletimage,(x+45,y+10))

def collide(bulletx,bullety,enemyx,enemyy):
    dis=math.sqrt(math.pow(enemyx-bulletx,2)+(math.pow(enemyy-bullety,2)))
    if dis <=27:
        return True
    else:
        return False



running=True
while running:
    
    
    
    gamewindow.blit(imagellow,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False


        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x=5
            if event.key==pygame.K_LEFT:
                velocity_x=-5
            if event.key==pygame.K_SPACE:
                if bulletstate == "ready":
                    bulletx=playerx
                    bullet(bulletx,bullety)

        if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                    velocity_x=0
    
    playerx+=velocity_x
    if playerx<=0:
        playerx=0
    elif playerx>690:
        playerx=690
    
    
    for i in range(numenemy):
        if enemyy[i] > 620:
            for j in range(numenemy):
                enemyy[j] = 2000
            game_over_text()
            break
        enemyx[i]+=enemyvelocityx[i]
        if enemyx[i]<=0:
            enemyvelocityx[i]=3
            enemyy[i]+=enemyvelocityy[i]
        elif enemyx[i]>730:
            enemyvelocityx[i]=-3
            enemyy[i]+=enemyvelocityy[i]



        colision=collide(enemyx[i], enemyy[i],bulletx, bullety)
        if colision:
            bullety=650
            bulletstate="ready"
            score_value += 1
            
            enemyx[i]=random.randint(0,800)
            enemyy[i]=random.randint(50,150)
        enemy(enemyx[i],enemyy[i],i)


    if bullety<=0:
        bullety=650
        bulletstate ="ready"
    if bulletstate == "fire":
        bullet(bulletx,bullety)
        bullety-=bulletyvelocity


    
    
    
    player(playerx,playery)
    
    
    show_score(textX, testY)
    clock.tick(fps)
    pygame.display.update()