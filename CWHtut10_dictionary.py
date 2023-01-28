d1={}
# print(type(d1))
d2={"harry":"burger", "rohan":"fish", "skillf":"roti", "shubham":{"b":"maggie","l":"roti","d":"chicken"}}
# print(d1)
# d2["ankit"]="junk food"
# # print(d2["shubham"]["b"])
# print(d2)
# print(d2["ankit"])
# d2["aurangzeb"] = "kababs"
# d2[345] = "rice"             #add 345 key
# del d2[345]            #delete 345 key
# print(d2)

d3=d2.copy()
print(d2)
del d3["harry"]     #deletes only from d3
print(d2)
print(d3)
print(d2.get("harry"))
d2.update({"leena":"toffee"})
print(d2)
print(d2.keys())      #prints keys
print(d2.items())