lesgo

Creating a table:
```
CREATE TABLE users (username, password)
```

Inserting data:
```
INSERT INTO users VALUES ("admin", "admin123")
```

Query:
```
SELECT username, password FROM users 
```

Selects everything:
```
SELECT * FROM users 
```

Specific Selection:
```
SELECT * FROM users WHERE username = "admin"
```

Delete:
```
DELETE FROM users WHERE username = "admin"
```

Update:
```
UPDATE users SET password = "admin456" WHERE username = "admin"
```

Union select:
```
SELECT username FROM users UNION SELECT passowrd FROM users
```

The Schema Table (sqlite)
```
SELECT tbl_name FROM sqlite_masetr
```

Drop table:
```
DROP TABLE users
```
BYE users

##### SQL Queries
```
hacker@sql-playground~sql-queries:~$ cat /challenge/sql 
#!/opt/pwn.college/python

import sys
import string
import random
import sqlite3
import tempfile


# Don't panic about the TemporaryDB class. It simply implements a temporary database
# in which this application can store data. You don't need to understand its internals,
# just that it processes SQL queries using db.execute().
class TemporaryDB:
    def __init__(self):
        self.db_file = tempfile.NamedTemporaryFile("x", suffix=".db")

    def execute(self, sql, parameters=()):
        connection = sqlite3.connect(self.db_file.name)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        result = cursor.execute(sql, parameters)
        connection.commit()
        return result


db = TemporaryDB()

# https://www.sqlite.org/lang_createtable.html
db.execute("""CREATE TABLE logs AS SELECT ? as entry""", [open("/flag").read().strip()])

# HINT: https://www.sqlite.org/lang_select.html
for _ in range(1):
    query = input("sql> ")

    try:
        results = db.execute(query).fetchall()
    except sqlite3.Error as e:
        print("SQL ERROR:", e)
        sys.exit(1)

    if len(results) == 0:
        print("No results returned!")
        sys.exit(0)

    print(f"Got {len(results)} rows.")
    for row in results:
        print(f"- { { k:row[k] for k in row.keys() } }")
hacker@sql-playground~sql-queries:~$
```

```
hacker@sql-playground~sql-queries:~$ /challenge/sql 
sql> SELECT * FROM logs
```

##### Filtering SQL
```
hacker@sql-playground~filtering-sql:~$ cat /challenge/sql 
#!/opt/pwn.college/python

import sys
import string
import random
import sqlite3
import tempfile


# Don't panic about the TemporaryDB class. It simply implements a temporary database
# in which this application can store data. You don't need to understand its internals,
# just that it processes SQL queries using db.execute().
class TemporaryDB:
    def __init__(self):
        self.db_file = tempfile.NamedTemporaryFile("x", suffix=".db")

    def execute(self, sql, parameters=()):
        connection = sqlite3.connect(self.db_file.name)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        result = cursor.execute(sql, parameters)
        connection.commit()
        return result


db = TemporaryDB()


def random_word(length):
    return "".join(random.sample(string.ascii_letters * 10, length))


flag = open("/flag").read().strip()

# https://www.sqlite.org/lang_createtable.html
db.execute("""CREATE TABLE repository AS SELECT 1 as flag_tag, ? as info""", [random_word(len(flag))])
# https://www.sqlite.org/lang_insert.html
for i in range(random.randrange(5, 42)):
    db.execute("""INSERT INTO repository VALUES(1, ?)""", [random_word(len(flag))])
db.execute("""INSERT INTO repository VALUES(?, ?)""", [1337, flag])


for i in range(random.randrange(5, 42)):
    db.execute("""INSERT INTO repository VALUES(1, ?)""", [random_word(len(flag))])

# HINT: https://www.sqlite.org/lang_select.html#whereclause
for _ in range(1):
    query = input("sql> ")

    try:
        results = db.execute(query).fetchall()
    except sqlite3.Error as e:
        print("SQL ERROR:", e)
        sys.exit(1)

    if len(results) == 0:
        print("No results returned!")
        sys.exit(0)

    if len(results) > 1:
        print("You're not allowed to read this many rows!")
        sys.exit(1)
    print(f"Got {len(results)} rows.")
    for row in results:
        print(f"- { { k:row[k] for k in row.keys() } }")
```

```
hacker@sql-playground~filtering-sql:~$ /challenge/sql 
sql> SELECT * FROM repository WHERE flag_tag = 1337
```

##### Choosing Columns
```
hacker@sql-playground~choosing-columns:~$ cat /challenge/sql 
#!/opt/pwn.college/python

import sys
import string
import random
import sqlite3
import tempfile


# Don't panic about the TemporaryDB class. It simply implements a temporary database
# in which this application can store data. You don't need to understand its internals,
# just that it processes SQL queries using db.execute().
class TemporaryDB:
    def __init__(self):
        self.db_file = tempfile.NamedTemporaryFile("x", suffix=".db")

    def execute(self, sql, parameters=()):
        connection = sqlite3.connect(self.db_file.name)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        result = cursor.execute(sql, parameters)
        connection.commit()
        return result


db = TemporaryDB()


def random_word(length):
    return "".join(random.sample(string.ascii_letters * 10, length))


flag = open("/flag").read().strip()

# https://www.sqlite.org/lang_createtable.html
db.execute("""CREATE TABLE details AS SELECT 1 as flag_tag, ? as info""", [random_word(len(flag))])
# https://www.sqlite.org/lang_insert.html
for i in range(random.randrange(5, 42)):
    db.execute("""INSERT INTO details VALUES(1, ?)""", [random_word(len(flag))])
db.execute("""INSERT INTO details VALUES(?, ?)""", [1337, flag])


for i in range(random.randrange(5, 42)):
    db.execute("""INSERT INTO details VALUES(1, ?)""", [random_word(len(flag))])

# HINT: https://www.sqlite.org/syntax/result-column.html
for _ in range(1):
    query = input("sql> ")

    try:
        results = db.execute(query).fetchall()
    except sqlite3.Error as e:
        print("SQL ERROR:", e)
        sys.exit(1)

    if len(results) == 0:
        print("No results returned!")
        sys.exit(0)

    if len(results) > 1:
        print("You're not allowed to read this many rows!")
        sys.exit(1)
    if len(results[0].keys()) > 1:
        print("You're not allowed to read this many columns!")
        sys.exit(1)
    print(f"Got {len(results)} rows.")
    for row in results:
        print(f"- { { k:row[k] for k in row.keys() } }")
```

```
SELECT info FROM details WHERE flag_tag = 1337
```

##### Exclusionary Filtering
```
hacker@sql-playground~exclusionary-filtering:~$ cat /challenge/sql 
#!/opt/pwn.college/python

import sys
import string
import random
import sqlite3
import tempfile


# Don't panic about the TemporaryDB class. It simply implements a temporary database
# in which this application can store data. You don't need to understand its internals,
# just that it processes SQL queries using db.execute().
class TemporaryDB:
    def __init__(self):
        self.db_file = tempfile.NamedTemporaryFile("x", suffix=".db")

    def execute(self, sql, parameters=()):
        connection = sqlite3.connect(self.db_file.name)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        result = cursor.execute(sql, parameters)
        connection.commit()
        return result


db = TemporaryDB()


def random_word(length):
    return "".join(random.sample(string.ascii_letters * 10, length))


flag = open("/flag").read().strip()

# https://www.sqlite.org/lang_createtable.html
db.execute("""CREATE TABLE flags AS SELECT 1 as flag_tag, ? as field""", [random_word(len(flag))])
# https://www.sqlite.org/lang_insert.html
for i in range(random.randrange(5, 42)):
    db.execute("""INSERT INTO flags VALUES(1, ?)""", [random_word(len(flag))])
db.execute("""INSERT INTO flags VALUES(?, ?)""", [random.randrange(1337, 313371337), flag])


for i in range(random.randrange(5, 42)):
    db.execute("""INSERT INTO flags VALUES(1, ?)""", [random_word(len(flag))])

# HINT: https://www.sqlite.org/lang_expr.html
for _ in range(1):
    query = input("sql> ")

    try:
        results = db.execute(query).fetchall()
    except sqlite3.Error as e:
        print("SQL ERROR:", e)
        sys.exit(1)

    if len(results) == 0:
        print("No results returned!")
        sys.exit(0)

    if len(results) > 1:
        print("You're not allowed to read this many rows!")
        sys.exit(1)
    if len(results[0].keys()) > 1:
        print("You're not allowed to read this many columns!")
        sys.exit(1)
    print(f"Got {len(results)} rows.")
    for row in results:
        print(f"- { { k:row[k] for k in row.keys() } }")
```

```
SELECT field FROM flags WHERE flag_tag NOT BETWEEN 0 AND 42
```
YES!
It fills the db with garbage data up until 42, a max value of 42 columns.
From that point, it picks a random value between 1337 and 313371337 and puts the flag there.

##### Filtering Strings
```
hacker@sql-playground~filtering-strings:~$ cat /challenge/sql 
#!/opt/pwn.college/python

import sys
import string
import random
import sqlite3
import tempfile


# Don't panic about the TemporaryDB class. It simply implements a temporary database
# in which this application can store data. You don't need to understand its internals,
# just that it processes SQL queries using db.execute().
class TemporaryDB:
    def __init__(self):
        self.db_file = tempfile.NamedTemporaryFile("x", suffix=".db")

    def execute(self, sql, parameters=()):
        connection = sqlite3.connect(self.db_file.name)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        result = cursor.execute(sql, parameters)
        connection.commit()
        return result


db = TemporaryDB()


def random_word(length):
    return "".join(random.sample(string.ascii_letters * 10, length))


flag = open("/flag").read().strip()

# https://www.sqlite.org/lang_createtable.html
db.execute("""CREATE TABLE repository AS SELECT 'nope' as flag_tag, ? as payload""", [random_word(len(flag))])
# https://www.sqlite.org/lang_insert.html
for i in range(random.randrange(5, 42)):
    db.execute("""INSERT INTO repository VALUES('nope', ?)""", [random_word(len(flag))])
db.execute("""INSERT INTO repository VALUES(?, ?)""", ["yep", flag])


for i in range(random.randrange(5, 42)):
    db.execute("""INSERT INTO repository VALUES('nope', ?)""", [random_word(len(flag))])

# HINT: https://www.sqlite.org/lang_expr.html
for _ in range(1):
    query = input("sql> ")

    try:
        results = db.execute(query).fetchall()
    except sqlite3.Error as e:
        print("SQL ERROR:", e)
        sys.exit(1)

    if len(results) == 0:
        print("No results returned!")
        sys.exit(0)

    if len(results) > 1:
        print("You're not allowed to read this many rows!")
        sys.exit(1)
    if len(results[0].keys()) > 1:
        print("You're not allowed to read this many columns!")
        sys.exit(1)
    print(f"Got {len(results)} rows.")
    for row in results:
        print(f"- { { k:row[k] for k in row.keys() } }")
```

```
SELECT payload FROM repository WHERE flag_tag = "yep"
```
I just read the code. If you select the row where flag_tag = "yep" you get the right data in "payload" = flag.

##### Filtering on Expressions
We want to search for the flag.
The first part of every flag is "pwn.college{"
```
hacker@sql-playground~filtering-on-expressions:~$ cat /challenge/sql 
#!/opt/pwn.college/python

import sys
import string
import random
import sqlite3
import tempfile


# Don't panic about the TemporaryDB class. It simply implements a temporary database
# in which this application can store data. You don't need to understand its internals,
# just that it processes SQL queries using db.execute().
class TemporaryDB:
    def __init__(self):
        self.db_file = tempfile.NamedTemporaryFile("x", suffix=".db")

    def execute(self, sql, parameters=()):
        connection = sqlite3.connect(self.db_file.name)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        result = cursor.execute(sql, parameters)
        connection.commit()
        return result


db = TemporaryDB()


def random_word(length):
    return "".join(random.sample(string.ascii_letters * 10, length))


flag = open("/flag").read().strip()

# https://www.sqlite.org/lang_createtable.html
db.execute("""CREATE TABLE resources AS SELECT ? as text""", [random_word(len(flag))])
# https://www.sqlite.org/lang_insert.html
for i in range(random.randrange(5, 42)):
    db.execute("""INSERT INTO resources VALUES(?)""", [random_word(len(flag))])
db.execute("""INSERT INTO resources VALUES(?)""", [flag])


for i in range(random.randrange(5, 42)):
    db.execute("""INSERT INTO resources VALUES(?)""", [random_word(len(flag))])

# HINT: https://www.sqlite.org/lang_corefunc.html#substr
for _ in range(1):
    query = input("sql> ")

    try:
        results = db.execute(query).fetchall()
    except sqlite3.Error as e:
        print("SQL ERROR:", e)
        sys.exit(1)

    if len(results) == 0:
        print("No results returned!")
        sys.exit(0)

    if len(results) > 1:
        print("You're not allowed to read this many rows!")
        sys.exit(1)
    if len(results[0].keys()) > 1:
        print("You're not allowed to read this many columns!")
        sys.exit(1)
    print(f"Got {len(results)} rows.")
    for row in results:
        print(f"- { { k:row[k] for k in row.keys() } }")
```

```
SELECT text FROM resources WHERE substr(text, 1, 12) = "pwn.college{"
```
yes.

##### SELECTing Expressions
```
hacker@sql-playground~selecting-expressions:~$ cat /challenge/sql 
#!/opt/pwn.college/python

import sys
import string
import random
import sqlite3
import tempfile


# Don't panic about the TemporaryDB class. It simply implements a temporary database
# in which this application can store data. You don't need to understand its internals,
# just that it processes SQL queries using db.execute().
class TemporaryDB:
    def __init__(self):
        self.db_file = tempfile.NamedTemporaryFile("x", suffix=".db")

    def execute(self, sql, parameters=()):
        connection = sqlite3.connect(self.db_file.name)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        result = cursor.execute(sql, parameters)
        connection.commit()
        return result


db = TemporaryDB()

# https://www.sqlite.org/lang_createtable.html
db.execute("""CREATE TABLE logs AS SELECT ? as item""", [open("/flag").read().strip()])

# HINT: https://www.sqlite.org/lang_corefunc.html#substr
for _ in range(1):
    query = input("sql> ")

    try:
        results = db.execute(query).fetchall()
    except sqlite3.Error as e:
        print("SQL ERROR:", e)
        sys.exit(1)

    if len(results) == 0:
        print("No results returned!")
        sys.exit(0)

    for row in results:
        for k in row.keys():
            if type(row[k]) in (str, bytes) and len(row[k]) > 5:
                print("You're not allowed to read this many characters!")
                sys.exit(1)
    print(f"Got {len(results)} rows.")
    for row in results:
        print(f"- { { k:row[k] for k in row.keys() } }")
```

```
SELECT substr(item, 1, 4) FROM logs
```
so
```
SELECT substr(item, 1, 5) AS chunk1, substr(item, 6, 5) AS chunk2, substr(item, 11, 5) AS chunk3, substr(item, 16, 5) AS chunk4, substr(item, 21, 5) AS chunk5, substr(item, 26, 5) AS chunk6, substr(item, 31, 5) AS chunk7, substr(item, 36, 5) AS chunk8, substr(item, 41, 5) AS chunk9, substr(item, 46, 5) AS chunk10, substr(item, 51, 5) AS chunk11, substr(item, 56, 5) AS chunk12 FROM logs
```

Flag is actually 60 chars, not 57. lol.

##### Composite Conditions
```
hacker@sql-playground~composite-conditions:~$ cat /challenge/sql 
#!/opt/pwn.college/python

import sys
import string
import random
import sqlite3
import tempfile


# Don't panic about the TemporaryDB class. It simply implements a temporary database
# in which this application can store data. You don't need to understand its internals,
# just that it processes SQL queries using db.execute().
class TemporaryDB:
    def __init__(self):
        self.db_file = tempfile.NamedTemporaryFile("x", suffix=".db")

    def execute(self, sql, parameters=()):
        connection = sqlite3.connect(self.db_file.name)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        result = cursor.execute(sql, parameters)
        connection.commit()
        return result


db = TemporaryDB()


def random_word(length):
    return "".join(random.sample(string.ascii_letters * 10, length))


flag = open("/flag").read().strip()

# https://www.sqlite.org/lang_createtable.html
db.execute("""CREATE TABLE entries AS SELECT 1 as flag_tag, ? as element""", [random_word(len(flag))])
# https://www.sqlite.org/lang_insert.html
for i in range(random.randrange(5, 42)):
    db.execute("""INSERT INTO entries VALUES(1, ?)""", [random_word(len(flag))])
db.execute("""INSERT INTO entries VALUES(?, ?)""", [1337, flag])

for i in range(random.randrange(5, 21)):
    db.execute("""INSERT INTO entries VALUES(1337, ?)""", [random_word(len(flag))])
for i in range(random.randrange(5, 21)):
    db.execute(
        """INSERT INTO entries VALUES(1, ?)""", ["pwn.college{" + random_word(len(flag) - len("pwn.college{}")) + "}"]
    )

for i in range(random.randrange(5, 42)):
    db.execute("""INSERT INTO entries VALUES(1, ?)""", [random_word(len(flag))])

# HINT: https://www.geeksforgeeks.org/sql-and-and-or-operators/
for _ in range(1):
    query = input("sql> ")

    try:
        results = db.execute(query).fetchall()
    except sqlite3.Error as e:
        print("SQL ERROR:", e)
        sys.exit(1)

    if len(results) == 0:
        print("No results returned!")
        sys.exit(0)

    if len(results) > 1:
        print("You're not allowed to read this many rows!")
        sys.exit(1)
    if len(results[0].keys()) > 1:
        print("You're not allowed to read this many columns!")
        sys.exit(1)
    print(f"Got {len(results)} rows.")
    for row in results:
        print(f"- { { k:row[k] for k in row.keys() } }")
```

so the flag has a flag tag of 1337, and its somewhere between 5 - 42 lines of garbage followed by 10 - 42 lines of garbage. BUT! its the only 1337 between 5 - 42. lets try:
```
SELECT element FROM entries WHERE flag_tag = 1337 AND substr(element, 1, 12) = "pwn.college{"
```
Select the 1337 tag and the only element with a flag prefix.

##### Reaching Your LIMITs
```
hacker@sql-playground~reaching-your-limits:~$ cat /challenge/sql 
#!/opt/pwn.college/python

import sys
import string
import random
import sqlite3
import tempfile


# Don't panic about the TemporaryDB class. It simply implements a temporary database
# in which this application can store data. You don't need to understand its internals,
# just that it processes SQL queries using db.execute().
class TemporaryDB:
    def __init__(self):
        self.db_file = tempfile.NamedTemporaryFile("x", suffix=".db")

    def execute(self, sql, parameters=()):
        connection = sqlite3.connect(self.db_file.name)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        result = cursor.execute(sql, parameters)
        connection.commit()
        return result


db = TemporaryDB()


def random_word(length):
    return "".join(random.sample(string.ascii_letters * 10, length))


flag = open("/flag").read().strip()

# https://www.sqlite.org/lang_createtable.html
db.execute("""CREATE TABLE items AS SELECT ? as note""", [random_word(len(flag))])
# https://www.sqlite.org/lang_insert.html
for i in range(random.randrange(5, 42)):
    db.execute("""INSERT INTO items VALUES(?)""", [random_word(len(flag))])
db.execute("""INSERT INTO items VALUES(?)""", [flag])

for i in range(random.randrange(5, 21)):
    db.execute("""INSERT INTO items VALUES(?)""", [random_word(len(flag))])
for i in range(random.randrange(5, 21)):
    db.execute(
        """INSERT INTO items VALUES(?)""", ["pwn.college{" + random_word(len(flag) - len("pwn.college{}")) + "}"]
    )

for i in range(random.randrange(5, 42)):
    db.execute("""INSERT INTO items VALUES(?)""", [random_word(len(flag))])

# HINT: https://www.sqlite.org/lang_select.html#limitoffset
for _ in range(1):
    query = input("sql> ")

    try:
        results = db.execute(query).fetchall()
    except sqlite3.Error as e:
        print("SQL ERROR:", e)
        sys.exit(1)

    if len(results) == 0:
        print("No results returned!")
        sys.exit(0)

    if len(results) > 1:
        print("You're not allowed to read this many rows!")
        sys.exit(1)
    if len(results[0].keys()) > 1:
        print("You're not allowed to read this many columns!")
        sys.exit(1)
    print(f"Got {len(results)} rows.")
    for row in results:
        print(f"- { { k:row[k] for k in row.keys() } }")
```

```
SELECT note FROM items WHERE substr(note, 1, 12) = "pwn.college{" LIMIT 1
```

##### Querying Metadata
```
hacker@sql-playground~querying-metadata:~$ cat /challenge/sql 
#!/opt/pwn.college/python

import sys
import string
import random
import sqlite3
import tempfile


# Don't panic about the TemporaryDB class. It simply implements a temporary database
# in which this application can store data. You don't need to understand its internals,
# just that it processes SQL queries using db.execute().
class TemporaryDB:
    def __init__(self):
        self.db_file = tempfile.NamedTemporaryFile("x", suffix=".db")

    def execute(self, sql, parameters=()):
        connection = sqlite3.connect(self.db_file.name)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        result = cursor.execute(sql, parameters)
        connection.commit()
        return result


db = TemporaryDB()

table_name = "".join(random.sample(string.ascii_letters, 8))
db.execute(f"""CREATE TABLE {table_name} AS SELECT ? as record""", [open("/flag").read().strip()])

# HINT: https://www.sqlite.org/schematab.html
for _ in range(2):
    query = input("sql> ")

    try:
        results = db.execute(query).fetchall()
    except sqlite3.Error as e:
        print("SQL ERROR:", e)
        sys.exit(1)

    if len(results) == 0:
        print("No results returned!")
        sys.exit(0)

    if len(results[0].keys()) > 1:
        print("You're not allowed to read this many columns!")
        sys.exit(1)
    print(f"Got {len(results)} rows.")
    for row in results:
        print(f"- { { k:row[k] for k in row.keys() } }")
```

```
SELECT tbl_name FROM sqlite_masetr 
```
```
 sql> SELECT tbl_name FROM sqlite_master LIMIT 1;
Got 1 rows.
- {'tbl_name': 'SjLDoFVY'}
hacker@sql-playground~querying-metadata:~$ /challenge/sql
sql> SELECT tbl_name FROM sqlite_master
Got 1 rows.
- {'tbl_name': 'AcfkeOwZ'}
  hacker@sql-playground~querying-metadata:~$ /challenge/sql
sql> SELECT tbl_name FROM sqlite_master
Got 1 rows.
- {'tbl_name': 'qmcpYlhI'}
```

Thats interesting.
Oh. It renames it every time I run it.
So:
```
SELECT record FROM qmcpYlhI
```

FINISHED SQL PLAYGROUND AND PLAYING WITH PROGRAMS!!!!