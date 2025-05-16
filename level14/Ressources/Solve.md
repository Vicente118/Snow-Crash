- There is absolutly nothing in the file system that can be useful to elevate our privilege. (Binary, scripts, ...)
- Let's run the getflag binary into gdb
```bash
gdb /bin/getflag
> disas main

- We can see there is a call of ptrace that protect the user to run the program with an exeternal program like gdb or lldb.
- We can easily bypass this within the gdb command line.

> catch syscall ptrace
> commands 1
> set $eax=0
> continue
> end

- We also saw with disassembly that there is a call to getuid() to check if flag14 (uid=3014) is running the binary. Let's put a breakpoint at getuid call and modifify it's return value (Register EAX).

> b getuid
> run
- We are now at the function getuid(), let's step one more time to the end of the function. The return value of the function that correspond to the UID of the current user level14 will be stored in EAX register. Let's modify it manually to trick the program so he will think we hare flag14.

> print $eax
$1 = 2014  // This is level14 UID

> set $eax=3014 // Set EAX to 3014, UID of flag14
> step
Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
```