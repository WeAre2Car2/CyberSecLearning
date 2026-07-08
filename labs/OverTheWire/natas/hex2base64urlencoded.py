import base64
from urllib.parse import quote


hex_string = "1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf2070bdd4684c4270354b8f08f7cb5480e68b151738d0187c720487ee2912fdb22ca8cf4e610913abae39a067619204a5a"


# 1. Convert hex string to raw bytes
raw_bytes = bytes.fromhex(hex_string)

# 2. Convert raw bytes to normal Base64
base64_string = base64.b64encode(raw_bytes).decode("ascii")

# 3. URL-encode the Base64 string
url_encoded_base64 = quote(base64_string, safe="")

# 4. Optional: URL-safe Base64 variant
url_safe_base64 = base64.urlsafe_b64encode(raw_bytes).decode("ascii")


print("Raw bytes:")
print(raw_bytes)

print("\nNormal Base64:")
print(base64_string)

print("\nURL-encoded Base64:")
print(url_encoded_base64)

print("\nURL-safe Base64:")
print(url_safe_base64)