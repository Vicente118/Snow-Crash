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





