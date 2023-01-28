# list comprehension
# ls = [i for i in range(100) if i%3==0]
# print(ls)


# -------------------------------
# dictionary comprehension
dict = {i:f"item {i}" for i in range(100) if i%3==0}

# to reverse the dict dictionary using python comprehension
dict = {value:key for key,value in dict.items()}
print(dict)


# ---------------------------------
# set comprehension
# d = {dress for dress in ["dress1","dress2","dress1","dress2"]}
# print(d)
# ---------------------------------
# generator comprehension
