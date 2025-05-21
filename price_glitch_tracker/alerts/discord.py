import requests
from utils.logger import log

def send_discord_alert(webhook_url, url, price):
    data = {
        "content": f"⚠️ **Price glitch?** `{price}` detected at:\n{url}"
    }
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            log(f"[ALERT] Sent for {url}")
        else:
            log(f"[ERROR] Discord failed: {response.status_code}")
    except Exception as e:
        log(f"[ERROR] Alert error: {e}")