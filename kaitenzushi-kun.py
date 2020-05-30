from pygame_functions import *
from random import random

SCREEN_X = 1200             # 画面 横サイズ （ピクセル）
SCREEN_Y = 600              # 画面 縦サイズ （ピクセル）
RAIL_Y = 312                # レール 初期Y位置 （ピクセル）
DISH_MOVELEN = 5            # お皿 動く幅 （ピクセル）

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

# メインループ
while True:
    # レールの描画
    for rail in all_rails:
        rail.x += DISH_MOVELEN
        if rail.x >= SCREEN_X:
            rail.x = SCREEN_X * (-1)
        moveSprite(rail, rail.x, RAIL_Y)

    tick(60)




