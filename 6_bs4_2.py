import requests
from bs4 import BeautifulSoup
import re

url = "https://www.zillow.com/dublin-ca/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.02855185009764%2C%22east%22%3A-121.79165914990233%2C%22south%22%3A37.63027553636415%2C%22north%22%3A37.81032670468355%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A51751%2C%22regionType%22%3A6%7D%5D%2C%22mapZoom%22%3A12%2C%22filterState%22%3A%7B%7D%2C%22isListVisible%22%3Atrue%2C%22isMapVisible%22%3Afalse%7D"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

price = soup.find("span", attrs={"class":"ds-value"})
print(price)

total_price = 0
prices = soup.find_all("div", attrs={"class":"list-card-price"})
for price in prices:
    # print(price.get_text())
    num_p = re.sub("[^\d\.]", "", price.get_text())
#     num_p = ''.join(e for e in price if e.isdigit() or e == '.')
    # print(num_p)
    total_price += float(num_p)
print(total_price)
print(total_price / len(prices))