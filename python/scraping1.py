import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.shoeisha.co.jp/book/upcoming') #webページを取得する

print(req.text)