import requests
from bs4 import BeautifulSoup
from utils.price_parser import parse_price

def get_price_amazon(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.content, "lxml")
        price_tag = soup.find("span", {"class": "a-offscreen"})
        if price_tag:
            return parse_price(price_tag.text)
    except:
        return None