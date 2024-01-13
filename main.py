import pandas as pd
import yfinance as yf

sp500_url = r"https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
dow_url = r"https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average#Components"

dow_table = pd.read_html(dow_url)[1]


# print(len(tables))
# print(pd.read_html(dow_url)[1])
# print(pd.read_html(dow_url)[1])
