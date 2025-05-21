import schedule
import time
import csv
from utils.logger import log
from scrapers import get_price
from alerts.discord import send_discord_alert
import yaml

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

INTERVAL = config.get("interval_minutes", 5)
DISCORD_WEBHOOK = config.get("discord_webhook", "")

def check_prices():
    log("🔍 Checking prices...")
    with open("products.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            url = row['url']
            threshold = float(row['threshold'])

            price = get_price(url)
            if price is None:
                log(f"[WARN] Could not get price for {url}")
                continue

            if price < threshold:
                log(f"🔥 GLITCH? {price} < {threshold} for {url}")
                send_discord_alert(DISCORD_WEBHOOK, url, price)
            else:
                log(f"✅ OK: {price} for {url}")

schedule.every(INTERVAL).minutes.do(check_prices)

log(f"⏱️ Tracker started. Checking every {INTERVAL} min.")
check_prices()
while True:
    schedule.run_pending()
    time.sleep(1)