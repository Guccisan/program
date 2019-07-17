# pythonの絵本p179参照
# 必ず2つのモジュールをインポートする
import requests
from bs4 import BeautifulSoup

# webページ取得
req = requests.get('https://www.shoeisha.co.jp/book/upcoming') #webページを取得する

# 取得したwebページのhtmlを出力
print(req.text)