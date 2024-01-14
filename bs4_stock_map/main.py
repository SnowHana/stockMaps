# import matplotlib

# matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import squarify

url = "https://companiesmarketcap.com/dow-jones/largest-companies-by-market-cap/"

# Create a browser
response = requests.get(url)
soup = BeautifulSoup(response.content, "html5lib")

rows = soup.table.select("tr")

# print(rows)

symbols = []
market_caps = []
sizes = []
for row in rows:
    try:
        symbol = row.find("div", {"class": "company-code"}).text
        # print(symbol)
        symbols.append(symbol)

        market_cap = row.findAll("td")[3].text
        # print(market_cap)
        market_caps.append(market_cap)

        # Now Clean market cap
        multiplier = 1
        if market_cap.endswith("T"):
            multiplier = 10**12
            # print(size)
        elif market_cap.endswith("B"):
            multiplier = 10**9
            # print(size)
        else:
            print("ERROR")

        size = float(market_cap[1:-2]) * multiplier
        sizes.append(size)
    except AttributeError:
        pass

labels = [f"{symbols[i]}\n{market_caps[i]}" for i in range(len(symbols))]
colors = [plt.cm.tab20c(i / float(len(symbols))) for i in range(len(symbols))]

squarify.plot(
    sizes=sizes,
    label=labels,
    color=colors,
    alpha=0.7,
    bar_kwargs={"linewidth": 0.5, "edgecolor": "#111111"},
)

plt.show()
