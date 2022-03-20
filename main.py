import bitflyerApiUtil
import messageUtil
import pyFxUtil

import time
import numpy as np

#api取得
api = bitflyerApiUtil.getBemApi('config.ini')

#ライン通知
#messageUtil.lineNotify("現在価格は{0}円".format(price))

#価格保持日数
days = 30

#価格取得間隔
interval = 60

#価格保持配列
prices = np.zeros(days * 24 * 60)

#main loop
while True:
    time.sleep(interval)
    
    #BITCOIN現在価格取得
    price = bitflyerApiUtil.getCurrentPrice(api)

    #価格保持配列更新
    prices = pyFxUtil.updatePrices(prices, price)

    