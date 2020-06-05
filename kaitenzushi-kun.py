from pygame_functions import *
from random import random

SCREEN_X = 1200             # 画面 横サイズ （ピクセル）
SCREEN_Y = 600              # 画面 縦サイズ （ピクセル）
PLAYER_ALLIMAGE = 27        # プレイヤー アニメーション全コマ数
PLAYER_MOVELEN = 16         # プレイヤー 動く幅 （ピクセル）
PLAYER_WIDTH = 192          # プレイヤー 横サイズ （ピクセル）
PLAYER_HEIGHT = 160         # プレイヤー 縦サイズ （ピクセル）
PLAYER_SCALE = 1.5          # プレイヤー 画像の拡大率
PLAYER_Y = 380 - PLAYER_HEIGHT * PLAYER_SCALE - 20    # プレイヤー 初期Y位置 （ピクセル）
DISH_MOVELEN = 5            # お皿 動く幅 （ピクセル）

screen = screenSize(SCREEN_X, SCREEN_Y)
setBackgroundImage("images/bg_kaitenzushi.jpg")

# プレイヤー初期描画
player = makeSprite("images/aji000.png")
player_x = SCREEN_X / 2
transformSprite(player, 0, PLAYER_SCALE)
moveSprite(player, player_x, PLAYER_Y)
showSprite(player)
left = False
right = False

# メインループ
while True:
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
        playerImgNo += 1
        if playerImgNo > 26:
            playerImgNo = 0
            left = False
        player_x -= PLAYER_MOVELEN * PLAYER_SCALE
        if player_x < 0:
            player_x = 0
        moveSprite(player, player_x, PLAYER_Y)

    # プレイヤーの操作判定　（入力：右キー）
    if right:
        playerImgNo -= 1
        if playerImgNo < 0:
            playerImgNo = 0
            right = False
        player_x += PLAYER_MOVELEN * PLAYER_SCALE
        if player_x > SCREEN_X - PLAYER_WIDTH * PLAYER_SCALE:
            player_x = SCREEN_X - PLAYER_WIDTH * PLAYER_SCALE
        moveSprite(player, player_x, PLAYER_Y)
    
    tick(60)




