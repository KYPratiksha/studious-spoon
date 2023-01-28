f = open("Harry.txt")

print(f.tell())       #shows at which character file pointer is
print(f.readline())
print(f.tell())
f.seek(0)
print(f.readline())
print(f.tell())
f.close() 