# 🛍️ Price Glitch Tracker

This is a scalable, easy-to-use Python app that tracks product prices from major retailers and alerts you when price glitches occur.

## 📦 Features

- Monitor multiple URLs across various stores
- Get notified via Discord webhook
- Built-in Streamlit dashboard to view tracked products and settings
- Ready for cloud deployment via [Streamlit Community Cloud](https://streamlit.io/cloud)

---

## 🚀 How to Run Locally

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start the backend price checker
python main.py

# 3. (Optional) Launch Streamlit dashboard
streamlit run app.py
```

---

## ☁️ Deploy to Streamlit Cloud (Free)

1. Fork or clone this repo and push it to your own GitHub account
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **"New app"** and link your GitHub repo
4. Set the main file as `app.py`
5. Click **"Deploy"**

You'll get a public URL you can open on your iPhone or any device.

---

## 📁 Files

- `main.py` — core price scanner logic
- `products.csv` — list of product URLs and price thresholds
- `config.yaml` — configuration (webhook, refresh interval)
- `app.py` — Streamlit dashboard UI
- `requirements.txt` — dependencies

---

## 🧩 Customize It

- Add more store scrapers in `scrapers/`
- Modify `products.csv` to track new URLs
- Set a Discord webhook in `config.yaml` for notifications

---

## 📬 Questions?

Feel free to open an issue or contact the developer.