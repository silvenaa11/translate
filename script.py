import requests
import time

URL = "https://translate-xqr9.onrender.com"
URL = "https://translate-run-script.onrender.com"

while True:
    try:
        response = requests.get(URL)
        response1 = requests.get(URL)
        print(f"Pinged: {response.status_code}")
        print(f"Pinged: {response1.status_code}")
    except Exception as e:
        print("Error:", e)

    time.sleep(300)  # 5 minut