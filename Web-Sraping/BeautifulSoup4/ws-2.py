from bs4 import BeautifulSoup
import requests

# HTML URL
url = "https://www.newegg.ca/gigabyte-geforce-rtx-4090-gv-n4090gaming-oc-24gd/p/N82E16814932550?Item=N82E16814932550"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
# print(result.text)
# print(doc.prettify())
# prices = doc.find_all(text="$") # doesn't work any more
prices = doc.find_all(string="$")  # this does
parent = prices[0].parent
strong = parent.find("strong")
# print(parent)
# print(strong)
print(strong.string)
