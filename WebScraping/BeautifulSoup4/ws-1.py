from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# print(doc.prettify())

tag = doc.title
# print(tag)
# print(tag.string)

# tag.string = "hello"
# print(tag.string)
# print(doc)

tags = doc.find_all("p")

print(tags)
