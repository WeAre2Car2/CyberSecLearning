##### Your First HTTP Request
As simple as it can be.

BTW, for now I skipped the videos because I have the beginner knowledge for web. If necessary, I will of course watch them.

##### Reading Flask
I made a website with Flask once! for a project. I should make a list of everything I have learned and put it on github. Hecking, Flask, cisco course, portswigger, natas, powershell, python, APK RE...
#TODO
Anyways...
```
hacker@talking-web~reading-flask:~$ cat /challenge/server 
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


@app.route("/check", methods=["GET"])
def challenge():
    if "Firefox" not in flask.request.headers.get("User-Agent"):
        flask.abort(400, "You are using an incorrect client to access this resource!")

    return f"""
        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p>{open("/flag").read().strip()}</p>
        </body>
        </html>
    """


app.secret_key = os.urandom(8)
app.run("challenge.localhost", 80)
```
So the user agent should be Firefox. This is easily duped. lets try?

```
curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0" http://challenge.localhost:80/check

```
```
hacker@talking-web~reading-flask:~$ curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0" http://challenge.localhost:80/check

        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p>~flag~</p>
        </body>
        </html>
```
I like to censor the flag. It worked.

##### Commented Data
Basically use web tools.
And read the /challenge/server file to see that I need to access the /fulfill directory.

##### HTTP Metadata
Its in the request.
Network - View the GET request

##### HTTP (netcat)
```
hacker@talking-web~http-netcat:~$ printf "GET / HTTP/1.1\r\nHost: challenge.localhost\r\nConnection: close\r\n\r\n" | nc challenge.localhost 80
HTTP/1.1 200 OK
Server: Werkzeug/3.0.6 Python/3.8.10
Date: Sat, 19 Sep 2026 13:28:47 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 84
X-Flag: 
Connection: close
```

##### HTTP Paths
```
hacker@talking-web~http-paths-netcat:~$ printf "GET /gateway HTTP/1.1\r\nHost: challenge.localhost\r\nConnection: close\r\n\r\n" | nc challenge.localhost 80
HTTP/1.1 200 OK
Server: Werkzeug/3.0.6 Python/3.8.10
Date: Sat, 19 Sep 2026 13:33:08 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 245
Connection: close


        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <!-- TOP SECRET: <p></p> -->
        </body>
        </html>

```
Remember to turn on the server!

##### HTTP (curl)
```
curl -i challenge.localhost/mission
HTTP/1.1 200 OK
Server: Werkzeug/3.0.6 Python/3.8.10
Date: Sat, 19 Sep 2026 13:39:57 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 224
Connection: close


        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p></p>
        </body>
        </html>

```

##### HTTP (python)
```
import requests

import json

  

response = requests.get('http://challenge.localhost:80/gate')

print("--- RESPONSE HEADERS ---")

print(json.dumps(dict(response.headers), indent=4))

  

print("\n--- RESPONSE BODY ---")

print(response.text)
```

```
hacker@talking-web~http-python:~$ /run/dojo/bin/python "/home/hacker/Talking_Web/HTTP_(python).py"
--- RESPONSE HEADERS ---
{
    "Server": "Werkzeug/3.0.6 Python/3.8.10",
    "Date": "Sat, 19 Sep 2026 13:47:51 GMT",
    "Content-Type": "text/html; charset=utf-8",
    "Content-Length": "224",
    "Connection": "close"
}

--- RESPONSE BODY ---

        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p></p>
        </body>
        </html>
    
```

##### HTTP Host Header (python)
```
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


@app.route("/qualify", methods=["GET"])
def challenge():
    if name_of_program_for(peer_process_of(flask.request.input_stream.fileno())) not in ["python3"]:
        flask.abort(400, "You are using an incorrect client to access this resource!")

    return f"""
        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p>{open("/flag").read().strip()}</p>
        </body>
        </html>
    """


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "cryptohack.org:80"
app.run("challenge.localhost", 80)
```
```
import requests

import json

  

url = "http://challenge.localhost:80/qualify"

custom_headers = {

    "Host": "cryptohack.org:80"

}

  

response = requests.get(url, headers=custom_headers)

print("--- RESPONSE HEADERS ---")

print(json.dumps(dict(response.headers), indent=4))

  

print("\n--- RESPONSE BODY ---")

print(response.text)
```

##### HTTP Host Header (curl)
```
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


@app.route("/task", methods=["GET"])
def challenge():
    if name_of_program_for(peer_process_of(flask.request.input_stream.fileno())) not in ["curl"]:
        flask.abort(400, "You are using an incorrect client to access this resource!")

    return f"""
        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p>{open("/flag").read().strip()}</p>
        </body>
        </html>
    """


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "net-force.nl:80"
app.run("challenge.localhost", 80)


```
```
curl -H "Host: "net-force.nl:80"" http://challenge.localhost:80/task

```

##### HTTP Host Header (netcat)
```
hacker@talking-web~http-host-header-netcat:~$ cat /challenge/server 
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


@app.route("/fulfill", methods=["GET"])
def challenge():
    if name_of_program_for(peer_process_of(flask.request.input_stream.fileno())) not in ["nc"]:
        flask.abort(400, "You are using an incorrect client to access this resource!")

    response = flask.make_response(
        "<html><head><title>Talking Web</title></head><body><h1>Great job!</h1></body></html>"
    )
    response.headers["X-Flag"] = open("/flag").read().strip()
    return response


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "www.thisislegal.com:80"
app.run("challenge.localhost", 80)
```

```
printf "GET /fulfill HTTP/1.1\r\nHost: www.thisislegal.com:80\r\nConnection: close\r\n\r\n" | nc challenge.localhost 80

```

##### URL Encoding (netcat)
```
hacker@talking-web~url-encoding-netcat:~$ cat /challenge/server 
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


@app.route("/mission progress fulfill", methods=["GET"])
def challenge():
    if name_of_program_for(peer_process_of(flask.request.input_stream.fileno())) not in ["nc"]:
        flask.abort(400, "You are using an incorrect client to access this resource!")

    response = flask.make_response(
        "<html><head><title>Talking Web</title></head><body><h1>Great job!</h1></body></html>"
    )
    response.headers["X-Flag"] = open("/flag").read().strip()
    return response


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```

```
printf "GET /mission%%20progress%%20fulfill HTTP/1.1\r\nHost: challenge.localhost\r\nConnection: close\r\n\r\n" | nc challenge.localhost 80

```

##### HTTP GET Parameters
```
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


@app.route("/complete", methods=["GET"])
def challenge():
    if flask.request.args.get("auth_token", None) != "woiaadpt":
        flask.abort(403, "Incorrect value for get parameter auth_token!")

    return f"""
        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p>{open("/flag").read().strip()}</p>
        </body>
        </html>
    """


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```

```
curl -G -d "auth_token=woiaadpt" http://challenge.localhost:80/complete
```

##### Multiple HTTP Parameters (netcat)
```
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


@app.route("/check", methods=["GET"])
def challenge():
    if name_of_program_for(peer_process_of(flask.request.input_stream.fileno())) not in ["nc"]:
        flask.abort(400, "You are using an incorrect client to access this resource!")

    if flask.request.args.get("pass", None) != "clsazklj":
        flask.abort(403, "Incorrect value for get parameter pass!")

    if flask.request.args.get("keycode", None) != "zmxqebuu":
        flask.abort(403, "Incorrect value for get parameter keycode!")

    if flask.request.args.get("auth_pass", None) != "vbxefpvy":
        flask.abort(403, "Incorrect value for get parameter auth_pass!")

    return f"""
        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p>{open("/flag").read().strip()}</p>
        </body>
        </html>
    """


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```

Should be something like:
```
printf "GET /check?pass=clsazklj&keycode=zmxqebuu&auth_pass=vbxefpvy HTTP/1.1\r\nHost: challenge.localhost\r\nConnection: close\r\n\r\n" | nc challenge.localhost 80
```

##### Multiple HTTP Parameters (curl)
```
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


@app.route("/evaluate", methods=["GET"])
def challenge():
    if name_of_program_for(peer_process_of(flask.request.input_stream.fileno())) not in ["curl"]:
        flask.abort(400, "You are using an incorrect client to access this resource!")

    if flask.request.args.get("verify", None) != "kxqhhioe":
        flask.abort(403, "Incorrect value for get parameter verify!")

    if flask.request.args.get("auth_pass", None) != "azymkygt":
        flask.abort(403, "Incorrect value for get parameter auth_pass!")

    if flask.request.args.get("secret", None) != "bqgqpqox":
        flask.abort(403, "Incorrect value for get parameter secret!")

    return f"""
        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p>{open("/flag").read().strip()}</p>
        </body>
        </html>
    """


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```

```
curl -G -d "verify=kxqhhioe" -d "auth_pass=azymkygt" -d "secret=bqgqpqox" http://challenge.localhost:80/evaluate
```

##### HTTP Forms
I guess I need to submit a form in the browser lol
I need to submit the password in the server files.

##### HTTP Forms (curl)
```
^Chacker@talking-web~http-forms-curl:~$ cat /challenge/server 
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


@app.route("/attempt", methods=["POST"])
def challenge():
    if name_of_program_for(peer_process_of(flask.request.input_stream.fileno())) not in ["curl"]:
        flask.abort(400, "You are using an incorrect client to access this resource!")

    if flask.request.form.get("pin", None) != "eyhyucgx":
        flask.abort(403, "Incorrect value for post parameter pin!")

    return f"""
        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p>{open("/flag").read().strip()}</p>
        </body>
        </html>
    """


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```

```
curl -X POST -d "pin=eyhyucgx" http://challenge.localhost:80/attempt
```
##### HTTP Forms (netcat)
```
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


@app.route("/task", methods=["POST"])
def challenge():
    if name_of_program_for(peer_process_of(flask.request.input_stream.fileno())) not in ["nc"]:
        flask.abort(400, "You are using an incorrect client to access this resource!")

    if flask.request.form.get("secret", None) != "qodvhyrg":
        flask.abort(403, "Incorrect value for post parameter secret!")

    return f"""
        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p>{open("/flag").read().strip()}</p>
        </body>
        </html>
    """


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```

```
printf "POST /task HTTP/1.1\r\nHost: challenge.localhost\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 15\r\nConnection: close\r\n\r\nsecret=qodvhyrg" | nc challenge.localhost 80

```
You gotta have the content length!

##### HTTP Forms (python)
```
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


@app.route("/hack", methods=["POST"])
def challenge():
    if name_of_program_for(peer_process_of(flask.request.input_stream.fileno())) not in ["python3"]:
        flask.abort(400, "You are using an incorrect client to access this resource!")

    if flask.request.form.get("security_token", None) != "rsnqgrbx":
        flask.abort(403, "Incorrect value for post parameter security_token!")

    return f"""
        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p>{open("/flag").read().strip()}</p>
        </body>
        </html>
    """


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```

```
import requests

  

url = "http://challenge.localhost:80/hack"

data_pram = {"security_token": "rsnqgrbx"}

  

# Parameters appear in the URL query string

response = requests.post(url, data=data_pram)

  

print(response.status_code)

print(response.text)
```

##### HTTP Forms Without Forms
```
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


@app.route("/progress", methods=["POST"])
def challenge():
    if "Firefox" not in flask.request.headers.get("User-Agent"):
        flask.abort(400, "You are using an incorrect client to access this resource!")

    if flask.request.form.get("hash", None) != "mnkeibsl":
        flask.abort(403, "Incorrect value for post parameter hash!")

    return f"""
        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p>{open("/flag").read().strip()}</p>
        </body>
        </html>
    """


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```

```
curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0" -X POST -d "hash=mnkeibsl" http://challenge.localhost:80/progress
```

##### Multiple Form Fields (curl)
```
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


@app.route("/authenticate", methods=["POST"])
def challenge():
    if name_of_program_for(peer_process_of(flask.request.input_stream.fileno())) not in ["curl"]:
        flask.abort(400, "You are using an incorrect client to access this resource!")

    if flask.request.form.get("auth_token", None) != "vfjgdfql":
        flask.abort(403, "Incorrect value for post parameter auth_token!")

    if flask.request.form.get("pin", None) != "tubmwweq":
        flask.abort(403, "Incorrect value for post parameter pin!")

    if flask.request.form.get("access", None) != "uzzspyys":
        flask.abort(403, "Incorrect value for post parameter access!")

    return f"""
        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p>{open("/flag").read().strip()}</p>
        </body>
        </html>
    """


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```

```
curl -X POST -d "auth_token=vfjgdfql" -d "pin=tubmwweq" -d "access=uzzspyys"  http://challenge.localhost:80/authenticate
```

##### Multiple Form Fields (netcat)
```
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


@app.route("/pwn", methods=["POST"])
def challenge():
    if name_of_program_for(peer_process_of(flask.request.input_stream.fileno())) not in ["nc"]:
        flask.abort(400, "You are using an incorrect client to access this resource!")

    if flask.request.form.get("secret_key", None) != "vyajvbop":
        flask.abort(403, "Incorrect value for post parameter secret_key!")

    if flask.request.form.get("challenge_key", None) != "cdmmpexq":
        flask.abort(403, "Incorrect value for post parameter challenge_key!")

    if flask.request.form.get("hash", None) != "xnezbbbc":
        flask.abort(403, "Incorrect value for post parameter hash!")

    if flask.request.form.get("credential", None) != "qmrjdtgq":
        flask.abort(403, "Incorrect value for post parameter credential!")

    return f"""
        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p>{open("/flag").read().strip()}</p>
        </body>
        </html>
    """


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```

```
printf "POST /pwn HTTP/1.1\r\nHost: challenge.localhost\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 76\r\nConnection: close\r\n\r\nsecret_key=vyajvbop&challenge_key=cdmmpexq&hash=xnezbbbc&credential=qmrjdtgq" | nc -N challenge.localhost 80
```
So far very basic stuff.

##### HTTP Redirects (netcat)
```
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


import random
import string

secret_endpoint = "".join(random.sample(string.ascii_letters, 8))


@app.route("/", methods=["GET"])
def challenge_redirector():
    if name_of_program_for(peer_process_of(flask.request.input_stream.fileno())) not in ["nc"]:
        flask.abort(400, "You are using an incorrect client to access this resource!")

    return flask.redirect(f"/{secret_endpoint}-evaluate")


@app.route(f"/{secret_endpoint}-evaluate", methods=["GET"])
def challenge():
    if name_of_program_for(peer_process_of(flask.request.input_stream.fileno())) not in ["nc"]:
        flask.abort(400, "You are using an incorrect client to access this resource!")

    return f"""
        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p>{open("/flag").read().strip()}</p>
        </body>
        </html>
    """


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```
Lets do a GET request, and the website should give us the new address.
```
printf "GET / HTTP/1.1\r\nHost: challenge.localhost\r\nConnection: close\r\n\r\n" | nc challenge.localhost 80

```

```
printf "GET / HTTP/1.1\r\nHost: challenge.localhost\r\nConnection: close\r\n\r\n" | nc challenge.localhost 80
HTTP/1.1 302 FOUND
Server: Werkzeug/3.0.6 Python/3.8.10
Date: Tue, 22 Sep 2026 00:40:53 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 223
Location: /dNKBwUkX-evaluate
Connection: close

<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/dNKBwUkX-evaluate">/dNKBwUkX-evaluate</a>. If not, click the link.
```
OK!
```
printf "GET dNKBwUkX-evaluate HTTP/1.1\r\nHost: challenge.localhost\r\nConnection: close\r\n\r\n" | nc challenge.localhost 80
```
YES!

##### HTTP Redirects (curl)
```
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


import random
import string

secret_endpoint = "".join(random.sample(string.ascii_letters, 8))


@app.route("/", methods=["GET"])
def challenge_redirector():
    if name_of_program_for(peer_process_of(flask.request.input_stream.fileno())) not in ["curl"]:
        flask.abort(400, "You are using an incorrect client to access this resource!")

    return flask.redirect(f"/{secret_endpoint}-evaluate")


@app.route(f"/{secret_endpoint}-evaluate", methods=["GET"])
def challenge():
    if name_of_program_for(peer_process_of(flask.request.input_stream.fileno())) not in ["curl"]:
        flask.abort(400, "You are using an incorrect client to access this resource!")

    return f"""
        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p>{open("/flag").read().strip()}</p>
        </body>
        </html>
    """


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```

```
curl -X GET -L http://challenge.localhost:80/
```
Easy as that.

##### HTTP Redirects (python)
It should be autumatic
```
import requests

import json

  

response = requests.get('http://challenge.localhost:80')

print("--- RESPONSE HEADERS ---")

print(json.dumps(dict(response.headers), indent=4))

  

print("\n--- RESPONSE BODY ---")

print(response.text)
```

##### HTTP Cookies (curl)
```
hacker@talking-web~http-cookies-curl:~$ /challenge/run 
Make an HTTP request to 127.0.0.1 on port 80 to get the flag. Make any HTTP request, and the server will ask you to set a cookie. Make another request with that cookie to get the flag.
You must make this request using the curl command

The following output is from the server, might be useful in helping you debug:
------------------------------------------------
 * Serving Flask app 'run'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:80
```
```
hacker@talking-web~http-cookies-curl:~$ curl -X GET -i http://127.0.0.1:80/
HTTP/1.1 302 FOUND
Server: Werkzeug/3.0.6 Python/3.8.10
Date: Tue, 22 Sep 2026 01:02:32 GMT
Content-Length: 189
Location: /
Set-Cookie: cookie=a496b3e76a6d32ce2b7bcea4138cdc46; Path=/
Server: pwn.college
Connection: close

<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/">/</a>. If not, click the link.
```

```
curl -X POST -b "cookie=a496b3e76a6d32ce2b7bcea4138cdc46" http://127.0.0.1:80/
```

##### HTTP Cookies (netcat)
```
hacker@talking-web~http-cookies-netcat:~$ printf "GET / HTTP/1.1\r\nHost: challenge.localhost\r\nConnection: close\r\n\r\n" | nc challenge.localhost 80
HTTP/1.1 302 FOUND
Server: Werkzeug/3.0.6 Python/3.8.10
Date: Wed, 23 Sep 2026 13:36:21 GMT
Content-Length: 189
Location: /
Set-Cookie: cookie=1211a69107c35114684aea54d4ddce10; Path=/
Server: pwn.college
Connection: close

<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/">/</a>. If not, click the link.
```

```
printf "POST / HTTP/1.1\r\nHost: challenge.localhost\r\nConnection: close\r\nCookie: cookie=1211a69107c35114684aea54d4ddce10\r\n\r\n" | nc challenge.localhost 80

```

```
hacker@talking-web~http-cookies-netcat:~$ printf "POST / HTTP/1.1\r\nHost: challenge.localhost\r\nConnection: close\r\nCookie: cookie=1211a69107c35114684aea54d4ddce10\r\n\r\n" | nc challenge.localhost 80
HTTP/1.1 200 OK
Server: Werkzeug/3.0.6 Python/3.8.10
Date: Wed, 23 Sep 2026 13:38:58 GMT
Content-Length: 60
Server: pwn.college
Connection: close
```

##### HTTP Cookies (python)
```
import requests

  
  

with requests.Session() as session:

  

    response = session.get("http://challenge.localhost:80/")

    print(response.text)
```
it updates automatically
##### Server State (python)
```
import requests

  
  

with requests.Session() as session:

  

    response = session.get("http://challenge.localhost:80/")

    print(response.text)
```

##### Listening Web
**You've been staring at web server code all this time and figuring out how to speak to it. Now, let's learn to _listen_.**

**In this level, you will write a simple server that'll receive the request for the flag! Simply copy the server code from, say, the very first module, remove anything extra, and build a web server that'll listen on port 1337 (instead of 80 --- you can't listen on port 80 as a non-administrative user) and on hostname `localhost`. When you're ready, run `/challenge/client`, and it will launch an internal web browser and visit `http://localhost:1337/` with the flag!**

ok.

```
import flask

  

app = flask.Flask(__name__)

  

@app.route("/", methods=["GET"])

def challenge():

    try:

        with open("/flag", "r") as flag_file:

            flag = flag_file.read().strip()

  

        return f"""

        <html>

          <head><title>Talking Web</title></head>

          <body>

            <h1>Great job!</h1>

            <p>{flag}</p>

          </body>

        </html>

        """

    except Exception as error:

        return f"Error: {type(error).__name__}: {error}\n", 500

  

app.run(host="challenge.localhost", port=1337)
```

```
/challenge/client
```

##### Speaking Redirects
I am very tired. its 9:00 and I did not sleep. Not because of studying, ofc.

Lets see what is the right address to redirect to.
```
hacker@talking-web~speaking-redirects:~$ cat /challenge/server 
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


@app.route("/verify", methods=["GET"])
def challenge():
    if peer_process_of(flask.request.input_stream.fileno()).username() != "root":
        flask.abort(
            400,
            f"""
              This page must be accessed using a browser run by the root user.
              Usually, this means you would run the scripted browser in /challenge/client or /challenge/victim,
              and it'll access this page for you.
              Of course, this sort of functionality doesn't exist on the actual web, as google.com can't access
              your user ID on your local machine, but we use this hack here for teaching purposes.
        """,
        )

    return f"""
        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p>{open("/flag").read().strip()}</p>
        </body>
        </html>
    """


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```
/verify

```
import flask

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])

def challenge():

    try:

        with open("/flag", "r") as flag_file:

            flag = flag_file.read().strip()

        return f"""

        <html>

          <head><title>Talking Web</title></head>

          <body>

            <h1>Great job!</h1>

            <p>{flag}</p>

          </body>

        </html>

        """

    except Exception as error:

        return f"Error: {type(error).__name__}: {error}\n", 500

app.run(host="challenge.localhost", port=1337)
```

```
/challenge/server
/challenge/client
```
Just redirect.

##### JavaScript Redirect
Server:
```
hacker@talking-web~javascript-redirects:~$ cat /challenge/server 
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


@app.route("/~hacker/<path:path>", methods=["GET"])
def public_html(path="index.html"):
    try:
        ruid, euid, suid = os.getresuid()
        os.seteuid(ruid)
        return flask.send_from_directory("/home/hacker/public_html", path)
    except PermissionError:
        flask.abort(403)
    finally:
        os.seteuid(euid)


@app.route("/submission", methods=["GET"])
def challenge():
    if peer_process_of(flask.request.input_stream.fileno()).username() != "root":
        flask.abort(
            400,
            f"""
              This page must be accessed using a browser run by the root user.
              Usually, this means you would run the scripted browser in /challenge/client or /challenge/victim,
              and it'll access this page for you.
              Of course, this sort of functionality doesn't exist on the actual web, as google.com can't access
              your user ID on your local machine, but we use this hack here for teaching purposes.
        """,
        )

    return f"""
        <html>
          <head><title>Talking Web</title></head>
        <body>
          <h1>Great job!</h1>
          <p>{open("/flag").read().strip()}</p>
        </body>
        </html>
    """


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```

Client:
```
hacker@talking-web~javascript-redirects:~$ cat /challenge/client 
#!/opt/pwn.college/python

import shutil
import psutil
import urllib
import atexit
import time
import sys
import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

os.setuid(os.geteuid())
os.environ.clear()
os.environ["PATH"] = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

options = FirefoxOptions()
options.add_argument("--headless")
service = FirefoxService(log_path="/dev/null", executable_path=shutil.which("geckodriver"))
browser = webdriver.Firefox(service=service, options=options)
atexit.register(browser.quit)

open_ports = {s.laddr.port for s in psutil.net_connections(kind="inet") if s.status == "LISTEN"}
if 80 not in open_ports:
    print("Service doesn't seem to be running?")
    sys.exit(1)

challenge_url = "http://challenge.localhost:80/~hacker/solve.html"

print(f"Visiting {challenge_url}")
browser.get(challenge_url)


print("Retrieved the following HTML:")
if "<html" not in browser.page_source.lower():
    print("Doesn't look like we retrieved an HTML page...")
    sys.exit(1)
print(browser.page_source)

time.sleep(2)
print(" ")
```
solve.html
```
<html>

    <p><script>

        window.location.href = "/submission";

    </script></p>

</html>
```

##### Including JavaScript
Server:
```
hacker@talking-web~including-javascript:~$ cat /challenge/server 
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


@app.route("/~hacker/<path:path>", methods=["GET"])
def public_html(path="index.html"):
    try:
        ruid, euid, suid = os.getresuid()
        os.seteuid(ruid)
        return flask.send_from_directory("/home/hacker/public_html", path)
    except PermissionError:
        flask.abort(403)
    finally:
        os.seteuid(euid)


@app.route("/meet", methods=["GET"])
def challenge():
    if peer_process_of(flask.request.input_stream.fileno()).username() != "root":
        flask.abort(
            400,
            f"""
              This page must be accessed using a browser run by the root user.
              Usually, this means you would run the scripted browser in /challenge/client or /challenge/victim,
              and it'll access this page for you.
              Of course, this sort of functionality doesn't exist on the actual web, as google.com can't access
              your user ID on your local machine, but we use this hack here for teaching purposes.
        """,
        )

    response = flask.Response(f"""var flag = "{open("/flag").read().strip()}";""", content_type="text/javascript")
    return response


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```

Client:
```
hacker@talking-web~including-javascript:~$ cat /challenge/client 
#!/opt/pwn.college/python

import shutil
import psutil
import urllib
import atexit
import time
import sys
import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

os.setuid(os.geteuid())
os.environ.clear()
os.environ["PATH"] = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

options = FirefoxOptions()
options.add_argument("--headless")
service = FirefoxService(log_path="/dev/null", executable_path=shutil.which("geckodriver"))
browser = webdriver.Firefox(service=service, options=options)
atexit.register(browser.quit)

open_ports = {s.laddr.port for s in psutil.net_connections(kind="inet") if s.status == "LISTEN"}
if 80 not in open_ports:
    print("Service doesn't seem to be running?")
    sys.exit(1)

challenge_url = "http://challenge.localhost:80/~hacker/solve.html"

print(f"Visiting {challenge_url}")
browser.get(challenge_url)


time.sleep(2)
print(" ")
```
solve.html:
```
<html>

    <script src="/meet"></script>

    <p><script>

        window.location = "http://127.0.0.1:80/?flag=" + encodeURIComponent(flag);

    </script></p>

</html>
```

##### HTTP (javascript)
This is getting hard. Hard to understand.
Server:
```
hacker@talking-web~http-javascript:~$ cat /challenge/server 
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


@app.route("/~hacker/<path:path>", methods=["GET"])
def public_html(path="index.html"):
    try:
        ruid, euid, suid = os.getresuid()
        os.seteuid(ruid)
        return flask.send_from_directory("/home/hacker/public_html", path)
    except PermissionError:
        flask.abort(403)
    finally:
        os.seteuid(euid)


@app.route("/complete", methods=["GET"])
def challenge():
    if peer_process_of(flask.request.input_stream.fileno()).username() != "root":
        flask.abort(
            400,
            f"""
              This page must be accessed using a browser run by the root user.
              Usually, this means you would run the scripted browser in /challenge/client or /challenge/victim,
              and it'll access this page for you.
              Of course, this sort of functionality doesn't exist on the actual web, as google.com can't access
              your user ID on your local machine, but we use this hack here for teaching purposes.
        """,
        )

    response = flask.Response(open("/flag").read().strip(), content_type="text/plain")
    return response


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```

Client:
```
cat /challenge/client 
#!/opt/pwn.college/python

import shutil
import psutil
import urllib
import atexit
import time
import sys
import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

os.setuid(os.geteuid())
os.environ.clear()
os.environ["PATH"] = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

options = FirefoxOptions()
options.add_argument("--headless")
service = FirefoxService(log_path="/dev/null", executable_path=shutil.which("geckodriver"))
browser = webdriver.Firefox(service=service, options=options)
atexit.register(browser.quit)

open_ports = {s.laddr.port for s in psutil.net_connections(kind="inet") if s.status == "LISTEN"}
if 80 not in open_ports:
    print("Service doesn't seem to be running?")
    sys.exit(1)

challenge_url = "http://challenge.localhost:80/~hacker/solve.html"

print(f"Visiting {challenge_url}")
browser.get(challenge_url)


time.sleep(2)
print(" ")
hacker@talk
```

SOLVE.HTML!!!! I GOT IT YES!
```
<html>

<head>

    <script>

        fetch("/complete")

          .then(response => response.text())

          .then(path => {

              window.location.href = path;

          })

          .catch(error => console.error("Error:", error));

    </script>

</head>

<body>

    <p>Redirecting...</p>

</body>

</html>
```
Flag is in the server log.

##### HTTP GET Parameters (javascript)
Server:
```
hacker@talking-web~http-get-parameters-javascript:~$ cat /challenge/server 
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


@app.route("/~hacker/<path:path>", methods=["GET"])
def public_html(path="index.html"):
    try:
        ruid, euid, suid = os.getresuid()
        os.seteuid(ruid)
        return flask.send_from_directory("/home/hacker/public_html", path)
    except PermissionError:
        flask.abort(403)
    finally:
        os.seteuid(euid)


@app.route("/authenticate", methods=["GET"])
def challenge():
    if peer_process_of(flask.request.input_stream.fileno()).username() != "root":
        flask.abort(
            400,
            f"""
              This page must be accessed using a browser run by the root user.
              Usually, this means you would run the scripted browser in /challenge/client or /challenge/victim,
              and it'll access this page for you.
              Of course, this sort of functionality doesn't exist on the actual web, as google.com can't access
              your user ID on your local machine, but we use this hack here for teaching purposes.
        """,
        )

    if flask.request.args.get("auth", None) != "zgpgzbsh":
        flask.abort(403, "Incorrect value for get parameter auth!")

    if flask.request.args.get("auth_token", None) != "frmnnodt":
        flask.abort(403, "Incorrect value for get parameter auth_token!")

    if flask.request.args.get("pass", None) != "paizyrnq":
        flask.abort(403, "Incorrect value for get parameter pass!")

    response = flask.Response(open("/flag").read().strip(), content_type="text/plain")
    return response


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```

Client
```
hacker@talking-web~http-get-parameters-javascript:~$ cat /challenge/client 
#!/opt/pwn.college/python

import shutil
import psutil
import urllib
import atexit
import time
import sys
import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

os.setuid(os.geteuid())
os.environ.clear()
os.environ["PATH"] = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

options = FirefoxOptions()
options.add_argument("--headless")
service = FirefoxService(log_path="/dev/null", executable_path=shutil.which("geckodriver"))
browser = webdriver.Firefox(service=service, options=options)
atexit.register(browser.quit)

open_ports = {s.laddr.port for s in psutil.net_connections(kind="inet") if s.status == "LISTEN"}
if 80 not in open_ports:
    print("Service doesn't seem to be running?")
    sys.exit(1)

challenge_url = "http://challenge.localhost:80/~hacker/solve.html"

print(f"Visiting {challenge_url}")
browser.get(challenge_url)


time.sleep(2)
print(" ")
```
Client is just visiting the html.
Sever is requiring 3 parameters to enter /authenticate and get the flag with fetch()
Looking at examples online:

solve.html
```
<html>
<head>
    <script>
        const auth = "zgpgzbsh";
        const auth_token = "frmnnodt";
        const pass = "paizyrnq";

        fetch("/submission")
          .then(response => response.text())
          .then(path => {
              // שרשור הפרמטרים לנתיב שהתקבל מהשרת
              // אם path הוא "/dashboard", הכתובת תהיה "/dashboard?user=123&status=success"
              window.location.href = `${path}?user=${userId}&status=${status}`; 
          })
          .catch(error => console.error("Error:", error));
    </script>
</head>
<body>
    <p>Redirecting...</p>
</body>
</html>

```

solve.html
```
<html>

<head>

    <script>

        const auth = "zgpgzbsh";

        const auth_token = "frmnnodt";

        const pass = "paizyrnq";

        fetch(`/authenticate?auth=${auth}&auth_token=${auth_token}&pass=${pass}`)

          .then(response => response.text())

          .then(path => {

              window.location.href = path;

          })

          .catch(error => console.error("Error:", error));

    </script>

</head>

<body>

    <p>Redirecting...</p>

</body>

</html>
```

##### HTTP Forms (javascript)
Server:
```
hacker@talking-web~http-forms-javascript:~$ cat /challenge/server 
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


import pathlib
import psutil


# This function determines the process that is on the
# other side of the file descriptor we pass in.
def peer_process_of(fd):
    server_connection = next(connection for connection in psutil.Process().net_connections() if connection.fd == fd)
    client_connection = next(
        connection
        for connection in psutil.net_connections()
        if connection.raddr == server_connection.laddr and connection.laddr == server_connection.raddr
    )
    return psutil.Process(client_connection.pid)


# This function returns the filename of a peer process for a given
# file descriptor, verifying that the path is owned by root and
# not open to shenanigans.
def name_of_program_for(process):
    client_path = pathlib.Path(process.exe())
    for p in reversed(client_path.parents):
        if p.owner() != "root":
            return None
        if str(p) in ("/home", "/tmp", "/var/tmp", "/dev/shm"):
            return None
    return client_path.stem


@app.route("/~hacker/<path:path>", methods=["GET"])
def public_html(path="index.html"):
    try:
        ruid, euid, suid = os.getresuid()
        os.seteuid(ruid)
        return flask.send_from_directory("/home/hacker/public_html", path)
    except PermissionError:
        flask.abort(403)
    finally:
        os.seteuid(euid)


@app.route("/qualify", methods=["POST"])
def challenge():
    if peer_process_of(flask.request.input_stream.fileno()).username() != "root":
        flask.abort(
            400,
            f"""
              This page must be accessed using a browser run by the root user.
              Usually, this means you would run the scripted browser in /challenge/client or /challenge/victim,
              and it'll access this page for you.
              Of course, this sort of functionality doesn't exist on the actual web, as google.com can't access
              your user ID on your local machine, but we use this hack here for teaching purposes.
        """,
        )

    if flask.request.form.get("secure_key", None) != "hjjdciil":
        flask.abort(403, "Incorrect value for post parameter secure_key!")

    if flask.request.form.get("unlock_code", None) != "aytpcgqm":
        flask.abort(403, "Incorrect value for post parameter unlock_code!")

    if flask.request.form.get("hash", None) != "zaomqlkp":
        flask.abort(403, "Incorrect value for post parameter hash!")

    response = flask.Response(open("/flag").read().strip(), content_type="text/plain")
    return response


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = "challenge.localhost:80"
app.run("challenge.localhost", 80)
```

Client:
```
hacker@talking-web~http-forms-javascript:~$ cat /challenge/client 
#!/opt/pwn.college/python

import shutil
import psutil
import urllib
import atexit
import time
import sys
import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

os.setuid(os.geteuid())
os.environ.clear()
os.environ["PATH"] = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

options = FirefoxOptions()
options.add_argument("--headless")
service = FirefoxService(log_path="/dev/null", executable_path=shutil.which("geckodriver"))
browser = webdriver.Firefox(service=service, options=options)
atexit.register(browser.quit)

open_ports = {s.laddr.port for s in psutil.net_connections(kind="inet") if s.status == "LISTEN"}
if 80 not in open_ports:
    print("Service doesn't seem to be running?")
    sys.exit(1)

challenge_url = "http://challenge.localhost:80/~hacker/solve.html"

print(f"Visiting {challenge_url}")
browser.get(challenge_url)


time.sleep(2)
print(" ")
```

solve.html
```
<html>

<head>

    <script>

        const formData = new URLSearchParams();

        formData.append("secure_key", "hjjdciil");

        formData.append("unlock_code", "aytpcgqm");

        formData.append("hash", "zaomqlkp");

  

        fetch("/qualify", {

        method: "POST",

        headers: {

        "Content-Type": "application/x-www-form-urlencoded"

        },

        body: formData.toString()

        })

            .then(response => response.text())

            .then(path => {

                window.location.href = path;

            })

            .catch(error => {

                console.error("Error:", error);

            });

    </script>

</head>

<body>

    <p>Redirecting...</p>

</body>

</html>
```

My first solution did not work because I did not encode it as url.

FINISHED TALKING WEB!
