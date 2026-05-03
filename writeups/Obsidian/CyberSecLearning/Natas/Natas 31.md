#natas #natas31
natas30
WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH
 
 What I See:
 I see a login page, username and password. The backend is written in perl. I see that the parameters are escaped via quote() function.

How I Think It Works:
 I read that it stops SQL injections. I will still try and maybe i will find something new.
 If not, maybe i will try something else. idk now, i just started trying.

Solving:
I noticed that username=natas31&password=0 will not print "fail:(", while every other one single digit does. and multiple 0 does. this has to mean something.
Actually, if any parameter, also username, is "0", then the program wont print out "fail:(". This is odd.
I read [[this]] and it got me thinking that there is a way maybe to solve this level by making the app think that a query is true using numbers and words comparing, which is weird apparently in MySQL. I used chatgpt just for helping me think, not telling me the payload. I don't know the payload yet lol. 
After some trial and error I think this is not the case. in the code, it does not specifically search for numbers or strings only. Chat lied, and I caught that.
no Implicit type conversion here. At least I learned a bit about that...
After a few hours i solved it. I knew it involved giving a few parameters.
in POST:
username=natas31&password='lol' or 1&password=4

why? well, username has to be known. so natas30 or natas31 would be smart.
then two password parameters. when giving pram() an array it will notice the second one. when giving it 4, it has to do something with SQL_INTEGER, which irdk what it does. when the code sees that it got a 4, it tells itself "ok, this input is safe, i won't quote it." which lets our SQL injection pass.


Password:
m7bfjAHpJmSYgQWWeqRE2qVBuMiRNq0y

Lesson Learned:
Read docs, search online well and understand that if a function expect X and you do Y, it might behave differently.
I liked this challenge. i spent maybe 4 hours on it total. good day.