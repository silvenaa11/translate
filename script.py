import requests
import time

URLS = [
    "https://translate-1-nx5c.onrender.com",
    "https://translate-run-script-13af.onrender.com"
]

while True:
    for url in URLS:
        try:
            response = requests.get(url, timeout=10)
            print(f"Pinged {url}: {response.status_code}")
        except Exception as e:
            print(f"Error {url}: {e}")

    time.sleep(300)