"""
"r" - open file for reading
"W" - open file for writing
"x" - creates file if not exists
"a" - add more content to a file
"t" - text mode  - default mode
"b" - binary mode
"+" - read and write
"""

f = open("Harry.txt", "rt")
# print(f.readline())     #reads only 1 line at a time
print(f.readlines())      #prints all lines in list

# content = f.read(355)
# print(content)

# for line in content:
#     print(line)

# for line in f:
#     print(line)

# content1 = f.read(355)
# print(content1)


f.close()
