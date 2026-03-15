"""
create a list of 5 animals called zoo
delete the animal at the 3rd index
append a new animal at the end of the list
delete the animal at the beginning of the lisr
print all the animal
print only the first 3 animals
"""


zoo = ['Lion','tiger','leopard','cheetah','elephant']
print(zoo)

zoo.pop(3)
print(zoo)

zoo.append('Lokesh')
print(zoo)

zoo.remove("tiger")
print(zoo)

print(zoo)

print(zoo[:3])
