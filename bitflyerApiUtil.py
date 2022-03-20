import pybitflyer
import configparser

#API取得関数
def getBemApi(conf_file):
    try:
        conf = configparser.ConfigParser()
        conf.read(conf_file)
    except:
        print("init file error.")

    ACCESS_KEY = conf['bem']['access_key']
    SECRET_KEY = conf['bem']['secret_key']
    
    return pybitflyer.API(api_key=ACCESS_KEY, api_secret=SECRET_KEY)


#PYBITFLYER APIラッパー

#現在価格取得
def getCurrentPrice(api):
    try:
        price = api.ticker(product_code = "FX_BTC_JPY")['ltp']
    except:
        print("get ltp error")
        time.sleep(5)
        price = getCurrentPrice()
    return price