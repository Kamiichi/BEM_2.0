# BEM_2.0
This repository provides us to become a millionaire.

BEM2.0 2022/03/01

# テストスクリプト

- main.py<br>
メインスクリプト

- messageUtil.py<br>
ライン通知用共通関数

- bitflyerApiUtil<br>
ビットフライヤーAPI取得／動作用関数

- config.ini<br>
APIキー

# 依存ライブラリ
- pybitflyer
- request
- configparser
- numpy

# コマンド
> python main.py

usage : python main.py {mode- 0:test 1:release} {process_interval(sec)}

### sample
> pyhon3 main.py 0 1