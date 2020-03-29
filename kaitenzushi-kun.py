from pygame_functions import *
from random import random

SCREEN_X = 1200             # 画面 横サイズ （ピクセル）
SCREEN_Y = 600              # 画面 縦サイズ （ピクセル）
PLAYER_ALLIMAGE = 27        # プレイヤー アニメーション全コマ数
PLAYER_MOVELEN = 16         # プレイヤー 動く幅 （ピクセル）
PLAYER_SPEED = 35           # プレイヤー 動く速さ （ms）
PLAYER_WIDTH = 192          # プレイヤー 横サイズ （ピクセル）
PLAYER_HEIGHT = 160         # プレイヤー 縦サイズ （ピクセル）
PLAYER_SCALE = 1.5          # プレイヤー 画像の拡大率
PLAYER_Y = 380 - PLAYER_HEIGHT * PLAYER_SCALE - 20    # プレイヤー 初期Y位置 （ピクセル）
RAIL_Y = 312                # レール 初期Y位置 （ピクセル）
DISH_MOVELEN = 5            # お皿 動く幅 （ピクセル）
DISH_WIDTH = 250            # お皿 横サイズ （ピクセル）
DISH_HEIGHT = 113           # お皿 縦サイズ （ピクセル）
DISH_SCALE = 1.2            # お皿 画像の拡大率
DISH_NUM = 5                # お皿 スプライトの枚数
DISH_APPEAR = 0.1           # お皿 出現率
DISH_VALUE = 100            # お皿 1枚の得点
DISH_X = DISH_WIDTH * (-1)  # お皿 初期X位置 （ピクセル）
DISH_Y = RAIL_Y - DISH_HEIGHT / 3 + 10  # お皿 初期Y位置 （ピクセル）
KAIKEI_KETA = 6             # 会計スコア 桁数（＝画像の枚数）
KAIKEI_X = 500              # 会計スコア 初期X位置 （ピクセル）
KAIKEI_Y = 0                # 会計スコア 初期Y位置 （ピクセル）
KAIKEI_WIDTH = 39           # 会計スコア 横サイズ （ピクセル）
METER_ALLIMAGE = 6          # お客メーター アニメーション全コマ数
METER_SCALE = 1             # お客メーター 画像の拡大率
METER_X = 550               # お客メーター 初期X位置 （ピクセル）
METER_Y = 430               # お客メーター 初期Y位置 （ピクセル）

screen = screenSize(SCREEN_X, SCREEN_Y)
setBackgroundImage("images/bg_kaitenzushi.jpg")

# レール初期描画
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

# お皿初期描画
all_dishes = []
for i in range(DISH_NUM):
    dish = makeSprite("images/dish" + format(i, '02') + ".png")
    dish.x = DISH_WIDTH * (-1)
    dish.y = DISH_Y
    moveSprite(dish, dish.x, dish.y)
    showSprite(dish)
    all_dishes.append(dish)

# 満足メーター初期描画
meter = makeSprite("images/good0.png")
for i in range(METER_ALLIMAGE - 1):
    addSpriteImage(meter, "images/good" + str(i + 1) + ".png")
transformSprite(meter, 0, METER_SCALE)
moveSprite(meter, METER_X, METER_Y)
showSprite(meter)

# プレイヤー初期描画
player = makeSprite("images/aji000.png")
for i in range(PLAYER_ALLIMAGE - 1):
    addSpriteImage(player, "images/aji" + format(i + 1, '03') + ".png")
player_x = SCREEN_X / 2
transformSprite(player, 0, PLAYER_SCALE)
moveSprite(player, player_x, PLAYER_Y)
showSprite(player)
left = False
right = False

# スコア更新の関数
def kaikei(n):
    j = 0
    for i in range(KAIKEI_KETA):
        if KAIKEI_KETA - len(str(n)) > i:
            kaikei = makeImage("images/a.jpg")
        else:
            kaikei = makeImage("images/" + str(n)[j] + ".jpg")
            j += 1
        screen.blit(kaikei, (KAIKEI_X + KAIKEI_WIDTH * i, KAIKEI_Y))

# ループ初期値
nextFrame = clock()
playerImgNo = 0
score = 0
kaikei(score)
dish_appearflg = 0
meter_level = 0
game_continue = True

# メインループ
while True:
    if game_continue:
        # プレイヤーの操作判定　（入力なし）
        if not left and not right:
            if keyPressed("left"):
                playerImgNo = 0
                left = True
            if keyPressed("right"):
                playerImgNo = PLAYER_ALLIMAGE
                right = True
            player_x += DISH_MOVELEN
            moveSprite(player, player_x, PLAYER_Y)
            if player_x > SCREEN_X - PLAYER_WIDTH * PLAYER_SCALE:
                player_x = SCREEN_X - PLAYER_WIDTH * PLAYER_SCALE
    
        # プレイヤーの操作判定　（入力：左キー）
        if left:
            if clock() > nextFrame:
                playerImgNo += 1
                if playerImgNo > 26:
                    playerImgNo = 0
                    left = False
                    
                changeSpriteImage(player, playerImgNo)
                nextFrame = clock() + PLAYER_SPEED
                
                if playerImgNo > 6 and playerImgNo < 22:
                    player_x -= PLAYER_MOVELEN * PLAYER_SCALE
                    if player_x < 0:
                        player_x = 0
                else:
                    player_x += DISH_MOVELEN
                moveSprite(player, player_x, PLAYER_Y)
    
        # プレイヤーの操作判定　（入力：右キー）
        if right:
            if clock() > nextFrame:
                playerImgNo -= 1
                if playerImgNo < 0:
                    playerImgNo = 0
                    right = False
                    
                changeSpriteImage(player, playerImgNo)
                nextFrame = clock() + PLAYER_SPEED
                
                if playerImgNo > 6 and playerImgNo < 22:
                    player_x += PLAYER_MOVELEN * PLAYER_SCALE
                else:
                    player_x += DISH_MOVELEN
                if player_x > SCREEN_X - PLAYER_WIDTH * PLAYER_SCALE:
                    player_x = SCREEN_X - PLAYER_WIDTH * PLAYER_SCALE
                moveSprite(player, player_x, PLAYER_Y)
    
        # レールの描画
        for rail in all_rails:
            rail.x += DISH_MOVELEN
            if rail.x >= SCREEN_X:
                rail.x = SCREEN_X * (-1)
            moveSprite(rail, rail.x, RAIL_Y)
    
        # お皿の描画
        cnt = 1
        for dish in all_dishes:
            if dish_appearflg == 0 and dish.x == DISH_X and random() < DISH_APPEAR:
                dish.x += DISH_MOVELEN
                dish_appearflg = cnt
            if player_x > PLAYER_MOVELEN / 2:
                if (left and playerImgNo == 24) or (right and playerImgNo == 3):
                    if touching(player, dish):
                        dish.y += DISH_MOVELEN * 2
            if SCREEN_Y > dish.y > DISH_Y:
                dish.y += DISH_MOVELEN * 2
            if dish.y > SCREEN_Y:
                dish.y = SCREEN_Y
                score += DISH_VALUE
                kaikei(score)
            if dish.x > SCREEN_X:
                if dish.y == DISH_Y:
                    meter_level += 1
                    changeSpriteImage(meter, meter_level)
                    
                    # ゲームオーバー判定
                    if meter_level == METER_ALLIMAGE - 1:
                        game_continue = False
                        break
                dish.x = DISH_X
                dish.y = DISH_Y
            elif dish.x > DISH_X:
                moveSprite(dish, dish.x, dish.y)
                dish.x += DISH_MOVELEN
                if cnt == dish_appearflg and dish.x > 0:
                    dish_appearflg = 0
            cnt += 1
    else:
        pass
    
    tick(60)




