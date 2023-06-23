from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# print(doc.prettify())

tag = doc.title
print(tag)
