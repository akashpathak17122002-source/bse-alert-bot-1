import requests
import feedparser
import time

BOT_TOKEN = "8397682017"
CHAT_ID = "1190833695"

RSS_URL = "https://www.bseindia.com/xml-data/corpfiling/AttachLive/rss.xml"

sent_news = set()

def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=data)

while True:

    feed = feedparser.parse(RSS_URL)

    for entry in feed.entries:

        title = entry.title
        link = entry.link

        keywords = [
            "Equity",
            "F&O",
            "Board Meeting",
            "Result"
        ]

        if any(word in title for word in keywords):

            if title not in sent_news:

                msg = f"""
🚨 BSE ALERT 🚨

{title}

🔗 {link}
"""

                send_message(msg)

                sent_news.add(title)

                print("Sent:", title)

    time.sleep(60)
