import requests
from bs4 import BeautifulSoup

url = "https://www.crossfit.com/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
content = soup.select("p")
print("\n")
print("+-----------------------------------------------------------+")
print("CF Mainsite workout of the day:")
print("+-----------------------------------------------------------+")
print("\n")

for row in content:
    if row.get_text()[:4] == "Post":
        break
    else:
        print(row.get_text())

print("\n")
