from bs4 import BeautifulSoup
import requests

url = "https://companiesmarketcap.com/dow-jones/largest-companies-by-market-cap/"
res = requests.get(url)

# We want Company code (and maybe name)
# 2nd column, class company-code
# And for each company, their market cap
soup = BeautifulSoup(res.text, "lxml")
table = soup.find("table")
# print(table)
tbody = table.find("tbody")

print(tbody)
rows = tbody.find_all("tr")
# print(rows)
# print(len(rows))


symbols = []
market_caps = []
sizes = []


# print(rows[0].findAll("td"))

# for row in rows:
# columns = row
# for row in rows:
#     # columns = row.find_all("td")
#     print(row)
# print(soup)
# print(res.status_code)
# print(res.headers)
# print(res.text)
