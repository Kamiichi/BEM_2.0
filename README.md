# BEM_2.0
This repository provides us to become a millionaire.

BEM2.0 2022/03/01

# テストスクリプト
　①main.py
  ②messageUtil.py
  ③bitflyerApiUtil.py
  ④config.ini

①main.py
メインスクリプト

②messageUtil.py
ライン通知用共通関数

③bitflyerApiUtil
ビットフライヤーAPI取得／動作用関数

④config.ini
APIキー

# 依存ライブラリ
　- pybitflyer
  - request
  - configparser

# コマンド
> python main.py

usage : python main.py {mode- 0:test 1:release} {process_interval(sec)}

### sample
> pyhon3 main.py 0 1