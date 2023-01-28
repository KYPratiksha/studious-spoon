mystr= "Harry is a good boy"

print(mystr[4])           #4th indexed character

print(mystr[0:4])         #0-4th character

print(len(mystr))

print(mystr[0:5:2])
print(mystr[::4])

print(mystr[::-1])        #reverse the string

print(mystr.isalnum())    #checks alphanumeric in string
print(mystr.endswith("boy"))      #checks if string ends with boy
print(mystr.count("o"))     #counts number of o characters in string
print(mystr.capitalize())         #capitalises first letter
print(mystr.find("good"))
print(mystr.lower())
print(mystr.upper())          #convert whole string to uppercase
print(mystr.replace("is","are"))