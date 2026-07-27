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
