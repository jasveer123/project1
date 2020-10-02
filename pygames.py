import pygame
import random
import math
from pygame import mixer
pygame.init()
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textx=10
texty=10
over_font=pygame.font.Font('freesansbold.ttf',64)
def show_score(x,y):
  score=font.render("score :"+ str(score_value),True,(255,255,255))
  screen.blit(score,(x,y))
def game_over_text():
  over_text=over_font.render("GAME OVER:",True,(255,255,255))
  screen.blit(over_text,(200,250))
screen=pygame.display.set_mode((800,600))
background=pygame.image.load('background.png')
pygame.display.set_caption("alein soot out")
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
playerimg=pygame.image.load('player.png')
playerx=380
playery=480
playerx_change=0

enemyimg=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
enemy_number=6
for i in range(enemy_number):
   enemyimg.append(pygame.image.load('enemy.png'))
   enemyx.append(random.randint(0,800))
   enemyy.append(random.randint(50,150))
   enemyx_change.append(2)
   enemyy_change.append(40)


mixer.music.load('background.wav')
mixer.music.play(-1)

bullet=pygame.image.load('bullet.png')
bulletx=0
bullety=480
bulletx_change=0
bullety_change=7
bullet_state="ready"
def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet,(x+16,y+10))
    
def collision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((math.pow(enemyx-bulletx,2))+(math.pow(enemyy-bullety,2)))    
    if distance<27:
        return True
    else:
       return False    
    

running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
  
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerx_change=-4
            if event.key==pygame.K_RIGHT:
                playerx_change=4
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerx_change=0               
            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound('shooot.wav')
                    bullet_sound.play()
                    bulletx=playerx
                    fire_bullet(playerx,bullety)
    playerx+=playerx_change
    
    if playerx<=0:
           playerx=0
    elif playerx>=736:
            playerx=736
    
    for i in  range(enemy_number):
        if enemyy[i]>400:
            for j in range(enemy_number):
                enemyy[j]=2000
            game_over_text()
            break     

        enemyx[i]+=enemyx_change[i]
        if enemyx[i]<=0:
            enemyx_change[i]=5
            enemyy[i]+=enemyy_change[i]
        elif enemyx[i]>=770:
            enemyx_change[i]=-5
            enemyy[i]+=enemyy_change[i] 

        iscollision=collision(enemyx[i],enemyy[i],bulletx,bullety)
        if iscollision:
           collide_sound=mixer.Sound('collide.wav')
           collide_sound.play()
           bullety=480
           bullet_state="ready"
           score_value+=1
          
           enemyx[i]=random.randint(0,800)
           enemyy[i]=random.randint(50,150)  
        enemy(enemyx[i],enemyy[i],i)   
    if bullety<=0:
        bullety=480
        bullet_state="ready"
    if bullet_state is "fire":
        fire_bullet(bulletx,bullety)    
        bullety-=bullety_change
    

    player(playerx,playery)
    show_score(textx,texty)

    pygame.display.update()