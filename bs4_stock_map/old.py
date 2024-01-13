from bs4 import BeautifulSoup
import requests
from selenium import webdriver

url = "https://companiesmarketcap.com/dow-jones/largest-companies-by-market-cap/"

# Create a browser
driver = webdriver.Chrome()
driver.get(url)

# Get page source after interaction
page_source = driver.page_source

# Parse...


# data = requests.get(url).text
# print(data)

# We want Company code (and maybe name)
# 2nd column, class company-code
# And for each company, their market cap
soup = BeautifulSoup(page_source, "lxml")
print(soup)
table = soup.find("table")
print(table)
rows = table.find_all("tr")

driver.quit()
# print(rows)
