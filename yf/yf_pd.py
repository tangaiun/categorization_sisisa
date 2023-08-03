import pandas as pd
import yfinance as yf
import datetime

#アップルの株価データを取得
aapl = yf.download(tickers='AAPL', 
                   start='2021-01-01', 
                   end=datetime.date.today(),
                   auto_adjust=True)

print(aapl)

