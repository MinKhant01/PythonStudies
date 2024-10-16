with open('example.txt','r') as file:
    line = file.readline()
    while(line):
        print(line, end='')
        line = file.readline()
    print()

with open("example.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:  # Check for end-of-file
            break
        print(line, end='')


with open('example.txt','r') as file:
    content = file.read()
print(content)

with open('example.txt','r') as file:
    arr = file.readlines()
print(arr)

"""
METHODS FOR READING
read()
read([byte_size])
readline()
readlines()
"""

"""
METHODS FOR WRITING
write([string])
writelines([list])
"""

with open('example.txt','r') as file:
    #items = file.readlines()        #returns ['line1\n', 'line2\n', 'line3\n', 'line4']
    content = file.read()            #returns ['line1', 'line2', 'line3', 'line4']
    items = content.split()
    print(items)

data = ['apple', 'banana', 'cherry']
with open('data.txt','w') as file:
    file.write(','.join(data))