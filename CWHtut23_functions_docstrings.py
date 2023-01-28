# a = 9
# b = 2
# c = sum((a, b))   #built in function
# print(c)

def function1(a, b):
    print("hello you are in function1", a + b)


def function2(a, b):
    """this is a function which will calculate average"""
    average = (a + b) / 2
    print(average)
    return average


# print(function1())
# v = function2(5, 6)
# print(v)

print(function2.__doc__)
