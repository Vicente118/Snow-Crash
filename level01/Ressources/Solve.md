
We can see that we are able to set what's in /etc/passwd

```bash
> cat /etc/passwd
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash

Here is a password : 42hDRfypTqqnw

> su flag01
Password: 
su: Authentication failure
```

---

Password seems to be encrypted
```bash
> john --wordlist=rockyou.txt password.txt

Password : abcdefg

> su flag01
> getflag
f2av5il02puano7naaf6adaaf
```

*f2av5il02puano7naaf6adaaf*
