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

## Assembly Assortment
##### Reverse the Calculation
I assume we want to submit the original value.
0x8c - 0x47 = 0x45
E

##### Reverse the Reverse
```
  401000:       48 8b 44 24 10          mov    rax,QWORD PTR [rsp+0x10]
  401005:       80 28 0d                sub    BYTE PTR [rax],0xd
  401008:       80 38 27                cmp    BYTE PTR [rax],0x27
```

so 0x27 + 0xd
4

##### Dealing with Bitwise Operations
```
0000000000401000 <_start>:
  401000:       48 8b 44 24 10          mov    rax,QWORD PTR [rsp+0x10]
  401005:       80 30 94                xor    BYTE PTR [rax],0x94
  401008:       80 38 a7                cmp    BYTE PTR [rax],0xa7
```

so 0xa7 xor 0x94 should give us the original value
10100111
10010100
00110011
3 ASCII

##### Even or Odd
```
.intel_syntax noprefix
.global solve
solve:
    and rdi, 0b1
    cmp rdi, 0
    je  even
    mov rax, 0
    ret
    even:
        mov rax, 1
        ret

```

##### Masking Bits
```
.intel_syntax noprefix
.global LOBYTE
LOBYTE:
    and rdi, 0xFF
    mov rax, rdi
    ret
    
```

##### Lowercase a String
```
.intel_syntax noprefix
.global chr_lower
chr_lower:
    or rdi, 0x20
    mov rax, rdi
    ret
    
```

##### Uppercase a String
I totally used an LLM to understand it.

```
.intel_syntax noprefix
.global str_upper
str_upper:

.loop:
    cmp BYTE PTR [rdi], 0x0
    je done

    and BYTE PTR [rdi], 0xDF
    inc rdi
    jmp .loop

done:
    mov rax, rdi
    ret

```

##### Swap Case
```
.intel_syntax noprefix
.global str_swapcase
str_swapcase:

.loop:
    cmp BYTE PTR [rdi], 0x0
    je done
    xor BYTE PTR [rdi], 0x20
    inc rdi
    jmp .loop

done:
    mov rax, rdi
    ret

```

##### Shifting Left
```
.intel_syntax noprefix
.global solve
solve:
    mov rdi, rax
    shl rax, 4
    ret


```
This does rax times 16, because 4 to the power of 2 is 16.

##### Shifting Right
This does root. I assume.
```
.intel_syntax noprefix
.global solve
solve:
    mov rax, rdi
    shr rax, 8
    and rax, 0xFF
    ret

```

##### Guide: Reading Stored Data in GDB
Back in [Opening the Flag, with RIP](https://pwn.college/computing-101/hello-hackers/open-read-write-rip-relative), you used a label and `lea` to pass the address of stored bytes to `open`. In [Examining Memory with GDB](https://pwn.college/computing-101/introspecting/gdb-examine-argv1), you used `x/s` to display the string at an address.

The next challenge combines those ideas in a binary you are reversing. The binary has already done the `lea`-style work for you: one of its registers will hold the runtime address of a stored string. Instead of looking for every secret byte as an immediate inside a `cmp`, step through the code until a register points at the stored string, then examine that address as a string:

```gdb
(gdb) x/s $rsi
```

Here, `$rsi` is just an example register. Use the register that the binary loads with the stored string's address, then run `/challenge/reverse-me` directly with the string you found.

##### Loops on Data
So far, the values you've been reversing have been embedded directly in instructions as immediate operands. However, this challenge compares the first program argument against a hardcoded string inside the challenge. The string lives in a different section of the program file: the binary's `.rodata` (read-only data) section, rather than in the instructions themselves.

There are several options to find it:

- The most familiar: `stepi` to where the comparison is happening and `x` the registers pointing to the data.
- Use `strings /challenge/reverse-me` to list all printable strings in the binary. There are a lot, but one of them will be the password.
- Use `objdump -s -j .rodata /challenge/reverse-me` to dump the raw contents of the `.rodata` section.

Which you use is up to you!

I used gdb and I `layout asm`
and `x/s $rsi` or whatever it was.

DONE?

## The Stack, Revisited
##### Reaching Into the Caller's Frame
I am building a function that grabs the flag from the calling function, but this data isn't handed to me. This level teaches you to kinda RCE..?
So to my understanding, all the data lives on the stack. Well, not ALL of the data, but because the function that calls my function has the flag in it, and it is on the stack, it is readable by my function as well.
The flag will be at a higher address, because the more you add to the stack, the smaller address you get at the start of it.
```
.intel_syntax noprefix
.global solve
solve:
    lea rdi, [rsp + 0x40]
    mov rdx, 0
    count_loop: // Code to calculate size of flag and store it in rdx
        cmp BYTE PTR [rdi + rdx], 0x0
        je write_data
        inc rdx
        jmp count_loop
    write_data:
        mov rdi, 1
        lea rsi, [rsp + 0x40]
        mov rax, 1
        syscall
    mov rdi, 42
    mov rax, 60
    syscall

```
I should definitely remember the comment I wrote here. Its a basic and important thing to get in my mind! A basic loop to get rdx out of any length of value to print.

##### Loading Stale Stack Data
```
.intel_syntax noprefix
.global solve
solve:
    call rdi
    mov rax, qword ptr [rsp-0x10]
    ret
```

##### Stealing Stale Stack Data
```
.intel_syntax noprefix
.global solve
solve:
    call rdi
    lea rdi, [rsp - 0x88]
    mov rdx, 0
    count_loop: // Code to calculate size of flag and store it in rdx
        cmp BYTE PTR [rdi + rdx], 0x0
        je write_data
        inc rdx
        jmp count_loop
    write_data:
        mov rdi, 1
        lea rsi, [rsp - 0x88]
        mov rax, 1
        syscall
        ret


```

##### Reserving Your Own Frame
I will learn how to reserve my own frame of data on the stack.
We sub rsp with how many bytes we want, fill them up with 0 to initlize them and then add back the bytes we sub to return for a correct return address (or sum like that).

```
.intel_syntax noprefix
.global solve
solve:
    mov rcx, 0
    sub rsp, 256
    init_bytes:
        mov byte ptr [rsp+rcx], 0
        cmp rcx, 255
        je success
        inc rcx
        jmp init_bytes
    success:
        add rsp, 256
        ret


```

##### Using Your Own Frame
I am very confused. Very much so.
```
.intel_syntax noprefix
.global solve
solve:
    mov rcx, 0
    mov r8, 0
    mov r9, 0
    sub rsp, 256
    mov rax, 0
    init_bytes:
        mov byte ptr [rsp+rcx], 0
        cmp rcx, 255
        je count_bytes
        inc rcx
        jmp init_bytes
    count_bytes:
        mov cl, byte ptr [rdi+r8]
        mov byte ptr [rsp+rcx], 1
        inc r8
        cmp r8, rsi
        je compare_bytes
        jmp count_bytes

    compare_bytes:
    cmp r9, 256
    je success

    cmp byte ptr [rsp+r9], 0
    je next_slot
    inc rax
    next_slot:
        inc r9
        jmp compare_bytes
    success:    
        add rsp, 256
        ret

```
Took some time and debugging with Sensai.

##### Environment Variables on the Stack
The flag will be as an environmental variable at \[rsp+24]
```
.intel_syntax noprefix
.global _start
_start:
    lea rdi, [rsp + 24]
    mov rdx, 0
    count_loop: // Code to calculate size of flag and store it in rdx
        cmp BYTE PTR [rdi + rdx], 0x0
        je write_data
        inc rdx
        jmp count_loop
    write_data:
        mov rdi, 1
        lea rsi, [rsp + 24]
        mov rax, 1
        syscall
    mov rdi, 42
    mov rax, 60
    syscall
```
This DOES NOT GET ACCEPTED!!
It says it accepts 8 instructions. I find it a bit dumb, but whatever.
```
.intel_syntax noprefix
.global _start
_start:
    mov rdi, 1
    mov rsi, [rsp + 24]
    mov rdx, 128
    mov rax, 1
    syscall
    mov rdi, 42
    mov rax, 60
    syscall

```
So apparently I don't need to calculate the exact size of the string and put it in rdx?
I will add this sequense for future referencing
Read/Write Data
```
# read up to 128 bytes  
xor eax, eax  
xor edi, edi  
lea rsi, [rsp]  
mov edx, 128  
syscall  


# write exactly the number of bytes that read returned  

mov rdx, rax  
mov eax, 1  
mov edi, 1  
syscall
```

##### Aligning the Stack Through the Environment
env -i FOO=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX /challenge/program
Minus 1 X for the null byte!

The Stack grows backwards.
"But where do the actual addresses (`rsp`, or the actual address that `rsp+200` resolves to, etc.) come from?

When your program is launched, the kernel **fills the stack backwards** from some chosen starting address. From there, it lays down the env strings ("growing" toward smaller addresses), then the arg strings, other metadata, then the `envp[]` and `argv[]` pointer tables, and finally `argc` on the leftmost side of the structure. That's where `rsp` ends up pointing.

This has an interesting consequence: **the more bytes you stuff into the environment (or the program arguments), the further "left" the stack the kernel pushes everything else**. An extra env byte means `rsp` ends up at a smaller address, the arg-strings region sits one byte further "left", and `argv[0]` (a pointer into that region) holds a one-byte-smaller value."

##### Aligning the Stack Through GDB
"A common stack-related snafu is the shift in stack addresses that happens when launching a program under gdb. By default, gdb passes its own environment (your shell's env, plus a few of gdb's own additions) to the debugged program, and these extra environment variables shift the stack to the left, so `argv[0]` ends up at a different address than it does when you run the program straight from your shell. This isn't so important right now, but it becomes a big bother later on when you're trying to figure out why your bit-precise exploit code works in gdb but not on a target running normally. In those cases, learning to "synchronize" the two environments is important.

This challenge will teach you the basics: making the addresses outside of gdb line up better with the addresses inside gdb.

1. Run `/challenge/program` under gdb (`gdb /challenge/program`, then `run`). The program records its own `argv[0]` as your target.
2. Quit gdb. Run `/challenge/program` from your shell --- it'll tell you how far off your shell-context `argv[0]` is from the target.
3. Use an environment variable to "pad" your shell environment until `argv[0]` lands at the gdb-captured target.
4. Flag!"
Target Address: 0x7fffffffed1d
-
env FOO=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXX /challenge/program

##### Aligning the Stack Through GDB, Generalized
"The challenge in the previous level inherited your interactive shell's environment both in and outside of gdb. In reality, the differences in environment are often more significant between your local setup and the target you're analyzing. The binary you're debugging from your shell and the same binary running as a service, a cron job, or a remote script would see completely different environments (different `HOME`, different `PATH`, a different _set_ of variables entirely).

This level explores this concept a bit more. In this level, the `gdb` wrapper sets its own environment rather than inheriting it from your shell, and the challenge, when run directly forces you to do the same, requiring an environment with only a single variable. For example:

```console
hacker@dojo:~$ /challenge/program
You're running me with 8 environment variables, but I need exactly 1! Clear the environment and set one variable, then rerun me!
hacker@dojo:~$ /challenge/program
```

How do you clear the environment? You can do so with the `env` command, which we've used before to print out all exported environment variables in the [Linux Luminarium](https://pwn.college/linux-luminarium/variables). The `env` command can also be used as a _wrapper_ to carefully control the environment of a program. For example, you can clear the child program's environment completely using `env -i`:

```console
hacker@dojo:~$ env -i /challenge/program
You're running me with 0 environment variables, but I need exactly 1! Clear the environment and set one variable, then rerun me!
hacker@dojo:~$ /challenge/program
```

You can also set variables after clearing the environment:

```console
hacker@dojo:~$ env -i PWN=COLLEGE HACK=PLANET /challenge/program
You're running me with 2 environment variables, but I need exactly 1! Clear the environment and set one variable, then rerun me!
hacker@dojo:~$ /challenge/program
```

This allows you to have very finegrained control over your environment. In this challenge, you'll use this finegrained control to line up addresses in a slightly more realistic setting, but keep the capability in mind for other situations!"

env -i FOO=IAMPADDINGIHAVEASTORYTOTELLYOUSOONCEUPONATIMETHEREWASACHILDNAMEDBOBANDHELIKEDTOPLAYINTHESANDBOBFOUNDACRABNAMEDBOBANDHEWASLIKEWOWANOTHERBOBTHARSMADSOBOBBITBOBBUTWHICHBOBBITTHEOTHERBOBTHATSAGREATQUESTIONANDIDONTHAVEANANSWERSORRYIHAVETOGOBYEEE

DONE!!!!

## Numbers as Strings
##### A Single Digit
I need to create a function theat gets 0-9 in hex in rdi and returns the number as decimal in rax.
OK?
```
.intel_syntax noprefix
.global atoi_digit
atoi_digit:
    movzx rdx, byte ptr [rdi]
    sub rdx, 0x30
    mov rax, rdx
    ret
```
I got wrong the part which is replaced by movzx and byte ptr. I thought I could work with the whole register.

##### Two Digits
I spend maybe an hour+ on this. At least.

```
.intel_syntax noprefix
.global atoi_digit
.global atoi
atoi_digit:
    movzx rdx, byte ptr [rdi]
    sub rdx, 0x30
    mov rax, rdx
    ret
atoi:
    push rdi
    call atoi_digit
    pop rdi
    mov rcx, rax
    imul rcx, 10
    inc rdi
    push rcx
    call atoi_digit
    pop rcx
    add rcx, rax
    mov rax, rcx
    ret

```
A chat I had with the LLM:

I dont quite understand the rdi and rdi+1 part.

so in the first call i am giving the atoi-digit a value to parse in rdi. But rdi hold 2 digits. how does it take the leftmost digit first and doesnt crash because i gave it two bytes instead of one?

- 

That’s the key idea: **`rdi` does not hold the digits themselves. It holds an address**.

## What `rdi` really contains

If the harness calls:

```c
atoi("42")
```

then memory looks like:

```text
address p:     '4'
address p+1:   '2'
address p+2:   '\0'
```

and `rdi = p`.

So:

- `rdi` points to `'4'`
- `rdi + 1` points to `'2'`

## Why `atoi_digit` only reads one digit

Your code does:

```asm
movzx rdx, byte ptr [rdi]
```

That means:

- go to the memory address in `rdi`
- read **exactly 1 byte**

So if `rdi = p`, it reads only `'4'`.

It does **not** read the whole string.

## Then why `rdi+1`?

After `inc rdi`, now `rdi = p+1`, so:

```asm
movzx rdx, byte ptr [rdi]
```

reads only `'2'`.

## Why no crash?

Because both `p` and `p+1` are valid addresses in the string.

You’d only crash if you pointed somewhere invalid.

## Mental model

Think of:

- `rdi` = “where to start reading”
- `byte ptr [rdi]` = “read one character from there”

##### String to Integer
```
.intel_syntax noprefix
.global atoi_digit
.global atoi
atoi_digit:
    movzx rdx, byte ptr [rdi]
    sub rdx, 0x30
    mov rax, rdx
    ret
atoi:
    push rdi
    call atoi_digit
    pop rdi
    loop:
    mov rcx, rax
    imul rcx, 10
    inc rdi
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x0
    je null_byte
    push rcx
    call atoi_digit
    pop rcx
    add rcx, rax
    mov rax, rcx
    jmp loop
null_byte:
    ret

```
I DONT KNOW HOW TO DEBUG WITH GDB AND THATS A PROBLEM!!
25.8.26 19:21
I am on my day off and I used an LLM to teach me to debug with gdb. I am pasting the output here for future references:
###### How to Debug:
Absolutely—and it’s not bad that you don’t know GDB yet. GDB feels confusing until you learn a small repeatable workflow. We’ll use the challenge’s _start exactly as intended and watch:

the test string get placed on the stack,
rdi point to it,
call atoi enter your function,
rdi move through each character,
rax build the result,
the bug appear when '\0' becomes -48.
1. Create a debugging version

Save this as debug.s:

.intel_syntax noprefix

.global _start
.global atoi_digit
.global atoi

_start:
    push 0x333231       # Stack bytes become: 31 32 33 00...
                        # In ASCII: "123\0"

    mov rdi, rsp        # rdi points to "123"
    int3                # GDB will stop here

    call atoi

    mov rdi, rax        # Linux exit status = atoi result
    mov rax, 60         # exit syscall
    syscall


atoi_digit:
    movzx rdx, byte ptr [rdi]
    sub rdx, 0x30
    mov rax, rdx
    ret


atoi:
    call atoi_digit

loop:
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0
    je null_byte

    mov rcx, rax
    imul rcx, 10

    inc rdi

    push rcx
    call atoi_digit
    pop rcx

    add rcx, rax
    mov rax, rcx
    jmp loop

null_byte:
    ret


I removed:

push rdi
call atoi_digit
pop rdi


because your atoi_digit does not change rdi. Therefore, saving it currently has no effect.

We’re intentionally keeping the rest of your buggy code because the purpose is to catch the bug in GDB.

2. Assemble and link it

Run:

as -g -o debug.o debug.s
ld -o debug debug.o


The -g adds debugging information.

Check that the executable exists:

ls -l debug


You can run it normally:

./debug
echo $?


Your code will not return 123 yet because it has the null-byte bug.

3. Start GDB in TUI mode

Use:

gdb -tui ./debug


At the GDB prompt, select Intel syntax:

set disassembly-flavor intel


This matters because your source uses Intel syntax. Otherwise, GDB may display instructions in AT&T syntax.

If TUI isn’t visible, press:

Ctrl-x a


That means:

hold Ctrl,
press x,
release them,
press a.

You can also enter:

tui enable

4. Choose a useful TUI layout

Enter:

layout regs


This normally gives you:

a register window,
an assembly window,
the GDB command window.

If you want only assembly:

layout asm


Return to the register layout with:

layout regs


For this exercise, use:

layout regs


The most important registers are:

rdi — pointer to the current character
rax — return value/running total
rdx — current character/current digit
rcx — temporary running total
rsp — top of the stack
rip — address of the next instruction

Changed registers are usually highlighted in the register window.

5. Run until int3

Enter:

run


Short form:

r


The program executes:

push 0x333231
mov rdi, rsp
int3


GDB should report something similar to:

Program received signal SIGTRAP, Trace/breakpoint trap.


This is expected. int3 deliberately generated the trap.

The highlighted instruction will usually be the instruction after int3:

call atoi


That is because the processor already executed int3 before reporting the trap.

6. Understand what _start created

At this point:

push 0x333231


has put the number 0x333231 on the stack.

Because x86-64 is little-endian, the bytes appear in memory in this order:

31 32 33 00 00 00 00 00


In ASCII:

'1' '2' '3' '\0'


And this instruction:

mov rdi, rsp


makes rdi point to the first byte.

Inspect the string

Enter:

x/s $rdi


You should see something similar to:

0x7fffffffe...: "123"


The command means:

x — examine memory
/s — show it as a null-terminated string
$rdi — start at the address stored in rdi
Inspect the first character
x/c $rdi


You should see:

49 '1'


Decimal 49 is hexadecimal 0x31, the ASCII code for '1'.

Inspect the raw bytes
x/8bx $rdi


Meaning:

8 — show eight units
b — each unit is one byte
x — print in hexadecimal

You should see bytes resembling:

0x31 0x32 0x33 0x00 0x00 0x00 0x00 0x00


This proves that the string really exists in memory as:

"123\0"

7. Step into atoi

The current instruction should be:

call atoi


Use:

stepi


Short form:

si


This executes one machine instruction. Because the instruction is call atoi, you should now be inside atoi.

The highlighted instruction should be:

call atoi_digit


You can confirm the current location using:

x/i $rip


Or:

disassemble atoi

8. Understand what call did

When this happens:

call atoi


the CPU effectively performs two actions:

pushes the return address onto the stack,
jumps to atoi.

Inspect the stack:

x/4gx $rsp


The first eight-byte value is the return address. That is where ret from atoi will return.

You don’t need to memorize the address. Just understand:

call = save where to return + jump
ret  = take saved address + jump back

9. Step into atoi_digit

You are now at:

call atoi_digit


Enter:

si


Now the highlighted instruction should be:

movzx rdx, byte ptr [rdi]


Before executing it, inspect the character:

x/c $rdi


It should show:

49 '1'


Now execute:

si


The instruction:

movzx rdx, byte ptr [rdi]


loads the byte '1', which is 0x31, into rdx.

Inspect it:

p/x $rdx


Expected:

$... = 0x31


You can also print it in decimal:

p/d $rdx


Expected:

49

10. Watch ASCII become a number

The current instruction should be:

sub rdx, 0x30


Why subtract 0x30?

ASCII digits are represented as:

'0' = 0x30
'1' = 0x31
'2' = 0x32
'3' = 0x33


So:

'1' - '0'
0x31 - 0x30
= 1


Execute the subtraction:

si


Now inspect rdx:

p/d $rdx


Expected:

1


Next instruction:

mov rax, rdx


Execute it:

si


Now:

p/d $rax


should show:

1


That means atoi_digit is returning the numeric value 1 in rax.

11. Step over ret

The current instruction should be:

ret


Execute:

si


You will return to atoi, at the instruction after:

call atoi_digit


At this point:

rax = 1
rdi still points to '1'


Verify:

p/d $rax
x/c $rdi


This is the first important state:

running value = 1
current character = '1'

12. Step through the first loop iteration

Your loop begins with:

movzx rdx, byte ptr [rdi]
cmp rdx, 0
je null_byte


Step through the load:

si


Now:

p/x $rdx


should show:

0x31


Execute the comparison:

si


A useful fact: cmp does not store a result. It updates the CPU flags.

Check the Zero Flag:

p $eflags


Or inspect the full flags register:

info registers eflags


Because rdx is not zero, the Zero Flag is not set.

Execute:

si


The instruction is:

je null_byte


Since the comparison was not equal, the jump is not taken.

13. Watch the running total

Continue with:

mov rcx, rax
imul rcx, 10


Execute the move:

si


Now:

p/d $rcx


should show:

1


Execute the multiplication:

si


Now:

p/d $rcx


should show:

10


Your code has calculated:

old result × 10
1 × 10 = 10

14. Watch rdi move through the string

Before inc rdi, check:

x/c $rdi


It should show:

'1'


Execute:

si


This executes:

inc rdi


Now examine the current character:

x/c $rdi


It should show:

48 '0'


If your test string is "123", it should instead show:

50 '2'


For "123", the pointer movement is:

Initially: rdi -> '1'
After inc: rdi -> '2'
After inc: rdi -> '3'
After inc: rdi -> '\0'


To see the remainder of the string:

x/s $rdi


After moving from '1' to '2', it should show:

"23"


That is an excellent way to understand what the pointer is doing.

15. Understand push rcx

Your next instructions are:

push rcx
call atoi_digit
pop rcx


Why save rcx?

At this moment:

rcx = 10


You want to keep that value while calling atoi_digit.

Execute:

si


That runs:

push rcx


Now inspect the top of the stack:

x/gd $rsp


You should see:

10


Then step into atoi_digit:

si


Follow it instruction by instruction again:

si
si
si
si


The character '2' becomes numeric 2, and atoi_digit returns:

rax = 2


Back in atoi, execute:

si


for:

pop rcx


Now:

p/d $rcx


should show the saved value:

10


And:

p/d $rax


should show:

2


You now have:

rcx = old result × 10 = 10
rax = new digit          = 2

16. Watch 10 + 2 become 12

The next instruction is:

add rcx, rax


Execute:

si


Then:

p/d $rcx


Expected:

12


Next:

mov rax, rcx


Execute:

si


Now:

p/d $rax


Expected:

12


Your running result is now 12.

Then:

jmp loop


Execute:

si


The highlighted instruction returns to the beginning of the loop.

17. Continue until the result is 123

Repeat the same process for '3'.

The important states should be:

After processing '1': rax = 1
After processing '2': rax = 12
After processing '3': rax = 123


The formula is:

result = result * 10 + digit


For "123":

0 × 10 + 1 = 1
1 × 10 + 2 = 12
12 × 10 + 3 = 123


After processing the last '3', check:

p/d $rax


You should see:

123


But your function does not return yet. This is where you should become suspicious:

“The answer is already correct. What instruction happens next?”

Continue slowly.

18. Catch the bug

At the beginning of the next loop iteration, rdi still points to '3'.

Check:

x/c $rdi


You will see:

51 '3'


So this check:

movzx rdx, byte ptr [rdi]
cmp rdx, 0
je null_byte


does not exit because rdi still points at '3', not at the byte after '3'.

Your code then does:

mov rcx, rax
imul rcx, 10


Now:

rcx = 1230


Execute:

inc rdi


Then inspect:

x/c $rdi


You should now see:

0 '\000'


This is the most important moment.

rdi now points to the null byte, but your program has already passed its null-byte check.

The next instructions call atoi_digit:

push rcx
call atoi_digit


Step into it.

At:

movzx rdx, byte ptr [rdi]


execute the instruction and inspect:

p/d $rdx


You should see:

0


That is correct: the current byte is '\0'.

But your next instruction is:

sub rdx, 0x30


Execute it:

si


Now show rdx as a signed decimal number:

p/d $rdx


You may see the unsigned interpretation because rdx is a 64-bit register. To force signed output:

p/d (long)$rdx


Expected:

-48


You have now caught the bug:

'\0' - '0'
= 0 - 48
= -48


Your code incorrectly converted the null terminator into the “digit” -48.

19. Watch the incorrect answer form

After returning from atoi_digit, your values are approximately:

rcx = 1230
rax = -48


Then the code performs:

add rcx, rax


Therefore:

1230 + (-48) = 1182


Execute it and check:

p/d $rcx


You should see:

1182


This explains your longer input too:

2012437022 × 10 - 48
= 20124370220 - 48
= 20124370172


That is exactly the incorrect result you observed.

You did not have to guess. GDB showed you:

rax reached the correct answer,
the loop continued once too many times,
rdi moved to '\0',
atoi_digit converted '\0' into -48,
-48 was added to the multiplied result.

That is real debugging.

20. Fix the location of the check

The current structure checks [rdi] before incrementing rdi, but it calls atoi_digit after incrementing it.

The check therefore needs to happen after inc rdi and before the call:

atoi:
    call atoi_digit

loop:
    mov rcx, rax
    imul rcx, 10

    inc rdi

    cmp byte ptr [rdi], 0
    je done

    push rcx
    call atoi_digit
    pop rcx

    add rcx, rax
    mov rax, rcx
    jmp loop

done:
    ret


However, this version has another subtle problem: when it sees '\0', rax contains the old result, which is good, but rcx contains the multiplied value that should not be returned. Since rax was not replaced by rcx yet, returning rax works.

A much simpler version is:

atoi:
    xor eax, eax

loop:
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0
    je done

    sub rdx, 0x30

    imul rax, rax, 10
    add rax, rdx

    inc rdi
    jmp loop

done:
    ret


This directly implements:

while current byte is not zero:
    digit = current byte - '0'
    result = result * 10 + digit
    move to next byte


For learning purposes, debug both versions and watch the simpler one produce:

rax: 0 → 1 → 12 → 123
rdi: '1' → '2' → '3' → '\0'

21. Restart after changing the program

Quit GDB:

quit


Reassemble and relink:

as -g -o debug.o debug.s
ld -o debug debug.o


Start GDB again:

gdb -tui ./debug


Then:

set disassembly-flavor intel
layout regs
run


You can also rebuild while GDB remains open in another terminal, then use:

file ./debug
run


But while learning, restarting GDB is simpler.

22. Useful TUI controls
Refresh a broken screen

Sometimes command output damages the TUI display. Press:

Ctrl-l


That redraws the screen.

Enable or disable TUI
Ctrl-x a

Change active TUI window
Ctrl-x o


This is useful if you want to scroll the assembly or register window.

Scroll an active TUI window

Use:

Page Up
Page Down


If typing commands starts moving or scrolling a window unexpectedly, press:

Ctrl-x o


until the command window is active again.

23. Important GDB commands to memorize

You don’t need to learn all of GDB. Start with these:

run


Start the program.

stepi


Execute one machine instruction, entering calls.

nexti


Execute one machine instruction, but treat a function call as one step.

layout regs


Show registers and assembly.

x/i $rip


Show the current instruction.

x/c $rdi


Show the character pointed to by rdi.

x/s $rdi


Show the string beginning at rdi.

x/8bx $rdi


Show eight raw bytes beginning at rdi.

p/d $rax


Print rax in decimal.

p/x $rax


Print rax in hexadecimal.

p/d (long)$rdx


Print rdx as a signed 64-bit value.

info registers


Show all general-purpose registers.

disassemble atoi


Show atoi’s instructions.

24. stepi versus nexti

Suppose the current instruction is:

call atoi_digit


If you enter:

stepi


GDB enters atoi_digit, allowing you to inspect every instruction.

If you enter:

nexti


GDB runs the entire call and stops at the next instruction in atoi.

Use:

stepi when debugging inside atoi_digit,
nexti once you trust atoi_digit and only want to debug atoi.

Short forms:

si
ni

25. One warning about echo $?

Linux terminal exit statuses contain only the low eight bits, so their normal visible range is:

0–255


For "123":

./debug
echo $?


shows:

123


But for "1000", the shell will not show 1000. It will show:

1000 modulo 256 = 232


That does not necessarily mean atoi returned the wrong value.

For large results, inspect rax in GDB just before:

mov rdi, rax


For example, break after atoi returns:

break *_start+7


Exact offsets can vary, so a safer method is to place another int3:

call atoi
int3

mov rdi, rax
mov rax, 60
syscall


Then run and inspect:

p/d $rax


That will show the full 64-bit result.

Your debugging mindset

Every loop iteration, ask only these four questions:

What character does rdi point to?

x/c $rdi


What is the running total?

p/d $rax


What digit did I just convert?

p/d $rdx


Which instruction changes the value incorrectly?

stepi


The aim is not initially to understand the whole function at once. The aim is to locate the first moment when reality differs from your expectation.

In this program, that moment is:

Expected: detect '\0' and return 123
Actual:   subtract 0x30 from '\0', producing -48


Once you identify the first wrong state, the cause is usually only one or two instructions above it.

##### Negative Numbers
```
.intel_syntax noprefix
.global atoi_digit
.global atoi
atoi_digit:
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x2d
    je neg_num_check
    sub rdx, 0x30
    mov rax, rdx
    ret
    neg_num_check:
        inc rdi
        mov r8, 1 # 1 if negative
        movzx rdx, byte ptr [rdi]
        sub rdx, 0x30
        mov rax, rdx
        ret
atoi:
    call atoi_digit
    loop:
    mov rcx, rax
    imul rcx, 10
    inc rdi
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x0
    je null_byte
    push rcx
    call atoi_digit
    pop rcx
    add rcx, rax
    mov rax, rcx
    jmp loop
null_byte:
    cmp r8, 1
    je neg_rax
    ret
neg_rax:
    neg rax
    ret
```

##### Where the Number Ends
```
.intel_syntax noprefix
.global atoi_digit
.global atoi
atoi_digit:
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x2d
    je neg_num_check
    sub rdx, '0'
    mov rax, rdx
    ret
    neg_num_check:
        inc rdi
        mov r8, 1 # 1 if negative
        movzx rdx, byte ptr [rdi]
        sub rdx, 0x30
        mov rax, rdx
        ret
atoi:
    xor r8, r8
    call atoi_digit
    loop:
    inc rdi
    movzx rdx, byte ptr [rdi]
    sub rdx, '0'
    cmp rdx, 9
    ja done
    mov rcx, rax
    imul rcx, 10
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x0
    je null_byte
    call atoi_digit
    add rcx, rax
    mov rax, rcx
    jmp loop
null_byte:
    cmp r8, 1
    je neg_rax
    ret
done:
    cmp r8, 1
    je neg_rax
    ret
neg_rax:
    neg rax
    ret

```
Debugged completely by myself. I know the code isn't the cleanest...

##### A Whole Program
Should be simple.
```
.intel_syntax noprefix
.global _start
.global atoi_digit
.global atoi

_start:
    mov rdi, [rsp+16]
    call atoi
    mov rdi, rax
    mov rax, 60
    syscall

atoi_digit:
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x2d
    je neg_num_check
    sub rdx, '0'
    mov rax, rdx
    ret
    neg_num_check:
        inc rdi
        mov r8, 1 # 1 if negative
        movzx rdx, byte ptr [rdi]
        sub rdx, 0x30
        mov rax, rdx
        ret
atoi:
    xor r8, r8
    call atoi_digit
    loop:
    inc rdi
    movzx rdx, byte ptr [rdi]
    sub rdx, '0'
    cmp rdx, 9
    ja done
    mov rcx, rax
    imul rcx, 10
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x0
    je null_byte
    call atoi_digit
    add rcx, rax
    mov rax, rcx
    jmp loop
null_byte:
    cmp r8, 1
    je neg_rax
    ret
done:
    cmp r8, 1
    je neg_rax
    ret
neg_rax:
    neg rax
    ret

```

##### A Single Digit, Back to Text
```
.intel_syntax noprefix
.global itoa_digit
itoa_digit:
    mov rdx, rdi
    add rdx, 0x30
    mov rax, rdx
    ret

```

##### Divide and Reminder
```
.intel_syntax noprefix
.global itoa_digit
.global itoa
itoa_digit:
    mov rdx, rdi
    add rdx, 0x30
    mov rax, rdx
    ret

itoa:
    mov rax, rdi
    xor rdx, rdx
    mov rcx, 10
    div rcx
    mov rdi, rax
    push rdx
    push rsi
    call itoa_digit
    pop rsi
    pop rdx
    mov rdi, rdx
    push rax
    push rsi
    call itoa_digit
    pop rsi
    mov rdx, rax
    pop rax
    mov [rsi], al
    mov [rsi+1], dl
    mov rax, 2
    ret

```
I debugged this for like 10 minutes without realising i was rebuilding debug and not DAR.so
Other than that I was writing to output instead of just writing to the buffer. Debugged by myself.

##### Drop the Leading Zero
```
.intel_syntax noprefix
.global itoa_digit
.global itoa
itoa_digit:
    mov rdx, rdi
    add rdx, 0x30
    mov rax, rdx
    ret

itoa:
    mov rax, rdi
    xor rdx, rdx
    mov rcx, 10
    div rcx
    cmp rax, 0
    je zero
    mov rdi, rax
    push rdx
    push rsi
    call itoa_digit
    pop rsi
    pop rdx
    mov rdi, rdx
    push rax
    push rsi
    call itoa_digit
    pop rsi
    mov rdx, rax
    pop rax
    mov [rsi], al
    mov [rsi+1], dl
    mov rax, 2
    ret
     zero:
        mov rdi, rdx
        call itoa_digit
        mov [rsi], al
        mov rax, 1
        ret

```

Pretty ok. I just got to fix the ret 1 or 2 and do loops instead.

##### Integer to String

```
.intel_syntax noprefix
.global itoa_digit
.global itoa

itoa_digit:
    mov rdx, rdi
    add rdx, 0x30
    mov rax, rdx
    ret

itoa:
    mov r9, 0
    mov r10, 0
    mov rax, rdi
    xor rdx, rdx
    mov rcx, 10
    div rcx
    cmp rax, 0
    je zero
    peel_digits:
        inc r9
        push rdx
        cmp rax, 0
        je done_peel
        xor rdx, rdx
        mov rcx, 10
        div rcx
        jmp peel_digits
    done_peel:
        cmp r10, r9
        je done
        pop rdi
        call itoa_digit
        mov [rsi+r10], al
        inc r10
        jmp done_peel
    done:
        mov rax, r9
        ret
    zero:
        or  rax, rdx
        jz  both_zero
        mov rdi, rdx
        call itoa_digit
        mov [rsi], al
        mov rax, 1
        ret
    both_zero:
        mov rdi, rdx
        call itoa_digit
        mov [rsi], al
        mov rax, 1
        ret

```

##### Negative Numbers, Back to Text
```
.intel_syntax noprefix
.global itoa_digit
.global itoa
itoa_digit:
    mov rax, rdi
    add rax, '0'
    ret

itoa:
    mov rax, rdi
    xor r8, r8
    xor r9, r9

    test rax, rax
    jns .magnitude_ready

.is_negative:
    mov byte ptr [rsi], '-'
    inc rsi
    inc r8
    neg rax

.magnitude_ready:
    test rax, rax
    jnz .peel_digits
    mov byte ptr [rsi], '0'
    inc r8
    mov rax, r8
    ret

.peel_digits:
    xor edx, edx
    mov ecx, 10
    div rcx

    push rdx
    inc r9

    test rax, rax
    jnz .peel_digits

.write_digits:
    pop rdi
    call itoa_digit

    mov byte ptr [rsi], al
    inc rsi
    inc r8

    dec r9
    jnz .write_digits

.done:
    mov rax, r8
    ret
    
```

##### Sum Them All
This seems ok?
Actually, no.
I need to load the value from argv\[1] to argv\[argc-1].
I need to know how long is each number, until a null byte.
Then, load each number to "atoi", and store the sum in a register.
In the end, I need to turn it back to ascii with itoa and write() it.

```
.intel_syntax noprefix
.global itoa_digit
.global itoa
.global atoi_digit
.global atoi
.global _start

.section .bss
buf: .skip 32

.section .text

_start:
    xor r11, r11
    mov rbx, [rsp]
    lea r12, [rsp + 16]

.loop:
    cmp rbx, 1
    jle .done

    mov rdi, [r12]
    call atoi

    add r11, rax
    add r12, 8
    dec rbx
    jmp .loop

.done:
    mov rdi, r11
    lea rsi, [rip + buf]
    call itoa

    mov rdx, rax
    lea rsi, [rip + buf]

    mov rax, 1
    mov rdi, 1
    syscall

    mov rax, 60
    xor rdi, rdi
    syscall

itoa_digit:
    mov rax, rdi
    add rax, '0'
    ret

itoa:
    mov rax, rdi
    xor r8, r8
    xor r9, r9

    test rax, rax
    jns .magnitude_ready

.is_negative:
    mov byte ptr [rsi], '-'
    inc rsi
    inc r8
    neg rax

.magnitude_ready:
    test rax, rax
    jnz .peel_digits
    mov byte ptr [rsi], '0'
    inc r8
    mov rax, r8
    ret

.peel_digits:
    xor rdx, rdx
    mov ecx, 10
    div rcx

    push rdx
    inc r9

    test rax, rax
    jnz .peel_digits

.write_digits:
    pop rdi
    call itoa_digit

    mov byte ptr [rsi], al
    inc rsi
    inc r8

    dec r9
    jnz .write_digits

.done_itoa:
    mov byte ptr [rsi], 0
    mov rax, r8
    ret

atoi_digit:
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x2d
    je neg_num_check
    sub rdx, '0'
    mov rax, rdx
    ret
    neg_num_check:
        inc rdi
        mov r8, 1 # 1 if negative
        movzx rdx, byte ptr [rdi]
        sub rdx, 0x30
        mov rax, rdx
        ret
atoi:
    xor r8, r8
    call atoi_digit
    loop:
    inc rdi
    movzx rdx, byte ptr [rdi]
    sub rdx, '0'
    cmp rdx, 9
    ja done
    mov rcx, rax
    imul rcx, 10
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x0
    je null_byte
    call atoi_digit
    add rcx, rax
    mov rax, rcx
    jmp loop
null_byte:
    cmp r8, 1
    je neg_rax
    ret
done:
    cmp r8, 1
    je neg_rax
    ret
neg_rax:
    neg rax
    ret


```
I dont want to talk about it. I understand the logic, but I coulnd't write it by myself. Yes, I AM DUMB!

##### Addition
So from what I understand, this doesnt support multiple operators. X+Y and thats it.
In this case, it's more simple.
```
.intel_syntax noprefix
.global itoa_digit
.global itoa
.global atoi_digit
.global atoi
.global _start


_start:
    mov rcx, 0
    mov rdi, [rsp+24]
    cmp BYTE PTR [rdi], '+'
    jnz unknown_operator
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall
    unknown_operator:
        mov rdi, 1
        mov rax, 60
        syscall


itoa_digit:
    mov rax, rdi
    add rax, '0'
    ret

itoa:
    mov rax, rdi
    xor r8, r8
    xor r9, r9

    test rax, rax
    jns .magnitude_ready

.is_negative:
    mov byte ptr [rsi], '-'
    inc rsi
    inc r8
    neg rax

.magnitude_ready:
    test rax, rax
    jnz .peel_digits
    mov byte ptr [rsi], '0'
    inc r8
    mov rax, r8
    ret

.peel_digits:
    xor rdx, rdx
    mov ecx, 10
    div rcx

    push rdx
    inc r9

    test rax, rax
    jnz .peel_digits

.write_digits:
    pop rdi
    call itoa_digit

    mov byte ptr [rsi], al
    inc rsi
    inc r8

    dec r9
    jnz .write_digits

.done_itoa:
    mov byte ptr [rsi], 0
    mov rax, r8
    ret

atoi_digit:
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x2d
    je neg_num_check
    sub rdx, '0'
    mov rax, rdx
    ret
    neg_num_check:
        inc rdi
        mov r8, 1 # 1 if negative
        movzx rdx, byte ptr [rdi]
        sub rdx, 0x30
        mov rax, rdx
        ret
atoi:
    xor r8, r8
    call atoi_digit
    loop:
    inc rdi
    movzx rdx, byte ptr [rdi]
    sub rdx, '0'
    cmp rdx, 9
    ja done
    mov rcx, rax
    imul rcx, 10
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x0
    je null_byte
    call atoi_digit
    add rcx, rax
    mov rax, rcx
    jmp loop
null_byte:
    cmp r8, 1
    je neg_rax
    ret
done:
    cmp r8, 1
    je neg_rax
    ret
neg_rax:
    neg rax
    ret

```

##### Subtraction
```
.intel_syntax noprefix
.global itoa_digit
.global itoa
.global atoi_digit
.global atoi
.global _start


_start:
    mov rcx, 0
    mov rdi, [rsp+24]
    cmp BYTE PTR [rdi], '+'
    je addition
    cmp BYTE PTR [rdi], '-'
    je subtraction
    jnz unknown_operator
    addition:
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall
    subtraction:
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    sub rcx, rax    # subtraction!
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall
    unknown_operator:
        mov rdi, 1
        mov rax, 60
        syscall


itoa_digit:
    mov rax, rdi
    add rax, '0'
    ret

itoa:
    mov rax, rdi
    xor r8, r8
    xor r9, r9

    test rax, rax
    jns .magnitude_ready

.is_negative:
    mov byte ptr [rsi], '-'
    inc rsi
    inc r8
    neg rax

.magnitude_ready:
    test rax, rax
    jnz .peel_digits
    mov byte ptr [rsi], '0'
    inc r8
    mov rax, r8
    ret

.peel_digits:
    xor rdx, rdx
    mov ecx, 10
    div rcx

    push rdx
    inc r9

    test rax, rax
    jnz .peel_digits

.write_digits:
    pop rdi
    call itoa_digit

    mov byte ptr [rsi], al
    inc rsi
    inc r8

    dec r9
    jnz .write_digits

.done_itoa:
    mov byte ptr [rsi], 0
    mov rax, r8
    ret

atoi_digit:
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x2d
    je neg_num_check
    sub rdx, '0'
    mov rax, rdx
    ret
    neg_num_check:
        inc rdi
        mov r8, 1 # 1 if negative
        movzx rdx, byte ptr [rdi]
        sub rdx, 0x30
        mov rax, rdx
        ret
atoi:
    xor r8, r8
    call atoi_digit
    loop:
    inc rdi
    movzx rdx, byte ptr [rdi]
    sub rdx, '0'
    cmp rdx, 9
    ja done
    mov rcx, rax
    imul rcx, 10
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x0
    je null_byte
    call atoi_digit
    add rcx, rax
    mov rax, rcx
    jmp loop
null_byte:
    cmp r8, 1
    je neg_rax
    ret
done:
    cmp r8, 1
    je neg_rax
    ret
neg_rax:
    neg rax
    ret


```

##### Multiplication
```
.intel_syntax noprefix
.global itoa_digit
.global itoa
.global atoi_digit
.global atoi
.global _start


_start:
    mov rcx, 0
    mov rdi, [rsp+24]
    cmp BYTE PTR [rdi], '+'
    je addition
    cmp BYTE PTR [rdi], '-'
    je subtraction
    cmp BYTE PTR [rdi], '*'
    je multiplication
    jnz unknown_operator

    addition:
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall

    subtraction:
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    sub rcx, rax    # subtraction!
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall

    multiplication:
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    imul rcx, rax    # multiplication!
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall

    unknown_operator:
        mov rdi, 1
        mov rax, 60
        syscall


itoa_digit:
    mov rax, rdi
    add rax, '0'
    ret

itoa:
    mov rax, rdi
    xor r8, r8
    xor r9, r9

    test rax, rax
    jns .magnitude_ready

.is_negative:
    mov byte ptr [rsi], '-'
    inc rsi
    inc r8
    neg rax

.magnitude_ready:
    test rax, rax
    jnz .peel_digits
    mov byte ptr [rsi], '0'
    inc r8
    mov rax, r8
    ret

.peel_digits:
    xor rdx, rdx
    mov ecx, 10
    div rcx

    push rdx
    inc r9

    test rax, rax
    jnz .peel_digits

.write_digits:
    pop rdi
    call itoa_digit

    mov byte ptr [rsi], al
    inc rsi
    inc r8

    dec r9
    jnz .write_digits

.done_itoa:
    mov byte ptr [rsi], 0
    mov rax, r8
    ret

atoi_digit:
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x2d
    je neg_num_check
    sub rdx, '0'
    mov rax, rdx
    ret
    neg_num_check:
        inc rdi
        mov r8, 1 # 1 if negative
        movzx rdx, byte ptr [rdi]
        sub rdx, 0x30
        mov rax, rdx
        ret
atoi:
    xor r8, r8
    call atoi_digit
    loop:
    inc rdi
    movzx rdx, byte ptr [rdi]
    sub rdx, '0'
    cmp rdx, 9
    ja done
    mov rcx, rax
    imul rcx, 10
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x0
    je null_byte
    call atoi_digit
    add rcx, rax
    mov rax, rcx
    jmp loop
null_byte:
    cmp r8, 1
    je neg_rax
    ret
done:
    cmp r8, 1
    je neg_rax
    ret
neg_rax:
    neg rax
    ret

```

##### Bitwise Operators
```
.intel_syntax noprefix
.global itoa_digit
.global itoa
.global atoi_digit
.global atoi
.global _start


_start:
    mov rcx, 0
    mov rdi, [rsp+24]

    cmp BYTE PTR [rdi], '+'
    je .addition
    cmp BYTE PTR [rdi], '-'
    je .subtraction
    cmp BYTE PTR [rdi], '*'
    je .multiplication
    cmp BYTE PTR [rdi], '^'
    je .xor
    cmp BYTE PTR [rdi], '|'
    je .or
    cmp BYTE PTR [rdi], '&'
    je .and

    jnz .unknown_operator

    .addition:
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall

    .subtraction:
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    sub rcx, rax    # subtraction!
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall

    .multiplication:
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    imul rcx, rax    # multiplication!
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall

    .xor:
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    xor rcx, rax    # xor!
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall

    .or:
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    or rcx, rax    # or!
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall

    .and:
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    and rcx, rax    # and!
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall     

    .unknown_operator:
        mov rdi, 1
        mov rax, 60
        syscall


itoa_digit:
    mov rax, rdi
    add rax, '0'
    ret

itoa:
    mov rax, rdi
    xor r8, r8
    xor r9, r9

    test rax, rax
    jns .magnitude_ready

.is_negative:
    mov byte ptr [rsi], '-'
    inc rsi
    inc r8
    neg rax

.magnitude_ready:
    test rax, rax
    jnz .peel_digits
    mov byte ptr [rsi], '0'
    inc r8
    mov rax, r8
    ret

.peel_digits:
    xor rdx, rdx
    mov ecx, 10
    div rcx

    push rdx
    inc r9

    test rax, rax
    jnz .peel_digits

.write_digits:
    pop rdi
    call itoa_digit

    mov byte ptr [rsi], al
    inc rsi
    inc r8

    dec r9
    jnz .write_digits

.done_itoa:
    mov byte ptr [rsi], 0
    mov rax, r8
    ret

atoi_digit:
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x2d
    je neg_num_check
    sub rdx, '0'
    mov rax, rdx
    ret
    neg_num_check:
        inc rdi
        mov r8, 1 # 1 if negative
        movzx rdx, byte ptr [rdi]
        sub rdx, 0x30
        mov rax, rdx
        ret
atoi:
    xor r8, r8
    call atoi_digit
    loop:
    inc rdi
    movzx rdx, byte ptr [rdi]
    sub rdx, '0'
    cmp rdx, 9
    ja done
    mov rcx, rax
    imul rcx, 10
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x0
    je null_byte
    call atoi_digit
    add rcx, rax
    mov rax, rcx
    jmp loop
null_byte:
    cmp r8, 1
    je neg_rax
    ret
done:
    cmp r8, 1
    je neg_rax
    ret
neg_rax:
    neg rax
    ret

```

##### Unary Operators
```
.intel_syntax noprefix
.global itoa_digit
.global itoa
.global atoi_digit
.global atoi
.global _start


_start:
    mov rcx, 0
    mov rdx, [rsp]
    cmp rdx, 4
    je binary_dispatch
    cmp rdx, 3
    je unary_dispatch
    binary_dispatch:
    mov rdi, [rsp+24]

    cmp BYTE PTR [rdi], '+'
    je .addition
    cmp BYTE PTR [rdi], '-'
    je .subtraction
    cmp BYTE PTR [rdi], '*'
    je .multiplication
    cmp BYTE PTR [rdi], '^'
    je .xor
    cmp BYTE PTR [rdi], '|'
    je .or
    cmp BYTE PTR [rdi], '&'
    je .and

    jnz .unknown_operator

    .addition:
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall

    .subtraction:
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    sub rcx, rax    # subtraction!
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall

    .multiplication:
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    imul rcx, rax    # multiplication!
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall

    .xor:
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    xor rcx, rax    # xor!
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall

    .or:
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    or rcx, rax    # or!
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall

    .and:
    mov rdi, [rsp+16]
    push rcx
    call atoi
    pop rcx
    add rcx, rax
    mov rdi, [rsp+32]
    push rcx
    call atoi
    pop rcx
    and rcx, rax    # and!
    mov rdi, rcx
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall

    unary_dispatch:
    mov rdi, [rsp+16]
    cmp BYTE PTR [rdi], '-'
    je .negates
    cmp BYTE PTR [rdi], '~'
    je .not

    jnz .unknown_operator
    
    
    .negates:
    mov rdi, [rsp+24]
    call atoi
    neg rax    # negates!
    mov rdi, rax
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall

    .not:
    mov rdi, [rsp+24]
    call atoi
    not rax    # negates!
    mov rdi, rax
    sub rsp, 0x20
    mov rsi, rsp
    call itoa
    mov rdx, rax
    mov rsi, rsp
    mov byte ptr [rsi + rdx], 10    # '\n'
    inc rdx
    mov rdi, 1
    mov rax, 1
    syscall
    mov rdi, 0
    mov rax, 60
    syscall


    .unknown_operator:
        mov rdi, 1
        mov rax, 60
        syscall


itoa_digit:
    mov rax, rdi
    add rax, '0'
    ret

itoa:
    mov rax, rdi
    xor r8, r8
    xor r9, r9

    test rax, rax
    jns .magnitude_ready

.is_negative:
    mov byte ptr [rsi], '-'
    inc rsi
    inc r8
    neg rax

.magnitude_ready:
    test rax, rax
    jnz .peel_digits
    mov byte ptr [rsi], '0'
    inc r8
    mov rax, r8
    ret

.peel_digits:
    xor rdx, rdx
    mov ecx, 10
    div rcx

    push rdx
    inc r9

    test rax, rax
    jnz .peel_digits

.write_digits:
    pop rdi
    call itoa_digit

    mov byte ptr [rsi], al
    inc rsi
    inc r8

    dec r9
    jnz .write_digits

.done_itoa:
    mov byte ptr [rsi], 0
    mov rax, r8
    ret

atoi_digit:
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x2d
    je neg_num_check
    sub rdx, '0'
    mov rax, rdx
    ret
    neg_num_check:
        inc rdi
        mov r8, 1 # 1 if negative
        movzx rdx, byte ptr [rdi]
        sub rdx, 0x30
        mov rax, rdx
        ret
atoi:
    xor r8, r8
    call atoi_digit
    loop:
    inc rdi
    movzx rdx, byte ptr [rdi]
    sub rdx, '0'
    cmp rdx, 9
    ja done
    mov rcx, rax
    imul rcx, 10
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x0
    je null_byte
    call atoi_digit
    add rcx, rax
    mov rax, rcx
    jmp loop
null_byte:
    cmp r8, 1
    je neg_rax
    ret
done:
    cmp r8, 1
    je neg_rax
    ret
neg_rax:
    neg rax
    ret

```

DONE CALC!

PRINTF
4.9.26 16:49

##### Literal Output
```
.intel_syntax noprefix
.global _start

_start:
    mov rdx, 0
    mov rdi, [rsp+16]
    count_loop: // Code to calculate size of flag and store it in rdx
        cmp BYTE PTR [rdi + rdx], 0
        je write_data
        inc rdx
        jmp count_loop
    write_data:
        mov rdi, 1
        mov rsi, [rsp+16]
        mov rax, 1
        syscall
        mov rdi, 0
        mov rax, 60
        syscall
```

ALSO:
mov - when the data is given by a pointer
lea - when there is actual data at that address. for the write_data part.

##### Newline Escapes
```
.intel_syntax noprefix
.global _start

_start:
    mov rdi, [rsp+16]

    sub rsp, 0x100
    mov rsi, rsp

    xor rdx, rdx            # input index
    xor rcx, rcx            # output index

filter_loop:
    cmp BYTE PTR [rdi + rdx], 0
    je write_data

    cmp BYTE PTR [rdi + rdx], 0x5c     # '\'
    je slash

    # normal character
    mov al, BYTE PTR [rdi + rdx]
    mov BYTE PTR [rsi + rcx], al
    inc rdx
    inc rcx
    jmp filter_loop

slash:
    inc rdx
    cmp BYTE PTR [rdi + rdx], 'n'
    je new_line

    # regular backslash
    mov BYTE PTR [rsi + rcx], 0x5c
    inc rcx
    jmp filter_loop

new_line:
    mov BYTE PTR [rsi + rcx], 0x0a
    inc rdx
    inc rcx
    jmp filter_loop

write_data:
    mov rdx, rcx
    mov rdi, 1
    mov rax, 1
    syscall

    mov rdi, 0
    mov rax, 60
    syscall
```

I definantly used an AI to complete this level. I wanted to copy rdi to rax byte by byte, but to filter out the \n and replace with 0x0a. I couldn't figure out a way to do it by myself, so I used AI for the syntax.

##### Escaped Syntax
In this challenge, we need to filter two \ to one and the same with %
```
.intel_syntax noprefix
.global _start

_start:
    mov rdi, [rsp+16]

    sub rsp, 0x100
    mov rsi, rsp

    xor rdx, rdx            # input index
    xor rcx, rcx            # output index

filter_loop:
    cmp BYTE PTR [rdi + rdx], 0
    je write_data

    cmp BYTE PTR [rdi + rdx], 0x5c     # '\'
    je slash
    cmp BYTE PTR [rdi + rdx], 0x25     # '%'
    je percent

    # normal character
    mov al, BYTE PTR [rdi + rdx]
    mov BYTE PTR [rsi + rcx], al
    inc rdx
    inc rcx
    jmp filter_loop

slash:
    inc rdx
    cmp BYTE PTR [rdi + rdx], 'n'
    je new_line
    cmp BYTE PTR [rdi + rdx], 0x5c
    je double_slash

    # regular backslash
    mov BYTE PTR [rsi + rcx], 0x5c
    inc rcx
    jmp filter_loop

percent:
    inc rdx
    cmp BYTE PTR [rdi + rdx], '%'
    je double_percent

    # regular percent
    mov BYTE PTR [rsi + rcx], 0x25
    inc rcx
    jmp filter_loop

new_line:
    mov BYTE PTR [rsi + rcx], 0x0a
    inc rdx
    inc rcx
    jmp filter_loop

double_slash:
    mov BYTE PTR [rsi + rcx], 0x5c
    inc rdx
    inc rcx
    jmp filter_loop
    
double_percent:
    mov BYTE PTR [rsi + rcx], 0x25
    inc rdx
    inc rcx
    jmp filter_loop

write_data:
    mov rdx, rcx
    mov rdi, 1
    mov rax, 1
    syscall

    mov rdi, 0
    mov rax, 60
    syscall

```

##### Decimal Markers
I need to build a feature so the if the scanner reads %d, it will scan the next argv and put it there. like:
argv1: "value=%d"
argv2: "-42"

It says to use the atoi and itoa I made.

```
.intel_syntax noprefix
.global itoa_digit
.global itoa
.global atoi_digit
.global atoi
.global _start

_start:
    mov r14, rsp           # original rsp

    mov rdi, [r14+16]      # argv[1]
    sub rsp, 0x100
    mov rsi, rsp            # output buffer

    xor rdx, rdx            # input index
    xor rcx, rcx            # output index

filter_loop:
    cmp BYTE PTR [rdi + rdx], 0
    je write_data

    cmp BYTE PTR [rdi + rdx], 0x5c     # '\'
    je slash
    cmp BYTE PTR [rdi + rdx], 0x25     # '%'
    je percent

    # normal character
    mov al, BYTE PTR [rdi + rdx]
    mov BYTE PTR [rsi + rcx], al
    inc rdx
    inc rcx
    jmp filter_loop

slash:
    inc rdx
    cmp BYTE PTR [rdi + rdx], 'n'
    je new_line
    cmp BYTE PTR [rdi + rdx], 0x5c
    je double_slash

    # regular backslash
    mov BYTE PTR [rsi + rcx], 0x5c
    inc rcx
    jmp filter_loop

percent:
    inc rdx
    cmp BYTE PTR [rdi + rdx], '%'
    je double_percent
    cmp BYTE PTR [rdi + rdx], 'd'
    je decimal_marker

    # regular percent
    mov BYTE PTR [rsi + rcx], 0x25
    inc rcx
    jmp filter_loop

new_line:
    mov BYTE PTR [rsi + rcx], 0x0a
    inc rdx
    inc rcx
    jmp filter_loop

double_slash:
    mov BYTE PTR [rsi + rcx], 0x5c
    inc rdx
    inc rcx
    jmp filter_loop
    
double_percent:
    mov BYTE PTR [rsi + rcx], 0x25
    inc rdx
    inc rcx
    jmp filter_loop

decimal_marker:
    push rdi
    push rdx
    push rcx
    push rsi

    mov rdi, [r14+24]       # argv[2]
    call atoi

    mov rdi, rax

    mov rcx, [rsp+8]        # restore output index
    mov rsi, [rsp]          # restore output buffer
    add rsi, rcx

    call itoa               # rax = number of bytes written
    mov r8, rax             # save length

    pop rsi
    pop rcx
    pop rdx
    pop rdi

    add rcx, r8             # advance output index
    inc rdx                 # skip the 'd'
    jmp filter_loop

write_data:
    mov rdx, rcx
    mov rdi, 1
    mov rax, 1
    syscall

    mov rdi, 0
    mov rax, 60
    syscall



itoa_digit:
    mov rax, rdi
    add rax, '0'
    ret

itoa:
    mov rax, rdi
    xor r8, r8
    xor r9, r9

    test rax, rax
    jns .magnitude_ready

.is_negative:
    mov byte ptr [rsi], '-'
    inc rsi
    inc r8
    neg rax

.magnitude_ready:
    test rax, rax
    jnz .peel_digits
    mov byte ptr [rsi], '0'
    inc r8
    mov rax, r8
    ret

.peel_digits:
    xor rdx, rdx
    mov ecx, 10
    div rcx

    push rdx
    inc r9

    test rax, rax
    jnz .peel_digits

.write_digits:
    pop rdi
    call itoa_digit

    mov byte ptr [rsi], al
    inc rsi
    inc r8

    dec r9
    jnz .write_digits

.done_itoa:
    mov byte ptr [rsi], 0
    mov rax, r8
    ret

atoi_digit:
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x2d
    je neg_num_check
    sub rdx, '0'
    mov rax, rdx
    ret
    neg_num_check:
        inc rdi
        mov r8, 1 # 1 if negative
        movzx rdx, byte ptr [rdi]
        sub rdx, 0x30
        mov rax, rdx
        ret
atoi:
    xor r8, r8
    call atoi_digit
    loop:
    inc rdi
    movzx rdx, byte ptr [rdi]
    sub rdx, '0'
    cmp rdx, 9
    ja done
    mov rcx, rax
    imul rcx, 10
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x0
    je null_byte
    call atoi_digit
    add rcx, rax
    mov rax, rcx
    jmp loop
null_byte:
    cmp r8, 1
    je neg_rax
    ret
done:
    cmp r8, 1
    je neg_rax
    ret
neg_rax:
    neg rax
    ret

```

##### Multiple Decimal Markers
```
.intel_syntax noprefix
.global itoa_digit
.global itoa
.global atoi_digit
.global atoi
.global _start

_start:
    mov r14, rsp           # original rsp

    mov rdi, [r14+16]      # argv[1]
    sub rsp, 0x100
    mov rsi, rsp            # output buffer
    mov r15, 24

    xor rdx, rdx            # input index
    xor rcx, rcx            # output index

filter_loop:
    cmp BYTE PTR [rdi + rdx], 0
    je write_data

    cmp BYTE PTR [rdi + rdx], 0x5c     # '\'
    je slash
    cmp BYTE PTR [rdi + rdx], 0x25     # '%'
    je percent

    # normal character
    mov al, BYTE PTR [rdi + rdx]
    mov BYTE PTR [rsi + rcx], al
    inc rdx
    inc rcx
    jmp filter_loop

slash:
    inc rdx
    cmp BYTE PTR [rdi + rdx], 'n'
    je new_line
    cmp BYTE PTR [rdi + rdx], 0x5c
    je double_slash

    # regular backslash
    mov BYTE PTR [rsi + rcx], 0x5c
    inc rcx
    jmp filter_loop

percent:
    inc rdx
    cmp BYTE PTR [rdi + rdx], '%'
    je double_percent
    cmp BYTE PTR [rdi + rdx], 'd'
    je decimal_marker

    # regular percent
    mov BYTE PTR [rsi + rcx], 0x25
    inc rcx
    jmp filter_loop

new_line:
    mov BYTE PTR [rsi + rcx], 0x0a
    inc rdx
    inc rcx
    jmp filter_loop

double_slash:
    mov BYTE PTR [rsi + rcx], 0x5c
    inc rdx
    inc rcx
    jmp filter_loop
    
double_percent:
    mov BYTE PTR [rsi + rcx], 0x25
    inc rdx
    inc rcx
    jmp filter_loop

decimal_marker:
    push rdi
    push rdx
    push rcx
    push rsi

    mov rdi, [r14+r15]      # current %d argument
    add r15, 8              # advance to next argument

    call atoi

    mov rdi, rax

    mov rcx, [rsp+8]        # output index
    mov rsi, [rsp]          # output buffer
    add rsi, rcx

    call itoa
    mov r8, rax             # length

    pop rsi
    pop rcx
    pop rdx
    pop rdi

    add rcx, r8             # output index += converted length
    inc rdx                  # skip 'd'
    jmp filter_loop

write_data:
    mov rdx, rcx
    mov rdi, 1
    mov rax, 1
    syscall

    mov rdi, 0
    mov rax, 60
    syscall



itoa_digit:
    mov rax, rdi
    add rax, '0'
    ret

itoa:
    mov rax, rdi
    xor r8, r8
    xor r9, r9

    test rax, rax
    jns .magnitude_ready

.is_negative:
    mov byte ptr [rsi], '-'
    inc rsi
    inc r8
    neg rax

.magnitude_ready:
    test rax, rax
    jnz .peel_digits
    mov byte ptr [rsi], '0'
    inc r8
    mov rax, r8
    ret

.peel_digits:
    xor rdx, rdx
    mov ecx, 10
    div rcx

    push rdx
    inc r9

    test rax, rax
    jnz .peel_digits

.write_digits:
    pop rdi
    call itoa_digit

    mov byte ptr [rsi], al
    inc rsi
    inc r8

    dec r9
    jnz .write_digits

.done_itoa:
    mov byte ptr [rsi], 0
    mov rax, r8
    ret

atoi_digit:
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x2d
    je neg_num_check
    sub rdx, '0'
    mov rax, rdx
    ret
    neg_num_check:
        inc rdi
        mov r8, 1 # 1 if negative
        movzx rdx, byte ptr [rdi]
        sub rdx, 0x30
        mov rax, rdx
        ret
atoi:
    xor r8, r8
    call atoi_digit
    loop:
    inc rdi
    movzx rdx, byte ptr [rdi]
    sub rdx, '0'
    cmp rdx, 9
    ja done
    mov rcx, rax
    imul rcx, 10
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x0
    je null_byte
    call atoi_digit
    add rcx, rax
    mov rax, rcx
    jmp loop
null_byte:
    cmp r8, 1
    je neg_rax
    ret
done:
    cmp r8, 1
    je neg_rax
    ret
neg_rax:
    neg rax
    ret


```

##### String Markers
```
.intel_syntax noprefix
.global itoa_digit
.global itoa
.global atoi_digit
.global atoi
.global _start

_start:
    mov r14, rsp           # original rsp

    mov rdi, [r14+16]      # argv[1]
    sub rsp, 0x100
    mov rsi, rsp            # output buffer
    mov r15, 24

    xor rdx, rdx            # input index
    xor rcx, rcx            # output index

filter_loop:
    cmp BYTE PTR [rdi + rdx], 0
    je write_data

    cmp BYTE PTR [rdi + rdx], 0x5c     # '\'
    je slash
    cmp BYTE PTR [rdi + rdx], 0x25     # '%'
    je percent

    # normal character
    mov al, BYTE PTR [rdi + rdx]
    mov BYTE PTR [rsi + rcx], al
    inc rdx
    inc rcx
    jmp filter_loop

slash:
    inc rdx
    cmp BYTE PTR [rdi + rdx], 'n'
    je new_line
    cmp BYTE PTR [rdi + rdx], 0x5c
    je double_slash

    # regular backslash
    mov BYTE PTR [rsi + rcx], 0x5c
    inc rcx
    jmp filter_loop

percent:
    inc rdx
    cmp BYTE PTR [rdi + rdx], '%'
    je double_percent
    cmp BYTE PTR [rdi + rdx], 'd'
    je decimal_marker

    # regular percent
    mov BYTE PTR [rsi + rcx], 0x25
    inc rcx
    jmp filter_loop

new_line:
    mov BYTE PTR [rsi + rcx], 0x0a
    inc rdx
    inc rcx
    jmp filter_loop

double_slash:
    mov BYTE PTR [rsi + rcx], 0x5c
    inc rdx
    inc rcx
    jmp filter_loop
    
double_percent:
    mov BYTE PTR [rsi + rcx], 0x25
    inc rdx
    inc rcx
    jmp filter_loop

decimal_marker:
    push rdi
    push rdx
    push rcx
    push rsi

    mov rdi, [r14+r15]      # current %d argument
    add r15, 8              # advance to next argument

    call atoi

    mov rdi, rax

    mov rcx, [rsp+8]        # output index
    mov rsi, [rsp]          # output buffer
    add rsi, rcx

    call itoa
    mov r8, rax             # length

    pop rsi
    pop rcx
    pop rdx
    pop rdi

    add rcx, r8             # output index += converted length
    inc rdx                  # skip 'd'
    jmp filter_loop

string_marker:
    mov r8, [r14+r15]       # r8 = pointer to string argument
    add r15, 8              # consume this argv

.copy_string:
    cmp BYTE PTR [r8], 0
    je .string_done

    mov al, BYTE PTR [r8]
    mov BYTE PTR [rsi+rcx], al

    inc r8
    inc rcx
    jmp .copy_string

.string_done:
    inc rdx                 # skip 's'
    jmp filter_loop

write_data:
    mov rdx, rcx
    mov rdi, 1
    mov rax, 1
    syscall

    mov rdi, 0
    mov rax, 60
    syscall



itoa_digit:
    mov rax, rdi
    add rax, '0'
    ret

itoa:
    mov rax, rdi
    xor r8, r8
    xor r9, r9

    test rax, rax
    jns .magnitude_ready

.is_negative:
    mov byte ptr [rsi], '-'
    inc rsi
    inc r8
    neg rax

.magnitude_ready:
    test rax, rax
    jnz .peel_digits
    mov byte ptr [rsi], '0'
    inc r8
    mov rax, r8
    ret

.peel_digits:
    xor rdx, rdx
    mov ecx, 10
    div rcx

    push rdx
    inc r9

    test rax, rax
    jnz .peel_digits

.write_digits:
    pop rdi
    call itoa_digit

    mov byte ptr [rsi], al
    inc rsi
    inc r8

    dec r9
    jnz .write_digits

.done_itoa:
    mov byte ptr [rsi], 0
    mov rax, r8
    ret

atoi_digit:
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x2d
    je neg_num_check
    sub rdx, '0'
    mov rax, rdx
    ret
    neg_num_check:
        inc rdi
        mov r8, 1 # 1 if negative
        movzx rdx, byte ptr [rdi]
        sub rdx, 0x30
        mov rax, rdx
        ret
atoi:
    xor r8, r8
    call atoi_digit
    loop:
    inc rdi
    movzx rdx, byte ptr [rdi]
    sub rdx, '0'
    cmp rdx, 9
    ja done
    mov rcx, rax
    imul rcx, 10
    movzx rdx, byte ptr [rdi]
    cmp rdx, 0x0
    je null_byte
    call atoi_digit
    add rcx, rax
    mov rax, rcx
    jmp loop
null_byte:
    cmp r8, 1
    je neg_rax
    ret
done:
    cmp r8, 1
    je neg_rax
    ret
neg_rax:
    neg rax
    ret


```

##### Hex Byte Escape
Imma be honest, because the chances of someone else reading it is quite low, I am using AI for this now. Yes, I cannot do it by myself. I feel like its quite useless now. I know its bad. I just want to move on from this.

```
.intel_syntax noprefix

.global itoa_digit
.global itoa
.global atoi_digit
.global atoi
.global _start


_start:
    mov r14, rsp                  # original rsp

    mov rdi, [r14+16]             # argv[1] = format string

    sub rsp, 0x100
    mov rsi, rsp                  # output buffer

    mov r15, 24                   # argv[2] = first extra argument

    xor rdx, rdx                  # format index
    xor rcx, rcx                  # output index


filter_loop:
    cmp BYTE PTR [rdi + rdx], 0
    je write_data

    cmp BYTE PTR [rdi + rdx], 0x5c        # '\'
    je slash

    cmp BYTE PTR [rdi + rdx], 0x25        # '%'
    je percent

    # normal character
    mov al, BYTE PTR [rdi + rdx]
    mov BYTE PTR [rsi + rcx], al
    inc rdx
    inc rcx
    jmp filter_loop


# --------------------------------------------------
# '\' escapes
# --------------------------------------------------

slash:
    inc rdx

    cmp BYTE PTR [rdi + rdx], 'n'
    je new_line

    cmp BYTE PTR [rdi + rdx], 0x5c        # '\\'
    je double_slash

    cmp BYTE PTR [rdi + rdx], 'x'
    je hex_escape

    # Unknown escape: keep the '\'
    mov BYTE PTR [rsi + rcx], 0x5c
    inc rcx
    jmp filter_loop


new_line:
    mov BYTE PTR [rsi + rcx], 0x0a
    inc rdx
    inc rcx
    jmp filter_loop


double_slash:
    mov BYTE PTR [rsi + rcx], 0x5c
    inc rdx
    inc rcx
    jmp filter_loop


# --------------------------------------------------
# \xNN
# --------------------------------------------------

hex_escape:
    # rdx points to 'x'
    inc rdx                           # first hex digit

    # -------------------------
    # First hex digit
    # -------------------------
    movzx r8, BYTE PTR [rdi + rdx]

    cmp r8, '0'
    jb hex_first_upper
    cmp r8, '9'
    jbe hex_first_digit

hex_first_upper:
    cmp r8, 'A'
    jb hex_first_lower
    cmp r8, 'F'
    jbe hex_first_uppercase

hex_first_lower:
    sub r8, 'a'
    add r8, 10
    jmp hex_first_done

hex_first_uppercase:
    sub r8, 'A'
    add r8, 10
    jmp hex_first_done

hex_first_digit:
    sub r8, '0'

hex_first_done:
    shl r8, 4                         # first nibble -> high 4 bits

    # -------------------------
    # Second hex digit
    # -------------------------
    inc rdx
    movzx r9, BYTE PTR [rdi + rdx]

    cmp r9, '0'
    jb hex_second_upper
    cmp r9, '9'
    jbe hex_second_digit

hex_second_upper:
    cmp r9, 'A'
    jb hex_second_lower
    cmp r9, 'F'
    jbe hex_second_uppercase

hex_second_lower:
    sub r9, 'a'
    add r9, 10
    jmp hex_second_done

hex_second_uppercase:
    sub r9, 'A'
    add r9, 10
    jmp hex_second_done

hex_second_digit:
    sub r9, '0'

hex_second_done:
    or r8, r9                         # combine the two nibbles

    mov BYTE PTR [rsi + rcx], r8b
    inc rcx

    inc rdx                           # move past second hex digit
    jmp filter_loop


# --------------------------------------------------
# '%' markers
# --------------------------------------------------

percent:
    inc rdx                           # points after '%'

    cmp BYTE PTR [rdi + rdx], '%'
    je double_percent

    cmp BYTE PTR [rdi + rdx], 'd'
    je decimal_marker

    cmp BYTE PTR [rdi + rdx], 's'
    je string_marker

    # Unknown marker: keep '%'
    mov BYTE PTR [rsi + rcx], 0x25
    inc rcx
    jmp filter_loop


double_percent:
    mov BYTE PTR [rsi + rcx], 0x25
    inc rdx                           # skip second '%'
    inc rcx
    jmp filter_loop


# --------------------------------------------------
# %d
# --------------------------------------------------

decimal_marker:
    # Save current state
    push rdi
    push rdx
    push rcx
    push rsi

    # Get next argv
    mov rdi, [r14 + r15]
    add r15, 8

    call atoi                         # rax = integer

    mov rdi, rax

    # Restore output position
    mov rcx, [rsp + 8]
    mov rsi, [rsp]
    add rsi, rcx

    call itoa                         # rax = number of bytes written
    mov r10, rax                      # save length

    pop rsi
    pop rcx
    pop rdx
    pop rdi

    add rcx, r10                      # advance output index
    inc rdx                           # skip 'd'
    jmp filter_loop


# --------------------------------------------------
# %s
# --------------------------------------------------

string_marker:
    mov r8, [r14 + r15]               # next argv string
    add r15, 8                        # consume argument

.copy_string:
    cmp BYTE PTR [r8], 0
    je .string_done

    mov al, BYTE PTR [r8]
    mov BYTE PTR [rsi + rcx], al

    inc r8
    inc rcx
    jmp .copy_string

.string_done:
    inc rdx                           # skip 's'
    jmp filter_loop


# --------------------------------------------------
# write output
# --------------------------------------------------

write_data:
    mov rdx, rcx                      # output length
    mov rdi, 1                        # stdout
    mov rax, 1                        # write
    syscall

    xor rdi, rdi
    mov rax, 60                       # exit
    syscall


# ==================================================
# itoa
# ==================================================

itoa_digit:
    mov rax, rdi
    add rax, '0'
    ret


itoa:
    mov rax, rdi
    xor r8, r8                        # output length
    xor r9, r9                        # digit count

    test rax, rax
    jns .magnitude_ready

    mov BYTE PTR [rsi], '-'
    inc rsi
    inc r8
    neg rax

.magnitude_ready:
    test rax, rax
    jnz .peel_digits

    mov BYTE PTR [rsi], '0'
    inc r8
    mov rax, r8
    ret

.peel_digits:
    xor rdx, rdx
    mov ecx, 10
    div rcx

    push rdx
    inc r9

    test rax, rax
    jnz .peel_digits

.write_digits:
    pop rdi
    call itoa_digit

    mov BYTE PTR [rsi], al
    inc rsi
    inc r8

    dec r9
    jnz .write_digits

.done_itoa:
    mov BYTE PTR [rsi], 0
    mov rax, r8
    ret


# ==================================================
# atoi
# ==================================================

atoi_digit:
    movzx rax, BYTE PTR [rdi]
    sub rax, '0'
    ret


atoi:
    xor rax, rax                     # result
    xor r8, r8                       # negative flag

    cmp BYTE PTR [rdi], '-'
    jne .atoi_loop

    mov r8, 1
    inc rdi

.atoi_loop:
    movzx rcx, BYTE PTR [rdi]

    cmp rcx, '0'
    jb .atoi_done

    cmp rcx, '9'
    ja .atoi_done

    sub rcx, '0'
    imul rax, rax, 10
    add rax, rcx

    inc rdi
    jmp .atoi_loop

.atoi_done:
    test r8, r8
    jz .atoi_return

    neg rax

.atoi_return:
    ret
```

## Debugging Refresher
##### Setting Breakpoints
```
(gdb) run
Starting program: /challenge/embryogdb_level4 
Warning:
Cannot insert breakpoint 3.
Cannot access memory at address 0x5bd6dd122d4e

(gdb) info break
Num     Type           Disp Enb Address            What
3       breakpoint     keep y   0x00005bd6dd122d4e 
(gdb) delete 3
(gdb) b *main+593
Breakpoint 4 at 0x5f169907bd02
(gdb) c
Continuing.
###
### Welcome to /challenge/embryogdb_level4!
###

GDB is a very powerful dynamic analysis tool which you can use in order to understand the state of a program throughout
its execution. You will become familiar with some of gdb's capabilities in this module.

A critical part of dynamic analysis is getting your program to the state you are interested in analyzing. So far, these
challenges have automatically set breakpoints for you to pause execution at states you may be interested in analyzing.
It is important to be able to do this yourself.

There are a number of ways to move forward in the program's execution. You can use the `stepi <n>` command, or `si <n>`
for short, in order to step forward one instruction. You can use the `nexti <n>` command, or `ni <n>` for short, in
order to step forward one instruction, while stepping over any function calls. The `<n>` parameter is optional, but
allows you to perform multiple steps at once. You can use the `finish` command in order to finish the currently
executing function. You can use the `break *<address>` parameterized command in order to set a breakpoint at the
specified-address. You have already used the `continue` command, which will continue execution until the program hits a
breakpoint.

While stepping through a program, you may find it useful to have some values displayed to you at all times. There are
multiple ways to do this. The simplest way is to use the `display/<n><u><f>` parameterized command, which follows
exactly the same format as the `x/<n><u><f>` parameterized command. For example, `display/8i $rip` will always show you
the next 8 instructions. On the other hand, `display/4gx $rsp` will always show you the first 4 values on the stack.
Another option is to use the `layout regs` command. This will put gdb into its TUI mode and show you the contents of all
of the registers, as well as nearby instructions.

In order to solve this level, you must figure out a series of random values which will be placed on the stack. You are
highly encouraged to try using combinations of `stepi`, `nexti`, `break`, `continue`, and `finish` to make sure you have
a good internal understanding of these commands. The commands are all absolutely critical to navigating a program's
execution.


Program received signal SIGTRAP, Trace/breakpoint trap.
0x00005f169907bca4 in main ()
(gdb) x/8gx $rbp-0x18
0x7ffe09e99d58: 0x0000000000000000      0x0000000000000000
0x7ffe09e99d68: 0xcea36c12e3337600      0x00007ffe09e99e10
0x7ffe09e99d78: 0x00007a5f3111e1ca      0x0000000000000000
0x7ffe09e99d88: 0x00007ffe09e99e98      0x0000000100000000
(gdb) c
Continuing.
The random value has been set!

Random value: 
Breakpoint 4, 0x00005f169907bd02 in main ()
(gdb) x/8gx $rbp-0x18
0x7ffe09e99d58: 0x244e0ff0b2433f62      0x0000000000000000
0x7ffe09e99d68: 0xcea36c12e3337600      0x00007ffe09e99e10
0x7ffe09e99d78: 0x00007a5f3111e1ca      0x0000000000000000
0x7ffe09e99d88: 0x00007ffe09e99e98      0x0000000100000000
(gdb) c
Continuing.

c
You input: c
The correct answer is: 244e0ff0b2433f62
[Inferior 1 (process 13020) exited with code 01]
(gdb) kill
The program is not being run.
(gdb) run
Starting program: /challenge/embryogdb_level4 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
###
### Welcome to /challenge/embryogdb_level4!
###

GDB is a very powerful dynamic analysis tool which you can use in order to understand the state of a program throughout
its execution. You will become familiar with some of gdb's capabilities in this module.

A critical part of dynamic analysis is getting your program to the state you are interested in analyzing. So far, these
challenges have automatically set breakpoints for you to pause execution at states you may be interested in analyzing.
It is important to be able to do this yourself.

There are a number of ways to move forward in the program's execution. You can use the `stepi <n>` command, or `si <n>`
for short, in order to step forward one instruction. You can use the `nexti <n>` command, or `ni <n>` for short, in
order to step forward one instruction, while stepping over any function calls. The `<n>` parameter is optional, but
allows you to perform multiple steps at once. You can use the `finish` command in order to finish the currently
executing function. You can use the `break *<address>` parameterized command in order to set a breakpoint at the
specified-address. You have already used the `continue` command, which will continue execution until the program hits a
breakpoint.

While stepping through a program, you may find it useful to have some values displayed to you at all times. There are
multiple ways to do this. The simplest way is to use the `display/<n><u><f>` parameterized command, which follows
exactly the same format as the `x/<n><u><f>` parameterized command. For example, `display/8i $rip` will always show you
the next 8 instructions. On the other hand, `display/4gx $rsp` will always show you the first 4 values on the stack.
Another option is to use the `layout regs` command. This will put gdb into its TUI mode and show you the contents of all
of the registers, as well as nearby instructions.

In order to solve this level, you must figure out a series of random values which will be placed on the stack. You are
highly encouraged to try using combinations of `stepi`, `nexti`, `break`, `continue`, and `finish` to make sure you have
a good internal understanding of these commands. The commands are all absolutely critical to navigating a program's
execution.


Program received signal SIGTRAP, Trace/breakpoint trap.
0x00005df6d7e7bca4 in main ()
(gdb) info break
Num     Type           Disp Enb Address            What
4       breakpoint     keep y   0x00005df6d7e7bd02 <main+593>
(gdb) delete 4
(gdb) b *main+593
Breakpoint 5 at 0x5df6d7e7bd02
(gdb) x/8gx $rbp-0x18
0x7ffc43fad708: 0x0000000000000000      0x0000000000000000
0x7ffc43fad718: 0xfcadd8da2bbd3500      0x00007ffc43fad7c0
0x7ffc43fad728: 0x000079b60c48f1ca      0x0000000000000000
0x7ffc43fad738: 0x00007ffc43fad848      0x0000000100000000
(gdb) c
Continuing.
The random value has been set!

Random value: 
Breakpoint 5, 0x00005df6d7e7bd02 in main ()
(gdb) x/8gx $rbp-0x18
0x7ffc43fad708: 0x354455671d2552a5      0x0000000000000000
0x7ffc43fad718: 0xfcadd8da2bbd3500      0x00007ffc43fad7c0
0x7ffc43fad728: 0x000079b60c48f1ca      0x0000000000000000
0x7ffc43fad738: 0x00007ffc43fad848      0x0000000100000000
(gdb) c
Continuing.
0x354455671d2552a5
You input: 354455671d2552a5
The correct answer is: 354455671d2552a5
The random value has been set!

Random value: 
Breakpoint 5, 0x00005df6d7e7bd02 in main ()
(gdb) x/8gx $rbp-0x18
0x7ffc43fad708: 0x61f01f2febd8ef2d      0x354455671d2552a5
0x7ffc43fad718: 0xfcadd8da2bbd3500      0x00007ffc43fad7c0
0x7ffc43fad728: 0x000079b60c48f1ca      0x0000000000000000
0x7ffc43fad738: 0x00007ffc43fad848      0x0000000100000000
(gdb) c
Continuing.
0x61f01f2febd8ef2d
You input: 61f01f2febd8ef2d
The correct answer is: 61f01f2febd8ef2d
The random value has been set!

Random value: 
Breakpoint 5, 0x00005df6d7e7bd02 in main ()
(gdb) x/8gx $rbp-0x18
0x7ffc43fad708: 0x8bb5c4e6cb42f3f8      0x61f01f2febd8ef2d
0x7ffc43fad718: 0xfcadd8da2bbd3500      0x00007ffc43fad7c0
0x7ffc43fad728: 0x000079b60c48f1ca      0x0000000000000000
0x7ffc43fad738: 0x00007ffc43fad848      0x0000000100000000
(gdb) c
Continuing.
0x8bb5c4e6cb42f3f8
You input: 8bb5c4e6cb42f3f8
The correct answer is: 8bb5c4e6cb42f3f8
The random value has been set!

Random value: 
Breakpoint 5, 0x00005df6d7e7bd02 in main ()
(gdb) x/8gx $rbp-0x18
0x7ffc43fad708: 0xee875c62be1fa6d0      0x8bb5c4e6cb42f3f8
0x7ffc43fad718: 0xfcadd8da2bbd3500      0x00007ffc43fad7c0
0x7ffc43fad728: 0x000079b60c48f1ca      0x0000000000000000
0x7ffc43fad738: 0x00007ffc43fad848      0x0000000100000000
(gdb) c
Continuing.
0xee875c62be1fa6d0
You input: ee875c62be1fa6d0
The correct answer is: ee875c62be1fa6d0
You win! Here is your flag:
pwn.college{wY95WkIw1Wk1DAtUqq-uoqoOzy6.ddDNywSM3QDN3EzW}


### Goodbye!
```
I didnt have any clue what the code meant. I use Chat to decipher it.


##### GDB Scripting
```
ubuntu@debugging-refresher~gdb-scripting:~/Numbers_As_Strings$ /challenge/embryogdb_level5 
The program is restarting under the control of gdb! You can run the program with the gdb command `run`.

GNU gdb (Ubuntu 15.1-1ubuntu1~24.04.1) 15.1
Copyright (C) 2024 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from /challenge/embryogdb_level5...

--Type <RET> for more, q to quit, c to continue without paging--c
This GDB supports auto-downloading debuginfo from the following URLs:
  <https://debuginfod.ubuntu.com>
Enable debuginfod for this session? (y or [n]) n
Debuginfod has been disabled.
To make this setting permanent, add 'set debuginfod enabled off' to .gdbinit.
(No debugging symbols found in /challenge/embryogdb_level5)
(gdb) starti
Starting program: /challenge/embryogdb_level5 

Program stopped.
0x00007d80d8067540 in _start () from /lib64/ld-linux-x86-64.so.2
(gdb) source /home/hacker/Numbers_As_Strings/GDB_Scripting.gdb
Breakpoint 1 at 0x58f3aa50bde8
(gdb) c
Continuing.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
###
### Welcome to /challenge/embryogdb_level5!
###

GDB is a very powerful dynamic analysis tool which you can use in order to understand the state of a program throughout
its execution. You will become familiar with some of gdb's capabilities in this module.

We write code in order to express an idea which can be reproduced and refined. We can think of our analysis as a program
which injests the target to be analyzed as data. As the saying goes, code is data and data is code.

While using gdb interactively as we've done with the past levels is incredibly powerful, another powerful tool is gdb
scripting. By scripting gdb, you can very quickly create a custom-tailored program analysis tool. If you know how to
interact with gdb, you already know how to write a gdb script--the syntax is exactly the same. You can write your
commands to some file, for example `x.gdb`, and then launch gdb using the flag `-x <PATH_TO_SCRIPT>`. This file will
execute all of the gdb commands after gdb launches. Alternatively, you can execute individual commands with `-ex
'<COMMAND>'`. You can pass multiple commands with multiple `-ex` arguments. Finally, you can have some commands be
always executed for any gdb session by putting them in `~/.gdbinit`. You probably want to put `set disassembly-flavor
intel` in there.

Within gdb scripting, a very powerful construct is breakpoint commands. Consider the following gdb script:

  start
  break *main+42
  commands
    x/gx $rbp-0x32
    continue
  end
  continue

In this case, whenever we hit the instruction at `main+42`, we will output a particular local variable and then continue
execution.

Now consider a similar, but slightly more advanced script using some commands you haven't yet seen:

  start
  break *main+42
  commands
    silent
    set $local_variable = *(unsigned long long*)($rbp-0x32)
    printf "Current value: %llx\n", $local_variable
    continue
  end
  continue

In this case, the `silent` indicates that we want gdb to not report that we have hit a breakpoint, to make the output a
bit cleaner. Then we use the `set` command to define a variable within our gdb session, whose value is our local
variable. Finally, we output the current value using a formatted string.

Use gdb scripting to help you collect the random values.


Program received signal SIGTRAP, Trace/breakpoint trap.
0x000058f3aa50bd94 in main ()
(gdb) c
Continuing.
The random value has been set!

Current value: eeadac9f45a97b91
Random value: eeadac9f45a97b91                                 
You input: eeadac9f45a97b91
The correct answer is: eeadac9f45a97b91
The random value has been set!

Current value: cd725db3e803b328
Random value: cd725db3e803b328
You input: cd725db3e803b328
The correct answer is: cd725db3e803b328
The random value has been set!

Current value: c8b43d0931a5c7a1
Random value: c8b43d0931a5c7a1
You input: c8b43d0931a5c7a1
The correct answer is: c8b43d0931a5c7a1
The random value has been set!

Current value: d7067b2378c56584
Random value: d7067b2378c56584
You input: d7067b2378c56584
The correct answer is: d7067b2378c56584
The random value has been set!

Current value: b86d04ae0025b91c
Random value: b86d04ae0025b91c
You input: b86d04ae0025b91c
The correct answer is: b86d04ae0025b91c
The random value has been set!

Current value: 34c6fe3c7a443599
Random value: 34c6fe3c7a443599
You input: 34c6fe3c7a443599
The correct answer is: 34c6fe3c7a443599
The random value has been set!

Current value: abff1318be53a641
Random value: abff1318be53a641
You input: abff1318be53a641
The correct answer is: abff1318be53a641
The random value has been set!

Current value: ef47c054b173635f
Random value: ef47c054b173635f
You input: ef47c054b173635f
The correct answer is: ef47c054b173635f
You win! Here is your flag:
pwn.college{4SxyppPrGah4RfpaKG7d92nR98x.dhDNywSM3QDN3EzW}


### Goodbye!
```

```
set disassembly-flavor intel

break *main+823
commands
  silent
  set $local_variable = *(unsigned long long*)($rbp-0x18)
  printf "Current value: %llx\n", $local_variable
  continue
end
```

##### Modifying Data
```
set disassembly-flavor intel

break *main+757
commands
    silent
    set $rdx = $rax
    continue
end
```
This worked, but not exacly as I wanted or expected.
##### Modifying Execution
```
(gdb) c
Continuing.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
###
### Welcome to /challenge/embryogdb_level7!
###

GDB is a very powerful dynamic analysis tool which you can use in order to understand the state of a program throughout
its execution. You will become familiar with some of gdb's capabilities in this module.

As we demonstrated in the previous level, gdb has FULL control over the target process. Under normal circumstances, gdb
running as your regular user cannot attach to a privileged process. This is why gdb isn't a massive security issue which
would allow you to just immediately solve all the levels. Nevertheless, gdb is still an extremely powerful tool.

Running within this elevated instance of gdb gives you elevated control over the entire system. To clearly demonstrate
this, see what happens when you run the command `call (void)win()`.

As it turns out, all of the levels other levels in module could be solved in this way.

GDB is very powerful!


Program received signal SIGTRAP, Trace/breakpoint trap.
0x000064f6d1fb6bc1 in main ()
(gdb) call (void)win()
You win! Here is your flag:
pwn.college{AiX-NH1EFlTqo2ptSp7Prtap0PF.dBTNywSM3QDN3EzW}


```

##### Broken Function
```
(gdb) run
Starting program: /challenge/embryogdb_level8 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
###
### Welcome to /challenge/embryogdb_level8!
###

GDB is a very powerful dynamic analysis tool which you can use in order to understand the state of a program throughout
its execution. You will become familiar with some of gdb's capabilities in this module.

As we demonstrated in the previous level, gdb has FULL control over the target process. Under normal circumstances, gdb
running as your regular user cannot attach to a privileged process. This is why gdb isn't a massive security issue which
would allow you to just immediately solve all the levels. Nevertheless, gdb is still an extremely powerful tool.

Running within this elevated instance of gdb gives you elevated control over the entire system. To clearly demonstrate
this, see what happens when you run the command `call (void)win()`.

Note that this will _not_ get you the flag (it seems that we broke the win function!), so you'll need to work a bit
harder to get this flag!

As it turns out, all of the levels other levels in module could be solved in this way.

GDB is very powerful!


Program received signal SIGTRAP, Trace/breakpoint trap.
0x00005b7833f7ebfa in main ()
(gdb) call (void) win()

Breakpoint 1, 0x00005b7833f7e96b in win ()
The program being debugged stopped while in a function called from GDB.
Evaluation of the expression containing the function
(win) will be abandoned.
When the function is done executing, GDB will silently stop.
(gdb) x/i $rip
=> 0x5b7833f7e96b <win+8>:      sub    $0x10,%rsp
(gdb) push %rbp
Undefined command: "push".  Try "help".
(gdb) set $rip = win+35
(gdb) x/i $rip
=> 0x5b7833f7e986 <win+35>:     lea    0x744(%rip),%rax        # 0x5b7833f7f0d1
(gdb) c
Continuing.
You win! Here is your flag:
pwn.college{kProVod1auHfASbLDVx-Rzygz5k.QX5MzMzwSM3QDN3EzW}


(gdb) 
```

I DONT KNOW!

## Building A Web Server