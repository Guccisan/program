# pythonの絵本p180参照
# 必ず2つのモジュールをインポートする
import requests
from bs4 import BeautifulSoup

# txtファイルを開く
file = open('output/test1.txt', 'w') 

# htmlを解析する
req = requests.get('https://www.shoeisha.co.jp/book/upcoming')
soup = BeautifulSoup(req.text, 'html.parser') 

# class属性がcolumのdivの内容を取得する
div = soup.find('div', {'class':'column'})

# 上で取得したdiv内のliの内容をすべて取得する
for book in div.findAll('li'):
    print(book.find('span').get_text() + ':')
    print(book.find('a').get_text())
    file.write(book.find('span').get_text() + ':\n')
    file.write(book.find('a').get_text() + '\n')

 # txtファイルを閉じる
file.close()