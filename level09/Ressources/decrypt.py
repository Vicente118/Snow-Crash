f = open("token", 'r', encoding = 'latin-1')
data = f.read()

result = ""

for i in range(len(data) - 1):
    result += chr(ord(data[i]) - i)

result += data[len(data) - 1]

print(result)