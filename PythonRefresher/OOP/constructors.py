"""
what are constructors?

constructors are used to create and initialize an object of a class with or without starting values.

different types of constructors

default or empty constructors
No arguments constructors
parameter constructors

1.
self = refers to the  current class or object
---- automatically created if no constructor is found

2.
in this , no starting values

3.
parameters constructors
in that we have pass the name like--- (enemy = Enemy("Chandru"))
"""
from Enemy import *

enemy = Enemy()

enemy.type_of_enemy = "Kavitha"

enemy.talk()

enemy.walk_forward()

enemy.attack()