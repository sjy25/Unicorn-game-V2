
import pgzrun
import pygame
from random import randint
WIDTH=1200
HEIGHT=900
unicorn=Actor("unicorn")
unicorn.pos=400,300


#create the "obstacles"
bird=Actor("bird")
bird.pos=randint(800,1400),randint(10,190)
house=Actor("house")
house.pos=randint(600,1200),randint(20,250)
dino=Actor("dino")
dino.pos=300,600
miner=Actor("miner")
miner.pos=300,800

game_over=False
score=0

background = pygame.image.load("images/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

def draw():
    screen.blit(background,(0,0))
    if not game_over:
        unicorn.draw()
        bird.draw()
        house.draw()
        dino.draw()
        miner.draw()
        screen.draw.text("Score: "+str(score),(700,5),color="black")

    else:
        screen.fill("red")
        screen.draw.text("Game over!",topright=(850,300),fontsize=200)
       
def update():
    global game_over,score,number_of_updates

    if  keyboard.up:
        unicorn.y=unicorn.y-5
    elif keyboard.down:
        unicorn.y=unicorn.y+5
#to make it look like the bird is "flying" across the screen
    if bird.x>0:
        bird.x-=4
#when the bird flys off the screen, to place it back on screen
    else:
        bird.x=randint(800,1600)
        bird.y=randint(10,200)
#add 1 point for every bird the player manages to aviod
        score+=1
        number_of_updates=0
    if house.right>0:
        house.x-=2
    else:
        house.x=randint(800,1600)
        score+=1

    if dino.right>0:
        dino.x-=2
    else:
        dino.x=randint(800,1600)
        score+=1
        
    if miner.right>0:
        miner.x-=2
    else:
        miner.x=randint(800,1600)
        score+=1
#end game if unicorn hits any obstacle

    if unicorn.collidepoint(bird.x,bird.y) or \
       unicorn.collidepoint(dino.x,dino.y)or \
       unicorn.collidepoint(miner.x,miner.y)or \
       unicorn.collidepoint(house.x,house.y):
        game_over=True

pgzrun.go()
