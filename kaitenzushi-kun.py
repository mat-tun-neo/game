from pygame_functions import *
from random import random

SCREEN_X = 1200             # 画面 横サイズ （ピクセル）
SCREEN_Y = 600              # 画面 縦サイズ （ピクセル）
PLAYER_IMAGE = "aji"         # プレイヤー 画像ファイル名
PLAYER_ALLIMAGE = 27        # プレイヤー アニメーション全コマ数
PLAYER_WIDTH = 192          # プレイヤー 横サイズ （ピクセル）
PLAYER_HEIGHT = 160         # プレイヤー 縦サイズ （ピクセル）
PLAYER_SCALE = 2            # プレイヤー 画像の拡大率
PLAYER_Y = 100              # プレイヤー 初期Y位置 （ピクセル）
RAIL_Y = 312                # レール 初期Y位置 （ピクセル）

screen = screenSize(SCREEN_X, SCREEN_Y)

# プレイヤー初期描画
player = makeSprite("images/" + PLAYER_IMAGE + "000.png")
for i in range(PLAYER_ALLIMAGE - 1):
    addSpriteImage(player, "images/" + PLAYER_IMAGE + format(i + 1, '03') + ".png")
player_x = SCREEN_X / 2 - PLAYER_WIDTH
transformSprite(player, 0, PLAYER_SCALE)
moveSprite(player, player_x, PLAYER_Y)
showSprite(player)

# ループ初期値
playerImgNo = 0

# メインループ
while True:
    playerImgNo += 1
    if playerImgNo == PLAYER_ALLIMAGE:
        playerImgNo = 0
    changeSpriteImage(player, playerImgNo)
    
    tick(20)




