def parse_price(text):
    return float(text.replace("$", "").replace(",", "").strip())