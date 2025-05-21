import requests
from bs4 import BeautifulSoup
from utils.price_parser import parse_price

def get_price_walmart(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.content, "lxml")
        price_tag = soup.find("span", {"class": "price-characteristic"})
        if price_tag and price_tag.get("content"):
            return float(price_tag["content"])
    except:
        return None