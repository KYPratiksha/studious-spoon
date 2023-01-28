# from typing import List
#
# ----------------MAP-------------
# # def sq(a):
# #     return a*a
# #
# # num= [2,3,4,5,6,7,8,9]
# # square = list(map(sq, num))
# # print(square)
#
#
# # num = [2,3,4,5,6,7,8,9]
# # square = list(map(lambda x:x*x, num))
# # print(square)
#
#
# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
#
# func = [square, cube]
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)

# map is used only with list and before comma is a function we use to apply and afte comma is the function on which we will apply on


#  -------------FILTER-------------
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# def is_greater_5(num):
#     return num >= 5
#
#
# greater_than_5 = list(filter(is_greater_5, list_1))
# print(greater_than_5)


# ----------------REDUCE----------
from functools import reduce

list1 = [2, 2, 3, 4, 6, 7, 2]

prod = reduce(lambda x, y: x * y, list1)
print(prod)
