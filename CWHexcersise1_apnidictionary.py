dict = {"set":"collection of numbers", "mutable":"values can be changed","immutable":"values cant be changed","optimistic":"person who takes things positively"}
inp = input("enter the word you want to know:")
answer = dict.get(inp)
print("the meaning is:",answer)