# -*- coding: utf-8 -*-

import bitflyerApiUtil
import messageUtil
import pyFxUtil

import time
import numpy as np

import sys, os

args = sys.argv
if len(args) != 3:
    print("invalid arguments recieved.")
    print("[" + str(args[0]) + "]")
    print("usage : python main.py <mode->0:test 1:release> <process_interval(sec)>")

#実行モード
mode = int(args[1])

#価格取得間隔
interval = int(args[2])

#設定ファイルパス
config_file = "./config/config.ini"
#設定ファイル存在確認
if not os.path.isfile(config_file):
    print("not found conf file -> [" + str(config_file) + "]")
    exit(0)

#api取得
try:
    api = bitflyerApiUtil.getBemApi(config_file)
except:
    print("get api error...  please contact for TAKA.")
    exit(1)

#ライン通知
#messageUtil.lineNotify("現在価格は{0}円".format(price))

#価格保持日数
days = 30

#価格保持配列
prices = np.zeros(days * 24 * 60)

#main loop
while True:
    time.sleep(interval)
    
    #BITCOIN現在価格取得
    price = bitflyerApiUtil.getCurrentPrice(api)

    #価格保持配列更新
    prices = pyFxUtil.updatePrices(prices, price)

    if mode == 0:
        print(prices)
