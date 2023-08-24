#ライブラリをインポート
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

#データセットを準備
csv_data = \
'''
Region,Sex,Age,Deposit,Investment
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
print(df)