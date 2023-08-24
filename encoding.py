#ライブラリインポート
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO
from sklearn.preprocessing import LabelEncoder

"""
1. データセットを準備
"""

csv_data = \
'''
Region,Sex,Age,Savings,Investment
Tokyo,Male,21,200000,No
Osaka,Female,25,2400000,No
Tokyo,Female,30,3200000,Yes
Fukuoka,Male,46,4600000,No
Osaka,Male,57,6500000,Yes
Osaka,Female,60,12000000,Yes
Fukuoka,Male,44,8000000,No
Saitama,Female,18,100000,No
'''

df = pd.read_csv(StringIO(csv_data))

# print(df)
"""
2. One Hot Encoding
"""

#One Hot Encoding
Region = pd.get_dummies(df["Region"],drop_first=True)

#Regionの列削除
df1= df.drop(["Region"],axis=1)

#DataFramae 結合＆新規生成
df1 = pd.concat([Region,df1],axis=1)

"""
3. Label Encoding
"""

df2 = df1.copy()

#Label Encoding: Sex(性別)
LE1 = LabelEncoder()
LE1.fit_transform(df1["Sex"].values)
df2["Sex"] = LE1.fit_transform(df1["Sex"].values)


#Label Encoding: Investment(投資経験)
LE2 = LabelEncoder()
LE2.fit_transform(df1["Investment"].values)
df2["Investment"] = LE2.fit_transform(df1["Investment"].values)

print(df1)