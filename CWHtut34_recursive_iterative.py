# def factorial(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i + 1)
#     return fac


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
#
#
# num = int(input("enter number:"))
# print(factorial(num))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("enter number till you want:"))
print(fibonacci(num))
