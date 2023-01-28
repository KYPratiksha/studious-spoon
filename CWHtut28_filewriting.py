f = open("Harry.txt", "a")
# f.write("Harry is good coder")
a = f.write("Harry is good coder\n")
print(a)    # return number of characters
f.close()
#
# f = open("Harry.txt", "w")
# # f.write("Harry is good coder")
# a = f.write("Harry is good coder")
# print(a)    # return number of characters
# f.close()

#handle read and write
f = open("Harry.txt", "r+")
print(f.read())
f.write("thank you")