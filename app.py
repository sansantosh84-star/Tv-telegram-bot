import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    message = f"""
📊 TradingView Alert

Symbol: {data.get('symbol')}
Price: {data.get('price')}
Signal: {data.get('signal')}
"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=payload)
    return "ok", 200

@app.route("/")
def home():
    return "Bot is running"
