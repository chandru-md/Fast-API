"""
Inheritance - Process of acquiring properities from one class to other classes.

Creates a hierarchy between classes

what is method over ride?
our animal eat() is pretty generic. what if we want to add our own dog eat()?

as we can see the last example, both dog() and animal() have the eat() functionality.

method overriding is when a child class has its own method already present in the parent class.

when the child class does not have the same method, it will default to the parent method.

SELF VS SUPER

self is used to refer to the current object that is created or being instantiated, while super is used to refer
to the parent class.

self is used when there is  a need to differentiate between the instance variables and parameters with the same
name, while super is used to call the parent class methods and /or constructors.


"""




class Animal: