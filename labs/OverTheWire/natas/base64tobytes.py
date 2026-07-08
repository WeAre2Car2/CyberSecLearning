import base64

base64_string = "G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPI6OvVV0/nx5G9AX9oDiynMIofWMfVYExJLd0oiGd4/SnX9UET9Bj0m9rt/c0tByJk="

raw_bytes = base64.b64decode(base64_string)

for i in range(0, len(raw_bytes), 16):
    block = raw_bytes[i:i+16]
    print(i // 16, block.hex())

print(raw_bytes.hex())
print(f"Length: {len(raw_bytes)}")
