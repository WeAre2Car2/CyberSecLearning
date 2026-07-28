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


