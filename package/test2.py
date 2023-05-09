from module1 import math


print (math('Bidhan'))

# here math function is only imported from module.py so we can't print num
# print(num)

from module1 import num
# now num has been printed as we import num now
print (num)

# dir() returns a list of defined names in a namespace

print(dir())