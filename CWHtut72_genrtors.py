"""
iterable - __iter__ or __getitem__
iterator - __next__
iteration


generators are  a type of iterator
"""
def gen(n):
    for i in range(n):
        yield i
g = gen(3456789123)
print(g)

#
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         yield n*fact(n-1)
#
#
# factorial  = fact(5)
# print(factorial)
#
#
#
# def fib(n):
#     if n == 0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         yield n+fib(n-1)
# num = fib(5)
# print(num)

n = "pratiksha"
it = iter(n)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

# n = 1234
# it = iter(n)
# print(it.__getitem__())