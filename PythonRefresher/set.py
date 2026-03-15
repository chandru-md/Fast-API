"""
Sets are similar to lists but are unordered and cannot duplications
use curly brackets
"""

my_set = {1,2,3,4,5,6,7,8,9,10,1,2,3,4,5}
print(my_set)


for x in my_set:
    print(x)

my_set.discard(10)
print(my_set)

my_set.add(10)
print(my_set)

my_set.update([11,12])
print(my_set)