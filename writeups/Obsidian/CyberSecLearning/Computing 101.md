## Your First Program
So far I have watched Computer Architecture and Assembly.
They are both interesting. I will write any notes I'll have here.
This website is quite amazing!

"What is the difference between compiled, interpreted and JIT?"

Registers - A fast place to store data. A file inside the CPU.
The size of the Register will typically be the size of the architecture (64 bit, for example).
If you write into eax, 32bit, it will zero out the rest of the register. For a complicated reason.
mov copies, not cuts.
OK, finished the video. It got complicated at the end. I will take a break to eat something and do other stuff. I will do the activity later on.

20.7.26 14:51
Came back to learning. Fed and more relaxed. I hope.
##### Your First Register
It was very straightforward. Do exactly what is written. That's it. I put the value of 60 into rax.
Its weird to think that only 12,000 people had solved this. That's a stupidly low number of people!

##### Your First Syscall
*Each system call is indicated by a syscall number, counting upwards from 0, and your program invokes a specific syscall by moving its syscall number into the `rax` register and invoking the `syscall` instruction. For example, if we wanted to invoke syscall 42 (a syscall that you'll learn about sometime later!), we would write two instructions:*

```assembly
mov rax, 42
syscall
```

Basically, to invoke syscall 42 you do it like how it is shown above.

##### Exit Codes
Nothing really hard. I learned about exit codes, used it in rdi.
It's a shame I didn't learn this before 18. Well, nothing to whine about.

(21.7.26 11:46)

##### Building Executables
To make an assembly file executable, first we must declare which syntax we are using.
We will use `.intel_syntax noprefix` at the top of the file.
Its a directive.
To make it an object file, we will use the `as` command.
Example: `as -o program.o program.s`
Then, we need to link between the Object file into an Executable file.
We are linking the .o and the .s into a program.
We are using the `ld` command.
Example: `ld -o program program.o`
`.global _start`
`\_start:`
will declare when to start the execution. By default, it starts from the first line.

##### Moving Between Registers
Nothing fancy. Basic stuff. Finished this Module.

## Computer Memory
(27.7.26)
##### Memory
Each memory locations is 1 byte.
0x1000
to
0x7fffffffffff
###### Stack
The stack lives in the memory and operates like the stack you know. You push and pop values, or addresses into it. Think about a pistol clip.
The address of the stack is stored at rsp. The address of the stack changes according to its size.

A lot more was explained, like little endian and about how to know where to store data in the memory with math. I don't grasp it 100%, but I think the challenges will help.

##### Loading From Memory
I used the notes from previous lectures and it was easy.

##### More Loading Practice
This time, I'll try to use the notes as less as possible.

##### Dereferencing with Offsets
(28.7.26 14:15)
Fairly simple. Like accessing an array.

##### Stored Addresses
Instead of storing values at addresses only, we can store addresses in adresses to point at values.
"I'll store a secret value at a secret address, then store that secret address at the address `567800`. You must read the address, dereference it, get the secret value, and then `exit` with it as the exit code. You got this!"

so the address of the adress of the secret is 567800.
Fairly simple.

##### Double Dereferencing
It was again, fairly simple. I shall continue learning today.

## The Stack
(28.7.26 16:00)
##### The Stack
In this challenge we learned that \[rsp] holds the number of args that is passed to the program. IDK why yet.

##### Stack Offsets
We will learn to use stack offsets with \[rsp + N]

##### Program Arguments on the Stack
This one seems a but tough. IDK. It seems simple but I guess I'll just try it out.
I got it a bit wrong the first time.
\[rsp] - argc (arg counter)
\[rsp + 8] - arg\[0] usually the program name
\[rsp + 16] - arg\[1] the first arg

##### Popping From the Stack
I need to use pop to get argc, or \[rsp] .
I will mov it to rdi and exit with it.
So it was pretty basic. I am quite afraid/excited to the more advanced stuff.

## Nibbling on Numbers
(29.7.26)
##### Data
We use HEX to represent binary numbers because its in the power of 2 and it aligns quite well.
His lectures are LONG! Very good, but long. Plus, I'm kinda sick so it's even harder.
(30.7.26)
##### Negative Numbers
so if the number starts with 1 its a negative, 0 is positive. to find the flip number you flip the bits and add one bit.

01001010 is 74
10110101 flipped
10110110 + 1 bit = -74
Understood.

1010111110001010
0101000001110101
0101000001110110
11011101 11010100 01110111 11100100
00100010 00101011 10001000 00011011
00100010001010111000100000011100

##### Encoding Negatives
30 - 11110
00001 + 1 = 01000
13 - 00001101
11110011

##### Binary and Hex Encoding
(2.8.26 13:36)
A single hex digit is 4 bits.
A byte is 8 bits.
So basically you split it and encode each half to hex.
1111 0110
F6
1001 1000
98
EZ

##### More Hex
Basically the same.
I cannot start any challenge though. The website has an issue of some sort.
20:45 
Seems to be working again. Lets finish this module and go to sleep!
0011 0000 1110 1010 0000 0110
30EA06
1001 1001 0001 1110 1000 1100
991E8C

##### Mixed Conversions
Did that too. Basically I have to remember that to get the signed value of X i gotta do 256 - X.

## Software Introspection
3.8.26 9:58
Lets Go!!!

##### Disassembling Programs
`objdump -d` to disassemble a program back to assembly.
We have to add `-M intel` to specify using intel infrastructure.
in this challenge, we need to submit the value of rdi before it's being wiped.

##### Tracing Syscalls
Lets run it.
EZ

##### Starting GDB
As simple as it can be.
`gdb`

##### Quitting GDB
Same.
`quit`

##### Starting Programs in GDB
`starti`

##### Disassembling in GDB
`disassemble`

##### Stepping Through Instructions
`stepi` to execute one command at a time. Even though the disassembly is censored, the value is still loaded to the CPU.
Worked the second time around. First time it gave me a value of 0.

##### Reading Register Values
1. Start the program with `starti`
2. Step one instruction with `stepi` (or `si`)
3. Read the register yourself with `print $rdi`
Ill add the solution just to show you (or me) that I did solve it. So far it's not challenging, just educational. I assume it will be much harder.
###### Code:
`ubuntu@introspecting~reading-register-values:~$ gdb /challenge/debug-me`
`GNU gdb (Ubuntu 15.1-1ubuntu1~24.04.1) 15.1`
`Copyright (C) 2024 Free Software Foundation, Inc.`
`License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>`
`This is free software: you are free to change and redistribute it.`
`There is NO WARRANTY, to the extent permitted by law.`
`Type "show copying" and "show warranty" for details.`
`This GDB was configured as "x86_64-linux-gnu".`
`Type "show configuration" for configuration details.`
`For bug reporting instructions, please see:`
`<https://www.gnu.org/software/gdb/bugs/>.`
`Find the GDB manual and other documentation resources online at:`
    `<http://www.gnu.org/software/gdb/documentation/>.`

`For help, type "help".`
`Type "apropos word" to search for commands related to "word"...`
`Reading symbols from /challenge/debug-me...`
`(No debugging symbols found in /challenge/debug-me)`
`Warning: 'set logging on', an alias for the command 'set logging enabled', is deprecated.`
`Use 'set logging enabled on'.`

`(gdb) starti`

`Dump of assembler code for function main:`
`=> 0x0000000000401000 <+0>:     mov    rdi,CENSORED`
   `0x0000000000401007 <+7>:     mov    rdi,0x0`
   `0x000000000040100e <+14>:    mov    rax,0x3c`
   `0x0000000000401015 <+21>:    syscall`
`End of assembler dump.`

`HACKER: The disassembly is CENSORED! Use 'stepi' to execute the first instruction.`
`0x0000000000401000 in main ()`
`(gdb) stepi`

`Dump of assembler code for function main:`
   `0x0000000000401000 <+0>:     mov    rdi,CENSORED`
`=> 0x0000000000401007 <+7>:     mov    rdi,0x0`
   `0x000000000040100e <+14>:    mov    rax,0x3c`
   `0x0000000000401015 <+21>:    syscall`
`End of assembler dump.`

`HACKER: You just executed 'mov rdi, CENSORED' --- the secret is now in rdi!`
`HACKER: Use 'print $rdi' to read the register value!`
`HACKER: When you're done, quit GDB with 'quit' (or 'q').`
`0x0000000000401007 in main ()`
`(gdb) print $rdi`
`$1 = 31546`
`(gdb) quit`
`ubuntu@introspecting~reading-register-values:~$ /challenge/submit-number 31546`
`CORRECT! Here is your flag:`


##### Setting Register Values
`set` command sets a value for a register.
I completed the level. its 10:51, Imma take a short break.

##### Popping Stack Values
Basically the same but with pop rdi.

##### Examining Memory
This time the secret isn't loaded into a register. Its argc, but we get it by examining the memory itself. How? Let's find out.
`x $rsp`
###### Code:
`ubuntu@introspecting~examining-memory:~$ gdb /challenge/debug-me`
`GNU gdb (Ubuntu 15.1-1ubuntu1~24.04.1) 15.1`
`Copyright (C) 2024 Free Software Foundation, Inc.`
`License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>`
`This is free software: you are free to change and redistribute it.`
`There is NO WARRANTY, to the extent permitted by law.`
`Type "show copying" and "show warranty" for details.`
`This GDB was configured as "x86_64-linux-gnu".`
`Type "show configuration" for configuration details.`
`For bug reporting instructions, please see:`
`<https://www.gnu.org/software/gdb/bugs/>.`
`Find the GDB manual and other documentation resources online at:`
    `<http://www.gnu.org/software/gdb/documentation/>.`

`For help, type "help".`
`Type "apropos word" to search for commands related to "word"...`
`Reading symbols from /challenge/debug-me...`
`(No debugging symbols found in /challenge/debug-me)`
`Warning: 'set logging on', an alias for the command 'set logging enabled', is deprecated.`
`Use 'set logging enabled on'.`

`(gdb) starti`

`Dump of assembler code for function main:`
`=> 0x0000000000401000 <+0>:     mov    rdi,0x0`
   `0x0000000000401007 <+7>:     mov    rax,0x3c`
   `0x000000000040100e <+14>:    syscall`
`End of assembler dump.`

`0x0000000000401000 in main ()`
`(gdb) x/d $rsp`
`0x7fffffffe6a0: 123`
`(gdb) quit`
`ubuntu@introspecting~examining-memory:~$ /challenge/submit-number 123`
`CORRECT! Here is your flag:`

##### Examining Stack Pointers
This is how to get the address of the first argument of the program:
`x/a $rsp+16`
Then to display the data as a string we do:
`x/s 0x7ffc001c4750`, assuming this is the address.

##### Cooperative Debugging
`int3` is basically a brekapoint. Like the red dot in VS Code.
Did the challenge. I should read the instructions more carefully.

##### Running with Arguments
ubuntu@introspecting~running-with-arguments:~$ /challenge/debug-me pwn
{flag}

Ok...

##### Redirecting Input in GDB
I ran /challenge/debug-me with gdb.
Then, inside the debgger, I ran the command with input from /challenge/secret with:
`run < /challenge/secret`
Then it did some stuff, downloaded something? debuginfod
It gave me the secret number which I fed into /challenge/submit-number and got the flag.

It's 13:53 now. I finished this module.

## Output and Input
(4.8.26)
