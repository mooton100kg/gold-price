from bs4 import BeautifulSoup
import requests

URL = "https://ทองคําราคา.com"

result = requests.get(URL)
doc = BeautifulSoup(result.text, "html.parser")

price_tag = doc.find_all(["td"] ,string="ทองคำแท่ง")
parent = price_tag[0].parent
price = parent.find_all(["td"], class_="em bg-em g-d")[1]

print(price.text)
