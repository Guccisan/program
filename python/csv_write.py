# csvモジュールでcsvの書き込み
import csv

l = []
l.append(100)
l.append(200)

with open('output/csv_write_out.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    writer.writerow([0, '目標', '手段'])
    writer.writerow([1, '未経験転職', 'テックアカデミーのJavaエンジニアコース'])
    writer.writerow([2, 'AI機械学習', 'テックアカデミーのPythonコース'])
    writer.writerow([3, '上級スキル習得', 'テックアカデミーのオーダーメイドコース'])
    writer.writerow(l) # listをcsvに書き込み

    # listの[]を消すために数値をstringに変換してprint
    # ""の中にデータの区切り毎に入れたい文字(,など)を書く
    print( " ".join( repr(e) for e in l ) ) 