import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import squarify


DOWJONES_LENGTH = 30
sp500_url = r"https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
dow_url = r"https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average#Components"

dow_symbols = pd.read_html(dow_url)[1]["Symbol"]
print(dow_symbols)

# ticker = yf.Ticker("AAPL")
# print(ticker.get_info().keys())
# print(ticker.get_fast_info().keys())
tickers = []
market_caps = []

for ticker in dow_symbols:
    try:
        ## Append to tickers
        tickers.append(ticker)
        ## Download marketCap
        stock = yf.Ticker(ticker)
        market_cap = stock.get_fast_info()["marketCap"]
        # TODO: We can format numbers nicely?

        market_caps.append(market_cap)
        # market_caps[symbol] = market_cap
    except Exception as e:
        print(e)

print("Market Cap for DOWJONES downloaded.")

## Plot a heat map using plotly
df = pd.DataFrame({"ticker": tickers, "market_cap": market_caps})

labels = [
    f"{df.loc[i, 'ticker']}\n{df.loc[i, 'market_cap']}" for i in range(len(dow_symbols))
]

# print(labels)

colors = [plt.cm.tab20c(i / float(len(dow_symbols))) for i in range(len(dow_symbols))]

squarify.plot(
    sizes=market_caps,
    label=labels,
    color=colors,
    bar_kwargs={"linewidth": 0.5, "edgecolor": "#111111"},
)

plt.title("DowMap")
plt.savefig("dow_plot.png")
plt.close()
# color_bin = [-1, -0.02, -0.01, 0, 0.01, 0.02, 1]
# df["colors"] = pd.cut(
#     df["market_cap"],
#     bins=color_bin,
#     labels=["red", "indianred", "lightpink", "lightgreen", "lime", "green"],
# )

# print(df)
# Get market cap
# market_cap = quote_table[]

# ticker = []
# deltas = []
# sectors = []
# market_caps = []

# print(len(tables))
# print(pd.read_html(dow_url)[1])
# print(pd.read_html(dow_url)[1])
