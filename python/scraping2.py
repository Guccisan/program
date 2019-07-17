import requests
from bs4 import BeautifulSoup

file = open('test1.txt', 'w') #txtファイルを開く

req = requests.get('https://www.shoeisha.co.jp/book/upcoming')
soup = BeautifulSoup(req.text, 'html.parser') #htmlを解析する

div = soup.find('div', {'class':'column'}) #class属性がcolumのdivの内容を取得する

# 上で取得したdiv内のliの内容をすべて取得する
for book in div.findAll('li'):
    print(book.find('span').get_text() + ':')
    print(book.find('a').get_text())
    file.write(book.find('span').get_text() + ':\n')
    file.write(book.find('a').get_text() + '\n')

file.close() #txtファイルを閉じる