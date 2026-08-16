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
##### System Calls
This is supposed to be pretty low level!
Writing only assembly and Linux system calls.
0 is read, 1 is write. There are more than 300 syscalls.
##### Writing Output
*Of course, the solution to this is to write multiple characters at the same time. The `write` system call does this by taking two parameters for the "what": a where (in memory) to start writing from and a how many characters to write. These parameters are passed as the second and third parameters to `write`. In the kinda-C syntax that we learned from `strace`, this would be:*

```c
write(file_descriptor, memory_address, number_of_characters_to_write)
```

*For a more concrete example, if you wanted to write 10 characters starting from some memory address to standard output (file descriptor 1), this would be:*

```c
write(1, memory_address, 10);
```

*Wow, that's simple! Now, how do we actually specify these parameters?*

1. *We'll pass the first parameter of a system call, as we reviewed above, in the `rdi` register.*
2. *We'll pass the second parameter via the `rsi` register. The agreed-upon convention in Linux is that `rsi` is used as the second parameter to system calls.*
3. *We'll pass the third parameter via the `rdx` register. This is the most confusing part of this entire module: `rdi` (the register holding the first parameter) has such a similar name to `rdx` that it's really easy to mix up and, unfortunately, the naming is this way for historic reasons and is here to stay. Oh well... It's just something we have to be careful about. Maybe a mnemonic like "`rdi` is the **i**nitial parameter while `rdx` is the **x**tra parameter"? Or just think of it as having to keep track of different friends with similar names, and you'll be fine.*

*And, of course, the `write` syscall index into `rax` itself: `1`. Other than the `rdi` vs `rdx` confusion, this is really easy!*

Ok, I did the challenge. In the beginning I didn't quite understand but basically I wrote a program that takes an arg and writes it to stdout.
###### Code:
`.intel_syntax noprefix`
`.global _start`
`_start:`
`mov rdi, 1`
`mov rsi, [rsp+16]`
`mov rdx, 1`
`mov rax, 1`
`syscall`

##### Chaining Syscalls
So I can call syscall twice, usurpingly actually.
This challenge is jut about exiting with rdi = 42 and setting rax to 60.

##### Writing Strings
I increased rdx to 64 to write the 64 bytes of the flag.

##### Reading Data
After some chatting with the Sensei Bot, I got it. the syscall needs the address of the thing I want to read/write, not the value. I kept \[rsp] and I didn't understand what is failing.
###### Code:
`.intel_syntax noprefix`
`.global _start`
`_start:`
`mov rdi, 0`
`mov rsi, rsp`
`mov rdx, 128`
`mov rax, 0`
`syscall`
`mov rdi, 1`
`mov rsi, rsp`
`mov rdx, 128`
`mov rax, 1`
`syscall`
`mov rdi, 42`
`mov rax, 60`
`syscall`

##### Reading Exactly
So far, I knew how much to read and write in terms of bytes. What if it was dynamic?
After the syscall, Linux return the num of bytes actually read in rax.
So lets change rdx!
It worked, but only in the second time.
rdx should stay at 128, because it will read 128 and will most likely use less bytes to read the flag. After that, we can use rax on rdx because it now has the value of how much was actually read after the syscall.
###### Code:
`.intel_syntax noprefix`
`.global _start`
`_start:`
`mov rdi, 0`
`mov rsi, rsp`
`mov rdx, 128`
`mov rax, 0`
`syscall`
`mov rdi, 1`
`mov rsi, rsp`
`mov rdx, rax`
`mov rax, 1`
`syscall`
`mov rdi, 42`
`mov rax, 60`
`syscall`

##### Opening Files
The registers for `open` follow the same convention:

| Register | Purpose                                  |
| -------- | ---------------------------------------- |
| `rax`    | `2` (syscall number for `open`)          |
| `rdi`    | pointer to the filename string in memory |
| `rsi`    | `0` (read-only)                          |

only now I got it. A day after. Well, I set on it for 20 minutes and used the sensai AI.
###### Code:
`.intel_syntax noprefix`
`.global _start`
`_start:`
`mov rax, 2`
`mov rdi, [rsp+16]`
`mov rsi, 0`
`syscall`
`mov rdi, rax`
`mov rsi, rsp`
`mov rdx, 4096`
`mov rax, 0`
`syscall`
`mov rdx, rax`
`mov rdi, 1`
`mov rsi, rsp`
`mov rax, 1`
`syscall`
`mov rax, 60`
`mov rdi, 42`
`syscall`

##### Hardcoding the Filename
A small change from last time.
###### Code:
```
.intel_syntax noprefix
.global _start
_start:
mov rax, 2
mov BYTE PTR [rsp], '/'
mov BYTE PTR [rsp+1], 'f'
mov BYTE PTR [rsp+2], 'l'
mov BYTE PTR [rsp+3], 'a'
mov BYTE PTR [rsp+4], 'g'
mov BYTE PTR [rsp+5], 0
mov rdi, rsp
mov rsi, 0
syscall
mov rdi, rax
mov rsi, rsp
mov rdx, 4096
mov rax, 0
syscall
mov rdx, rax
mov rdi, 1
mov rsi, rsp
mov rax, 1
syscall
mov rax, 60
mov rdi, 42
syscall

```

##### RIP-Relative Strings
```asm
_start:
    ...
    lea rdi, [rip+path]
    ...
path:
    .asciz "/flag"
```
mov copies bytes
lea copies the address!

```
.intel_syntax noprefix
.global _start
_start:
mov rax, 2
lea rdi, [rip+path]
mov rsi, 0
syscall
mov rdi, rax
mov rsi, rsp
mov rdx, 4096
mov rax, 0
syscall
mov rdx, rax
mov rdi, 1
mov rsi, rsp
mov rax, 1
syscall
mov rax, 60
mov rdi, 42
syscall
path:
    .asciz "/flag"

```

## Control Flow
So far the dude talked about jumping, conditions, looping and functions.
Kinda hard to read atm, but I'll learn.
##### Comparing Values
```
.intel_syntax noprefix
.global _start
_start:
mov rdi, [rsp]
cmp rdi, 42
setz dil
mov rax, 60
syscall

```
At first i was confused as to why it worked, bit dil is the smaller brother of rdi. and I only need 0 or 1 here as the exit code. no need to use rdi for the exit code.

##### Comparing Characters
```
.intel_syntax noprefix
.global _start
_start:
mov rax, [rsp+16]
cmp BYTE PTR [rax], 'p'
setz dil
mov rax, 60
syscall

```

##### Conditional Control Flow
```
.intel_syntax noprefix
.global _start
_start:
mov rax, [rsp+16]
cmp BYTE PTR [rax], 'p'
jne fail
success:
    mov rdi, 0
    mov rax, 60
    syscall
fail:
    mov rdi, 1
    mov rax, 60
    syscall

```

##### Comparing Strings
```
.intel_syntax noprefix
.global _start
_start:
mov rax, [rsp+16]
cmp BYTE PTR [rax], 'p'
jne fail
cmp BYTE PTR [rax+1], 'w'
jne fail
cmp BYTE PTR [rax+2], 'n'
jne fail
success:
    mov rdi, 0
    mov rax, 60
    syscall
fail:
    mov rdi, 1
    mov rax, 60
    syscall
    
```

##### Reverse the Password
I think it's qaty.

##### Conditionals Without Conditionals
11.8.26 10:18
After a lot of tries and with the help of sensai, I think I understand.
The code is a switch case kinda-thingy.
Each address is +8 bytes.
We see the address of the success and the original start of the table address.
Subtract the end from the start, divive by 8 and you get the ascii value of 'w'.

##### Recognizing Loops
```
ubuntu@control-flow~recognizing-loops:~$ objdump -d -M intel /challenge/reverse-me

/challenge/reverse-me:     file format elf64-x86-64


Disassembly of section .text:

0000000000401000 <_start>:
  401000:       48 8b 7c 24 10          mov    rdi,QWORD PTR [rsp+0x10]
  401005:       c6 04 24 4c             mov    BYTE PTR [rsp],0x4c
  401009:       c6 44 24 01 43          mov    BYTE PTR [rsp+0x1],0x43
  40100e:       c6 44 24 02 6e          mov    BYTE PTR [rsp+0x2],0x6e
  401013:       c6 44 24 03 63          mov    BYTE PTR [rsp+0x3],0x63
  401018:       c6 44 24 04 44          mov    BYTE PTR [rsp+0x4],0x44
  40101d:       c6 44 24 05 73          mov    BYTE PTR [rsp+0x5],0x73
  401022:       c6 44 24 06 00          mov    BYTE PTR [rsp+0x6],0x0
  401027:       48 8d 34 24             lea    rsi,[rsp]

000000000040102b <loop>:
  40102b:       8a 06                   mov    al,BYTE PTR [rsi]
  40102d:       3a 07                   cmp    al,BYTE PTR [rdi]
  40102f:       75 6e                   jne    40109f <fail>
  401031:       3c 00                   cmp    al,0x0
  401033:       74 08                   je     40103d <success>
  401035:       48 ff c7                inc    rdi
  401038:       48 ff c6                inc    rsi
  40103b:       eb ee                   jmp    40102b <loop>

000000000040103d <success>:
  40103d:       c6 04 24 2f             mov    BYTE PTR [rsp],0x2f
  401041:       c6 44 24 01 66          mov    BYTE PTR [rsp+0x1],0x66
  401046:       c6 44 24 02 6c          mov    BYTE PTR [rsp+0x2],0x6c
  40104b:       c6 44 24 03 61          mov    BYTE PTR [rsp+0x3],0x61
  401050:       c6 44 24 04 67          mov    BYTE PTR [rsp+0x4],0x67
  401055:       c6 44 24 05 00          mov    BYTE PTR [rsp+0x5],0x0
  40105a:       48 89 e7                mov    rdi,rsp
  40105d:       48 c7 c6 00 00 00 00    mov    rsi,0x0
  401064:       48 c7 c0 02 00 00 00    mov    rax,0x2
  40106b:       0f 05                   syscall
  40106d:       48 89 c7                mov    rdi,rax
  401070:       48 89 e6                mov    rsi,rsp
  401073:       48 c7 c2 40 00 00 00    mov    rdx,0x40
  40107a:       48 c7 c0 00 00 00 00    mov    rax,0x0
  401081:       0f 05                   syscall
  401083:       48 89 c2                mov    rdx,rax
  401086:       48 c7 c7 01 00 00 00    mov    rdi,0x1
  40108d:       48 c7 c0 01 00 00 00    mov    rax,0x1
  401094:       0f 05                   syscall
  401096:       48 c7 c0 3c 00 00 00    mov    rax,0x3c
  40109d:       0f 05                   syscall

000000000040109f <fail>:
  40109f:       48 c7 c0 3c 00 00 00    mov    rax,0x3c
  4010a6:       0f 05                   syscall
ubuntu@control-flow~recognizing-loops:~$ /challenge/reverse-me LCncDs

```

##### Writing Loops
I need to write a loop. I will reference the previous level ofc.

##### Writing From a Shared Library
The challenge is confusing

rdi - rsi
rsi - rdx

```
.intel_syntax noprefix
.global solve
solve:
    mov rax, rdi
    mov rdx, rsi
    mov rdi, 1
    mov rsi, rax
    mov rax, 1
    syscall
    mov rax, 60
    mov rdi, 0
    syscall
    
```

##### Returning a Value
```
.intel_syntax noprefix
.global solve
solve:
    mov rax, rdi
    ret
    mov rdi, 0
    mov rax, 60
    syscall
    
```
##### Calling Through a Pointer
```
.intel_syntax noprefix
.global solve
solve:
    call rdi
    ret
    mov rax, 60
    syscall

```

##### Calling Through a Pointer with an Argument
```
.intel_syntax noprefix
.global solve
solve:
    mov rax, rdi
    mov rdi, 1337
    call rax
    ret
    mov rax, 60
    syscall

```

##### Saving Caller-Saved Registers
```
.intel_syntax noprefix
.global solve
solve:
    push rax
    push rcx
    push rdx
    push rdi
    push r8
    push r9
    push r10
    push r11
    push rsi
    call rdi
    pop rsi
    pop r11
    pop r10
    pop r9
    pop r8
    pop rdi
    pop rdx
    pop rcx
    pop rax
    call rsi
    ret
    mov rax, 60
    mov rdi, 0
    syscall

```

##### Saving Callee-Saved Registers
So doing the same, but om the other side.
i am still trying to wrap around how does this translate to actual programs.
```
.intel_syntax noprefix
.global solve
solve:
    push rbx
    push rbp
    push r12
    push r13
    push r14
    push r15
    mov rbx, 0x1337
    mov rbp, 0x1337
    mov r12, 0x1337
    mov r13, 0x1337
    mov r14, 0x1337
    mov r15, 0x1337
    call rdi
    pop r15
    pop r14
    pop r13
    pop r12
    pop rbp
    pop rbx
    ret

```
This didn't work for like 20 minutes but worked after re-building it. IDK why.
DONE!!!
at 12.8.26 17:20

## Endian Escapades
##### Little-Endian
Basically, when I write 0x12131415 the computer reads it as 15 14 13 12 because it goes from the least significate byte to the most significate.

##### Memory Order and Register Values
The easiest place to get turned around is the boundary between memory order and the value printed from a register. Suppose `rdi` points at these eight bytes:

```text
Address    Byte
[rdi+0]    41
[rdi+1]    42
[rdi+2]    43
[rdi+3]    44
[rdi+4]    45
[rdi+5]    46
[rdi+6]    47
[rdi+7]    48
```

A 64-bit load reads those bytes starting at the lowest address:

```asm
mov rax, [rdi]
```

Because x86 is little-endian, `[rdi+0]` becomes the low byte of `rax`, `[rdi+1]` becomes the next byte, and so on. The register value is therefore `0x4847464544434241`. Written as hex, the most-significant byte prints on the left, so the bytes look reversed compared to address order:

```text
memory address order:  41 42 43 44 45 46 47 48
register hex order:   48 47 46 45 44 43 42 41
rax value:            0x4847464544434241
```

The bytes did not move in memory. The CPU interpreted the byte at the lowest address as the least-significant part of the number.

##### Bytes, Words and Friends
| Name                 | Bits | Bytes | Partial `rax` Access | Memory Access                             |
| -------------------- | ---- | ----- | -------------------- | ----------------------------------------- |
| byte                 | 8    | 1     | `mov al, [rdi]`      | `mov BYTE PTR [rdi], 0x11`                |
| word                 | 16   | 2     | `mov ax, [rdi]`      | `mov WORD PTR [rdi], 0x1122`              |
| doubleword (`dword`) | 32   | 4     | `mov eax, [rdi]`     | `mov DWORD PTR [rdi], 0x11223344`         |
| quadword (`qword`)   | 64   | 8     | `mov rax, [rdi]`     | `mov QWORD PTR [rdi], 0x1122334455667788` |

##### Sign Extension
```
.intel_syntax noprefix
.global solve
solve:
    movsx rax, BYTE PTR [rdi] // Takes the first byte of rdi
								//And saves it in rax as singed
    ret
    

```

##### Little-Endian Bytes
`movabs rbx,0x43785a6d436f6e6f`
so:
6f 6e 6f 43 6d 5a 78 43
onoCmZxC

##### Qword by Qword
movabs rbx,0x72556147477a314e
movabs rbx,0x7974485356646b43
This is stored like that. We need to flip the order of each byte. But the order of the qwords stay intact.
so:
4e 31 7a 47 47 61 55 72
43 6b 64 56 53 48 74 79
N1zGGaUrCkdVSHty

##### Dword by Dword
16.8.26 15:24
eax,0x384d7672 0x72764d38
eax,0x49646661 0x61666449
eax,0x514a6e57 0x576e4a51
eax,0x4c554b66 0x664b554c

rvM8afdIWnJQfKUL

##### Word by Word
ax,0x3862
ax,0x6951
ax,0x5973
ax,0x4876
ax,0x3947
ax,0x7146
ax,0x5935
ax,0x4161
0x62385169735976484739467135596141
b8QisYvHG9Fq5YaA

##### Byte by Byte
Nothing to reverse here.
al,0x48
al,0x42
al,0x35
al,0x6a
al,0x37
al,0x48
al,0x57
 al,0x4d
al,0x7a
al,0x58
al,0x69
al,0x32
al,0x41
al,0x62
al,0x6f
al,0x30
0x4842356a3748574d7a58693241626f30
HB5j7HWMzXi2Abo0

##### Cracking a Struct
rbx,0x4b544c7673367064
eax,0x79495a54
ax,0x5557
al,0x76
al,0x4f

0x64703673764c544b545a49795755764f
dp6svLTKTZIyWUvO

##### Scrambled Struct
In the previous challenge, I could read the registers from top to button because they were checked in order to their place in memory.
In this challenge, I assume, the order will be scrambled and I will have to read it by \[rdi+X]

```
0000000000401000 <_start>:
  401000:       48 8b 7c 24 10          mov    rdi,QWORD PTR [rsp+0x10]
  401005:       8b 47 08                mov    eax,DWORD PTR [rdi+0x8]
  401008:       3d 66 76 75 70          cmp    eax,0x70757666
  40100d:       0f 85 90 00 00 00       jne    4010a3 <fail>
  401013:       66 8b 47 0c             mov    ax,WORD PTR [rdi+0xc]
  401017:       66 3d 33 64             cmp    ax,0x6433
  40101b:       0f 85 82 00 00 00       jne    4010a3 <fail>
  401021:       48 bb 77 77 56 61 4a    movabs rbx,0x3566394a61567777
  401028:       39 66 35 
  40102b:       48 8b 07                mov    rax,QWORD PTR [rdi]
  40102e:       48 39 d8                cmp    rax,rbx
  401031:       75 70                   jne    4010a3 <fail>
  401033:       8a 47 0e                mov    al,BYTE PTR [rdi+0xe]
  401036:       3c 66                   cmp    al,0x66
  401038:       75 69                   jne    4010a3 <fail>
  40103a:       8a 47 0f                mov    al,BYTE PTR [rdi+0xf]
  40103d:       3c 6e                   cmp    al,0x6e
  40103f:       75 62                   jne    4010a3 <fail>
```
By order:
rbx,0x3566394a61567777
eax,0x70757666
ax,0x6433
al,0x66
al,0x6e

0x777756614a396635667675703364666e
wwVaJ9f5fvup3dfn

DONE!!