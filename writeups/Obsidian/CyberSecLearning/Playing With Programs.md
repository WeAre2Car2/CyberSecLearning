## Dealing with Data


##### Gleaning Challenge Insight
1. Read the challenge!
2. USE the code of the challenge!
##### What's the Password?
```
hacker@data-dealings~whats-the-password:~$ cat /challenge/runme buffihei
#!/usr/bin/exec-suid -- /bin/python3 -I

import sys


print("Enter the password:")
entered_password = sys.stdin.buffer.read1().strip()
correct_password = b"buffihei"

print(f"Read {len(entered_password)} bytes.")


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
cat: buffihei: No such file or directory
hacker@data-dealings~whats-the-password:~$ /challenge/runme buffihei
Enter the password:
buffihei
Read 8 bytes.
Congrats! Here is your flag:
```

As simple as it can be. Just read the code.
##### ... and Again
```
hacker@data-dealings~-and-again:~$ cat /challenge/runme 
#!/usr/bin/exec-suid -- /bin/python3 -I

import sys


print("Enter the password:")
entered_password = sys.stdin.buffer.read1().strip()
correct_password = b"fbharpsp"

print(f"Read {len(entered_password)} bytes.")


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
hacker@data-dealings~-and-again:~$ /challenge/runme 
Enter the password:
fbharpsp
Read 8 bytes.
Congrats! Here is your flag:
```

##### Newline Troubles
```
hacker@data-dealings~newline-troubles:~$ /challenge/runme
Enter the password:
rhufyrrlRead 8 bytes.
Congrats! Here is your flag:

```
Using CTRL + D

```
hacker@data-dealings~newline-troubles:~$ echo -n "rhufyrrl" | /challenge/runme
Enter the password:
Read 8 bytes.
Congrats! Here is your flag:
```
Using echo and pipe

##### Reasoning About Files
```
hacker@data-dealings~reasoning-about-files:~$ cat /challenge/runme 
#!/usr/bin/exec-suid -- /bin/python3 -I

import sys


try:
    entered_password = open("iqvn", "rb").read()
except FileNotFoundError:
    print("Input file not found...")
    sys.exit(1)
if b"\n" in entered_password:
    print("Password has newlines /")
    print("Editors add them sometimes /")
    print("Learn to remove them.")

correct_password = b"xgfkvmlb"

print(f"Read {len(entered_password)} bytes.")


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
```

Ok. the open command makes me think that I need to make a file with the password contents in it and it will read it and give me the password. A file named "iqvn". But what does the "rb" mean? Lets search! it means reading in binary. So perhaps I need to encode it in binary.
```
hacker@data-dealings~reasoning-about-files:~/Dealing_With_Data$ /challenge/runme 
Read 8 bytes.
Congrats! Here is your flag:
```
with a file named "iqvn" with contents of "xgfkvmlb".

##### Specifying Filenames
```
hacker@data-dealings~specifying-filenames:~$ cat /challenge/runme 
#!/usr/bin/exec-suid -- /bin/python3 -I

import sys


try:
    entered_password = open(sys.argv[1], "rb").read()
except FileNotFoundError:
    print("Input file not found...")
    sys.exit(1)
if b"\n" in entered_password:
    print("Password has newlines /")
    print("Editors add them sometimes /")
    print("Learn to remove them.")

correct_password = b"lakumkny"

print(f"Read {len(entered_password)} bytes.")


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
```
So I specify the file name? I assume.
```
hacker@data-dealings~specifying-filenames:~/Dealing_With_Data$ /challenge/runme flag_pls
Read 8 bytes.
Congrats! Here is your flag:
```

##### Binary and Hex Encoding
```
hacker@data-dealings~binary-and-hex-encoding:~/Dealing_With_Data$ cat /challenge/runme 
#!/usr/bin/exec-suid -- /bin/python3 -I

import sys


print("Enter the password:")
entered_password = sys.stdin.buffer.read1()
correct_password = b"\xc4"

print(f"Read {len(entered_password)} bytes.")


entered_password = bytes.fromhex(entered_password.decode("l1"))


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
```
So basically: Enter the value of correct password in hex and we will encode to bytes and compare it.
```
hacker@data-dealings~binary-and-hex-encoding:~/Dealing_With_Data$ /challenge/runme 
Enter the password:
C4
Read 3 bytes.
Congrats! Here is your flag:
```

##### More Hex
```
hacker@data-dealings~more-hex:~/Dealing_With_Data$ cat /challenge/runme 
#!/usr/bin/exec-suid -- /bin/python3 -I

import sys


print("Enter the password:")
entered_password = sys.stdin.buffer.read1()
correct_password = b"\xbe\xb0\x9b\x9e\xe9\xcf\xe3\xbc"

print(f"Read {len(entered_password)} bytes.")


entered_password = bytes.fromhex(entered_password.decode("l1"))


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
```
I made a python file to help me with this challenge:
```
correct_password = b"\xbe\xb0\x9b\x9e\xe9\xcf\xe3\xbc"

encoded_data = correct_password.hex()

print (f"Encoded data: {encoded_data}")
```
```
hacker@data-dealings~more-hex:~/Dealing_With_Data$ /challenge/runme 
Enter the password:
beb09b9ee9cfe3bc
Read 17 bytes.
Congrats! Here is your flag:
```

##### Decoding Hex
```
hacker@data-dealings~decoding-hex:~$ cat /challenge/runme 
#!/usr/bin/exec-suid -- /bin/python3 -I

import sys


print("Enter the password:")
entered_password = sys.stdin.buffer.read1()
correct_password = b"80fbe4dea3a599b5"

print(f"Read {len(entered_password)} bytes.")


correct_password = bytes.fromhex(correct_password.decode("l1"))


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
```
hex -> bytes
```
import pwn

  

p = pwn.process("/challenge/runme")

password = bytes.fromhex("80fbe4dea3a599b5")

p.send(password)

10

p.shutdown("send")

print(p.recvall().decode())
```
```
hacker@data-dealings~decoding-hex:~/Dealing_With_Data$ Decoding_hex.py
bash: Decoding_hex.py: command not found
hacker@data-dealings~decoding-hex:~/Dealing_With_Data$ python Decoding_Hex.py 
[+] Starting local process '/challenge/runme': pid 2089
[+] Receiving all data: Done (124B)
[*] Process '/challenge/runme' stopped with exit code 0 (pid 2089)
Enter the password:
Read 8 bytes.
Congrats! Here is your flag:
```

##### Decoding Practice
```
hacker@data-dealings~decoding-practice:~$ cat /challenge/runme 
#!/usr/bin/exec-suid -- /bin/python3 -I

import sys


def decode_from_bits(s):
    s = s.decode("latin1")
    assert set(s) <= {"0", "1"}, "non-binary characters found in bitstream!"
    assert len(s) % 8 == 0, "must enter data in complete bytes (each byte is 8 bits)"
    return int.to_bytes(int(s, 2), length=len(s) // 8, byteorder="big")


print("Enter the password:")
entered_password = sys.stdin.buffer.read1()
correct_password = b"1111000111000000110001001100101010000110100000111000110010101000"

print(f"Read {len(entered_password)} bytes.")


correct_password = decode_from_bits(correct_password)


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
```

```
import pwn

  

p = pwn.process("/challenge/runme")

bits = "1111000111000000110001001100101010000110100000111000110010101000"

s = bits.encode("latin1")

bytes = int.to_bytes(int(s, 2), length=len(s) // 8, byteorder="big")

p.send(bytes)

p.shutdown("send")

print(p.recvall().decode())
```
I used the function from the challenge itself.

##### Encoding Practice
```
hacker@data-dealings~encoding-practice:~/Dealing_With_Data$ cat /challenge/runme 
#!/usr/bin/exec-suid -- /bin/python3 -I

import sys


def decode_from_bits(s):
    s = s.decode("latin1")
    assert set(s) <= {"0", "1"}, "non-binary characters found in bitstream!"
    assert len(s) % 8 == 0, "must enter data in complete bytes (each byte is 8 bits)"
    return int.to_bytes(int(s, 2), length=len(s) // 8, byteorder="big")


print("Enter the password:")
entered_password = sys.stdin.buffer.read1()
correct_password = b"\xf5\xbe\xa1\xf5\x82\x83\x85\xf6"

print(f"Read {len(entered_password)} bytes.")


entered_password = decode_from_bits(entered_password)


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
```
```
import pwn

  

p = pwn.process("/challenge/runme")

data = b"\xf5\xbe\xa1\xf5\x82\x83\x85\xf6"

bit_string = "".join(f"{byte:08b}" for byte in data)

p.send(bit_string)

p.shutdown("send")

print(p.recvall().decode())
```

##### Hex-encoding ASCII
That was a long read.
```
hacker@data-dealings~hex-encoding-ascii:~/Dealing_With_Data$ cat /challenge/runme 
#!/usr/bin/exec-suid -- /bin/python3 -I

import sys


try:
    entered_password = open("xpln", "rb").read()
except FileNotFoundError:
    print("Input file not found...")
    sys.exit(1)
correct_password = b"lmuxtxjy"

print(f"Read {len(entered_password)} bytes.")


entered_password = bytes.fromhex(entered_password.decode("l1"))


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
```
```
import pwn

  

p = pwn.process("/challenge/runme")

p.shutdown("send")

print(p.recvall().decode())
```
xpln file:
6c6d757874786a79
with:
```
import sys

  

correct_password = b"lmuxtxjy"

  

print(correct_password.hex())
```

##### Nested Encoding
```
import sys


try:
    entered_password = open(sys.argv[1], "rb").read()
except FileNotFoundError:
    print("Input file not found...")
    sys.exit(1)
correct_password = b"pqpgkupc"

print(f"Read {len(entered_password)} bytes.")


entered_password = bytes.fromhex(entered_password.decode("l1"))
entered_password = bytes.fromhex(entered_password.decode("l1"))
entered_password = bytes.fromhex(entered_password.decode("l1"))
entered_password = bytes.fromhex(entered_password.decode("l1"))


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
```

The Tale of the String (wow)

hex
hex
hex
hex
pqpgkupc

Much wow.
and I get to give my own filename!
Lets use the helper file from last time.
```
import sys

  

correct_password = b"pqpgkupc"

correct_password = correct_password.hex().encode()

correct_password = correct_password.hex().encode()

correct_password = correct_password.hex().encode()

correct_password = correct_password.hex().encode()

  

print(correct_password)
```
```
hacker@data-dealings~nested-encoding:~$ /run/dojo/bin/python /home/hacker/Dealing_With_Data/shit.py
b'33333337333333303333333733333331333333373333333033333336333333373333333633363332333333373333333533333337333333303333333633333333'
```
file: wtf
```
import pwn

  

p = pwn.process(["/challenge/runme", "wtf"])

p.shutdown("send")

print(p.recvall().decode())
```

##### Hex-encoding UTF-8
```
import sys


try:
    entered_password = open(sys.argv[1], "rb").read()
except FileNotFoundError:
    print("Input file not found...")
    sys.exit(1)
correct_password = "😚 🚯 🏣 🔼".encode("utf-8")

print(f"Read {len(entered_password)} bytes.")


entered_password = bytes.fromhex(entered_password.decode("l1"))


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
```
```
import pwn

  

p = pwn.process(["/challenge/runme", "emojis"])

p.shutdown("send")

print(p.recvall().decode())
```
```
import sys

  

correct_password = "😚 🚯 🏣 🔼".encode("utf-8")

correct_password = correct_password.hex().encode()

  
  

print(correct_password)
```
Simple decoding.

##### UTF Mixups
```
import sys


print("Enter the password:")
entered_password = sys.stdin.buffer.read1()
correct_password = b"cohijjwo"

print(f"Read {len(entered_password)} bytes.")

assert entered_password != correct_password

entered_password = entered_password.decode("utf-16")
entered_password = entered_password.encode("latin1")


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
```
so lets decode it and then encode it as utf-16
```
import sys

  

correct_password = "cohijjwo"

correct_password = correct_password.encode("utf-16")

  
  

print(correct_password)
```
```
import pwn

  

p = pwn.process("/challenge/runme")

data = b"\xff\xfec\x00o\x00h\x00i\x00j\x00j\x00w\x00o\x00"

p.send(data)

p.shutdown("send")

print(p.recvall().decode())
```

##### Modifying Encoded Data
```
hacker@data-dealings~modifying-encoded-data:~$ cat /challenge/runme 
#!/usr/bin/exec-suid -- /bin/python3 -I

import sys


def reverse_string(s):
    return s[::-1]


print("Enter the password:")
entered_password = sys.stdin.buffer.read1()
correct_password = b"\xdcr\x9dn\x14W\xab\xbe"

print(f"Read {len(entered_password)} bytes.")


entered_password = entered_password[::-1]
entered_password = bytes.fromhex(entered_password.decode("l1"))


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
```
encode - hex - reverse?
```
import sys

  

correct_password = b"\xdcr\x9dn\x14W\xab\xbe"

correct_password = correct_password.hex()

correct_password = correct_password[::-1]

  
  

print(correct_password)
ebba7541e6d927cd
```
```
import pwn

  

p = pwn.process("/challenge/runme")

data = "ebba7541e6d927cd"

p.send(data)

p.shutdown("send")

print(p.recvall().decode())
```

##### Decoding Base64
```
hacker@data-dealings~decoding-base64:~/Dealing_With_Data$ cat /challenge/runme 
#!/usr/bin/exec-suid -- /bin/python3 -I

import sys

import base64


print("Enter the password:")
entered_password = sys.stdin.buffer.read1()
correct_password = b"XH16gGsHceo="

print(f"Read {len(entered_password)} bytes.")


correct_password = base64.b64decode(correct_password.decode("l1"))


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
```
so I need to encode data in base64 that will end up being "XH16gGsHceo="
No, I am just dumb at reading code. Just decode this shit.
```
import pwn

import sys

import base64

  

correct_password = "XH16gGsHceo="

correct_password = correct_password.encode("l1")

base64_bytes = base64.b64decode(correct_password)

correct_password = base64_bytes.decode("l1")

  
  

p = pwn.process("/challenge/runme")

p.send(correct_password)

p.shutdown("send")

print(p.recvall().decode())
```

##### Encoding Base64
```

import sys

import base64


print("Enter the password:")
entered_password = sys.stdin.buffer.read1()
correct_password = b"\rQR\x9e\xae*\xe6\xf2"

print(f"Read {len(entered_password)} bytes.")


entered_password = base64.b64decode(entered_password.decode("l1"))


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
```
```
import pwn

import sys

import base64

  

correct_password = b"\rQR\x9e\xae*\xe6\xf2"

base64_bytes = base64.b64encode(correct_password)

correct_password = base64_bytes.decode("l1")

  
  

p = pwn.process("/challenge/runme")

p.send(correct_password)

p.shutdown("send")

print(p.recvall().decode())
```

##### Dealing with Obfuscation
```
import sys

import base64


def encode_to_bits(s):
    return b"".join(format(c, "08b").encode("latin1") for c in s)


print("Enter the password:")
entered_password = sys.stdin.buffer.read1()
correct_password = b'"\n\xcatn\xa6}\xf2'

print(f"Read {len(entered_password)} bytes.")


correct_password = correct_password.hex().encode("l1")
correct_password = encode_to_bits(correct_password)
correct_password = base64.b64encode(correct_password)
correct_password = correct_password.hex().encode("l1")


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
```
```
import base64

import pwn

  
  

def encode_to_bits(s):

    return b"".join(format(c, "08b").encode("latin1") for c in s)

  

correct_password = b'"\n\xcatn\xa6}\xf2'

  

correct_password = correct_password.hex().encode("l1")

correct_password = encode_to_bits(correct_password)

correct_password = base64.b64encode(correct_password)

correct_password = correct_password.hex().encode("l1")

  

p = pwn.process("/challenge/runme")

p.send(correct_password)

p.shutdown("send")

print(p.recvall().decode())
```

##### Dealing with Obfuscation 2
```

import sys

import base64


def reverse_string(s):
    return s[::-1]


print("Enter the password:")
entered_password = sys.stdin.buffer.read1()
correct_password = b"\xc8\xf2#\xb4\x94@\x82N"

print(f"Read {len(entered_password)} bytes.")


entered_password = entered_password[::-1]
entered_password = base64.b64decode(entered_password.decode("l1"))
entered_password = bytes.fromhex(entered_password.decode("l1"))
entered_password = entered_password[::-1]

correct_password = correct_password[::-1]
correct_password = correct_password.hex().encode("l1")
correct_password = correct_password[::-1]
correct_password = correct_password[::-1]


if entered_password == correct_password:
    print("Congrats! Here is your flag:")
    print(open("/flag").read().strip())
else:
    print("Incorrect!")
    sys.exit(1)
```

```
import base64

import pwn

import sys

  

def reverse_string(s):

    return s[::-1]

  

correct_password = b"\xc8\xf2#\xb4\x94@\x82N"

  

correct_password = correct_password[::-1]

correct_password = correct_password.hex().encode("l1") # Encoding the correct password

  

correct_password = correct_password[::-1]

correct_password = bytes.hex(correct_password)

correct_password = base64.b64encode(correct_password.encode("l1"))

  

correct_password = correct_password[::-1]

  

p = pwn.process("/challenge/runme")

p.send(correct_password)

p.shutdown("send")

print(p.recvall().decode())
```

Finished Dealing with Data