from selenium import webdriver
from decouple import config
import chromedriver_binary
import requests

driver = webdriver.Chrome()

driver.get('https://item.rakuten.co.jp/popinaladdin/xit-air110w/')

# 売り切れメッセージの有無で、メッセージを送信
soldOutMessage = "ポッピンアラジンの在庫状況："
try:
    inventoryStatus = driver.find_element_by_class_name('soldout_msg').text
    if inventoryStatus == '売り切れました':
        soldOutMessage = soldOutMessage + '在庫なし'
except Exception:
    soldOutMessage = soldOutMessage + '在庫復活！！！'
driver.quit()

# Lineに通知を送る
url = "https://notify-api.line.me/api/notify"
access_token = config('ACCESS_TOKEN')
headers = {'Authorization': 'Bearer ' + access_token}

payload = {'message': soldOutMessage}
r = requests.post(url, headers=headers, params=payload)




