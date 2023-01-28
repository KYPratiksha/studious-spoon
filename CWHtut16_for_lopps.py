# list1 = [["harry",1], ["larry",2], ["carry",56], ["marie",34] ]
#
# dict1 = dict(list1)
# print(dict1)
# for item in list1:
#     print(item)

# for item in dict1.items():
#     print(item)

# for item in dict1:
#     print(item)

list = [1,4,"marie", 89,56,"kolkata",12]

# if(list[i] == type(int)):
for i in list:
    if str(i).isnumeric() and i>6:
        print(i)
