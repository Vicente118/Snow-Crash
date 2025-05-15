- We have a level13 ELF binary with SUID bit set.
- Let's get it on our machine and deceompile it:

```bash
> scp -P 4242 level13@192.168.56.101:/home/user/level13/level13 .

int32_t main(int32_t argc, char** argv, char** envp)
{
	if (getuid() == 4242)
	return printf("your token is %s\n", ft_des("boe]!ai0FB@.:|L6l@A?>qJ}I"));
       
    printf("UID %d started us but we we expe…", getuid(), 4242);
    exit(1);
}
```

- The program check if we are UID 4242 and decrypt this string "boe]!ai0FB@.:|L6l@A?>qJ}I" to print the flag.
- We just have to create a user with UID 4242 and run the program to get the flag.

```bash
> sudo groupadd -g 4242 attack
> sudo useradd attacker -u 4242  -m -s /bin/bash
> sudo passwd attacker

> ./level13
2A31L79asukciNyi8uppkEuSx
```