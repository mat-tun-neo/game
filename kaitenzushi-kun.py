from pygame_functions import *
from random import random

SCREEN_X = 1200
SCREEN_Y = 600
PLAYER_ALLIMAGE = 27
PLAYER_MOVELEN = 16
PLAYER_WIDTH = 192
PLAYER_HEIGHT = 160
PLAYER_SCALE = 1.5
GROUND = 380 - PLAYER_HEIGHT * PLAYER_SCALE - 20
TOUCH_JUDGE = 30
RAIL_Y = 312
DISH_MOVELEN = 5
DISH_WIDTH = 250
DISH_HEIGHT = 113
DISH_SCALE = 1.2
DISH_NUM = 5
DISH_APPEAR = 0.01
DISH_VALUE = 100
DISH_X = DISH_WIDTH * (-1)
DISH_Y = RAIL_Y - DISH_HEIGHT / 3 + 10
KAIKEI_KETA = 6
KAIKEI_X = 500
KAIKEI_Y = 0
KAIKEI_WIDTH = 39

screen = screenSize(SCREEN_X, SCREEN_Y)
setBackgroundImage("images/bg_kaitenzushi.jpg")

all_rails = []
for i in range(2):
    rail = makeSprite("images/rail.jpg")
    if i==0:
        rail.x = SCREEN_X * (-1)
    else:
        rail.x = 0
    moveSprite(rail, rail.x, RAIL_Y)
    showSprite(rail)
    all_rails.append(rail)

all_dishes = []
for i in range(DISH_NUM):
    dish = makeSprite("images/dish" + format(i, '02') + ".png")
    dish.x = DISH_WIDTH * (-1)
    dish.y = DISH_Y
    moveSprite(dish, dish.x, dish.y)
    showSprite(dish)
    all_dishes.append(dish)

player = makeSprite("images/aji000.png")
for i in range(PLAYER_ALLIMAGE - 1):
    addSpriteImage(player, "images/aji" + format(i + 1, '03') + ".png")
    
player_x = SCREEN_X / 2
transformSprite(player, 0, PLAYER_SCALE)
moveSprite(player, player_x, GROUND)
showSprite(player)
left = False
right = False

def kaikei(n):
    j = 0
    for i in range(KAIKEI_KETA):
        if KAIKEI_KETA - len(str(n)) > i:
            kaikei = makeImage("images/a.jpg")
        else:
            kaikei = makeImage("images/" + str(n)[j] + ".jpg")
            j += 1
        screen.blit(kaikei, (KAIKEI_X + KAIKEI_WIDTH * i, KAIKEI_Y))

nextFrame = clock()
playerImgNo = 0
score = 0
kaikei(score)
dish_appearflg = 0

while True:
    if not left and not right:
        if keyPressed("left"):
            playerImgNo = 0
            left = True
        if keyPressed("right"):
            playerImgNo = PLAYER_ALLIMAGE
            right = True
        
    if left:
        if clock() > nextFrame:
            playerImgNo += 1
            if playerImgNo > 26:
                playerImgNo = 0
                left = False
                
            changeSpriteImage(player, playerImgNo)
            nextFrame = clock() + 60
            
            if playerImgNo > 6 and playerImgNo < 22:
                player_x -= PLAYER_MOVELEN * PLAYER_SCALE
                if player_x < 0:
                    player_x = 0
            else:
                player_x += DISH_MOVELEN
            moveSprite(player, player_x, GROUND)
            
    if right:
        if clock() > nextFrame:
            playerImgNo -= 1
            if playerImgNo < 0:
                playerImgNo = 0
                right = False
                
            changeSpriteImage(player, playerImgNo)
            nextFrame = clock() + 60
            
            if playerImgNo > 6 and playerImgNo < 22:
                player_x += PLAYER_MOVELEN * PLAYER_SCALE
            else:
                player_x += DISH_MOVELEN
            if player_x > SCREEN_X - PLAYER_WIDTH * PLAYER_SCALE:
                player_x = SCREEN_X - PLAYER_WIDTH * PLAYER_SCALE
            moveSprite(player, player_x, GROUND)
    
    if not left and not right:
        player_x += DISH_MOVELEN
        moveSprite(player, player_x, GROUND)
        if player_x > SCREEN_X - PLAYER_WIDTH * PLAYER_SCALE:
            player_x = SCREEN_X - PLAYER_WIDTH * PLAYER_SCALE
    
    for rail in all_rails:
        rail.x += DISH_MOVELEN
        if rail.x >= SCREEN_X:
            rail.x = SCREEN_X * (-1)
        moveSprite(rail, rail.x, RAIL_Y)
    
    cnt = 1
    for dish in all_dishes:
        if dish_appearflg == 0 and dish.x == DISH_X and random() < DISH_APPEAR:
            dish.x += DISH_MOVELEN
            dish_appearflg = cnt
        
        if (left and playerImgNo == 24) and touching(player, dish):
            dish.y += DISH_MOVELEN * 2
        if SCREEN_Y > dish.y > DISH_Y:
            dish.y += DISH_MOVELEN * 2
        if dish.y > SCREEN_Y:
            dish.y = SCREEN_Y
            score += DISH_VALUE
            kaikei(score)
        if dish.x > SCREEN_X:
            dish.x = DISH_X
            dish.y = DISH_Y
        elif dish.x > DISH_X:     
            moveSprite(dish, dish.x, dish.y)
            dish.x += DISH_MOVELEN
            if cnt == dish_appearflg and dish.x > 0:
                dish_appearflg = 0
        cnt += 1
            
    tick(30)




