# 45 * 3=555 , 56+9 = 77, 56/6=4

a= int(input("enter first number:"))
b = int(input("enter second number:"))
c = input("enter an operater +,-,*,/:")

if a == 45 and b == 3 and c == '*':
    print("555")
elif a == 56 and b == 9 and c== '+':
    print("77")
elif a == 56 and b == 6 and c == '/':
    print("4")
elif c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
elif c == '/':
    print(a/b)
else:
    print("invalid input")
