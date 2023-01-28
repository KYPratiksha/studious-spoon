# input number of rows = integer n
# boolean = true or false
# true:
# *
# **
# ***
# ****
#
# false:
# ****
# ***
# **
# *

rows = int(input("enter number of rows :"))
t_f = int(input("enter 1 or 0 : "))
if t_f == 1:
    for i in range(0, rows):
        for j in range(1, rows+1):
            print("* "*j)
            # print("\n")
        break
elif t_f == 0:
    for i in range(0, rows):
        for j in range(rows, i, -1):
            print("* "*j)
        break
# else:
#     print("invalid input!")


