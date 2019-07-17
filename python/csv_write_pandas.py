import pandas as pd

# df = pd.read_csv('sample_pandas_normal.csv', index_col=0)

# df.to_csv('to_csv_out.csv')

# print(df)

calendar = [['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], ['a', 'b', 'c', 'd', 'e', 'f', 'g']]
df1 = pd.DataFrame(calendar)
print(df1)
df1.to_csv('to_csv_out1.csv', header=False, index=False) #ヘッダー（列名）、インデックス（行名）のありなしは引数header, indexにTrue or Falseで指定する。