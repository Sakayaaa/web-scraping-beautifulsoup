import requests
from bs4 import BeautifulSoup as bs
import json
url = "https://en.wikipedia.org/wiki/Khabib_Nurmagomedov"
headers = {'User-agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
content = response.content
soup = bs(content, "html.parser")
tables = soup.find_all('table')

# ---- To find the target table(here is the table that contains Khabib's matches) ----#
target_table = None
found = False

for t in tables:
    if found:
        break

    first_row = t.find("tr")
    # ---- To prevent AttributeError from occuring in the following command: first_row.find_all("th")---- #
    if not first_row:
        continue

    for th in first_row.find_all("th"):
        if th.get_text(strip=True) == "Opponent":
            target_table = t
            found = True
            break

all_trs = target_table.find_all("tr")
opponents_list = []
for tr in all_trs:
    if tr.find_all("th"):
        continue

    opponent = tr.find_all("td")[2].get_text(strip=True)
    opponents_list.append(opponent)

json_opponents_list = json.dumps(opponents_list)

with open('opponents_list.json', "w", encoding="utf-8") as file:
    file.write(json_opponents_list)
