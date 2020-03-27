from pygame_functions import *

SCREEN_X = 1200
SCREEN_Y = 600
PLAYER_ALLIMAGE = 27
PLAYER_MOVELEN = 12
PLAYER_WIDTH = 192
PLAYER_HEIGHT = 160
PLAYER_SCALE = 1.5
DISH_ALLIMAGE = 3
DISH_MOVELEN = 5
DISH_WIDTH = 250
DISH_HEIGHT = 113
DISH_SCALE = 1.2
DISH_NUM = 5
DISH_INTERVAL = 2
GROUND = 380 - PLAYER_HEIGHT * PLAYER_SCALE - 20
TOUCH_JUDGE = 30
RAIL_Y = 312
DISH_Y = RAIL_Y - DISH_HEIGHT / 3 + 10

screenSize(SCREEN_X, SCREEN_Y)
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
    dish.x = i * SCREEN_X / DISH_INTERVAL * (-1) - DISH_WIDTH
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
score = 0
scorelabel = makeLabel(str(score), 50, SCREEN_X / 3, 450, "black")
showLabel(scorelabel)

nextFrame = clock()
playerImgNo = 0

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
    
    for dish in all_dishes:
        dish.x += DISH_MOVELEN
        if left and playerImgNo == 24 and touching(player, dish):
            dish.y += 10
            score += 1
            changeLabel(scorelabel, str(score))
        if dish.y > DISH_Y:
            dish.y += 10
        moveSprite(dish, dish.x, dish.y)
        if dish.x > SCREEN_X:
            dish.x = DISH_WIDTH * (-1)
            if dish.y > SCREEN_Y:
                dish.y = DISH_Y

    tick(30)




