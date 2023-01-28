# num1 = input()
# num2 = input()
# try:
#     print("sum of these numbers are :", int(num1)+int(num2))
# except Exception as e:
#     print(e)
# print("this is running")
# ---------------------------------------------------------
# try, except, else syntax

# try:
#      # run this code
# except:
#      #  execute this code when there is an exception
# else:
     # no exception . Run this code
# finally:
    # this will run anyway


def divide(a,b):
    try :
        print(f"{a}/{b} is {a/b}")
    except ZeroDivisionError as z:
        print(z)
    else:
        print("No exception error")
    finally:
        print("this will run anyway")

num1 = int(input())
num2 = int(input())
divide(num1, num2)