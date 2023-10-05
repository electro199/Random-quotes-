import json
import requests
from pprint import pprint

import bs4 as bs

Page_url = "https://www.heloplus.com/quotes/sad-quotes-in-english/"  #


source = requests.get(Page_url).text


soup = bs.BeautifulSoup(source, "html.parser")

el = soup.find_all("blockquote")


# for br in el.find_all("br"):
#     br.replace_with("\n")

r = {"site": Page_url, "qoutes": [e.get_text() for e in el]}
# data = json.loads(r)
# pprint(r, indent=2)


with open("love-quotes5.json", "w", encoding="utf-8") as f:
    json.dump(r, f, indent=2, ensure_ascii=False)
#     print(json.load(f))
