import pandas as pd
import yfinance as yf

sp500_url = r"https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
dow_url = r"https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average#Components"

dow_symbols = pd.read_html(dow_url)[1]["Symbol"]
print(dow_symbols)

# ticker = yf.Ticker("AAPL")
# print(ticker.get_info().keys())
# print(ticker.get_fast_info().keys())

for symbol in dow_symbols:
    # print(symbol)
    ticker = yf.Ticker(symbol)
    print(ticker.get_fast_info()["marketCap"])

# Get market cap
# market_cap = quote_table[]

# ticker = []
# deltas = []
# sectors = []
# market_caps = []

# print(len(tables))
# print(pd.read_html(dow_url)[1])
# print(pd.read_html(dow_url)[1])
