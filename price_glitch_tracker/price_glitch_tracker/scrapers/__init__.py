from .amazon import get_price_amazon
from .walmart import get_price_walmart
from urllib.parse import urlparse

def get_price(url):
    domain = urlparse(url).netloc
    if "amazon." in domain:
        return get_price_amazon(url)
    elif "walmart." in domain:
        return get_price_walmart(url)
    else:
        return None