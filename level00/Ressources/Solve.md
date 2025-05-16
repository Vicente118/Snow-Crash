HINT : FIND the file executable by level00 only.

```bash
> find / -user flag00 2>/dev/null
/usr/sbin/john

> cat /usr/bin/jhon

```

Now let's make a little python script to decrypt this password that looks to be encrypted with the Caesar method.

```python
def rot(code, x):
    str = ''
    for j in code:
        if ord(j) + x > 122:
            str += chr((ord(j) + x) % 122 + 97 - 1) 
        else:
            str += chr(ord(j) + x)
    return str


for i in range(26):
    print("Rotation of ", i, ": ", rot("cdiiddwpgswtgt", i))
```

We can see at the output that a rotation of 11 gives us the string : "nottohardhere"
Which is without a doubt the password of next user.

```bash
> su flag00

> getflag
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias
```

*x24ti5gi3x0ol2eh4esiuxias*