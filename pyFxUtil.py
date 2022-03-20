import numpy as np

#価格更新関数
def updatePrices(old_prices, price):
    new_prices = np.roll(old_prices, 1)
    new_prices[0] = price
    return new_prices