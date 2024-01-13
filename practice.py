import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://pt.wikipedia.org/wiki/Lista_de_bairros_de_Manaus"
data = requests.get(url).text

soup = BeautifulSoup(data, "html.parser")
# print(soup)

# Verify tagbles and their classes
print("classes of each table: ")
for table in soup.find_all("table"):
    print(table.get("class"))

tables = soup.find_all("table")
# Find 2nd table cuz thats what we want
table = soup.find("table", class_="wikitable sortable")
# print(table)

# Data frame
df = pd.DataFrame(
    columns=["Neighborhood", "Zone", "Area", "Population", "Density", "Homes_count"]
)

# Collect data
for row in table.tbody.find_all("tr"):
    # Find all data for each colummn
    print(row)
    print("###########################################")
