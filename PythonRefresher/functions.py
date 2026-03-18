"""
Functions - user defined functions
 - built -in functions
"""

print("Hello and welcome to python programming!!")

def my_fun():
    print("Inside my function")


my_fun()

def print_my_name(name):
    print(f"Hello {name}!!!")

print_my_name("Chandru Deivanayagan")

def print_my_name(first_name,second_name):
    print(f"Hello {first_name} {second_name}!!!")

print_my_name("Sweety","Omana")

def print_red_color():
    color = 'red' # local variable
    print(color)


color = 'Blue' # global variable
print(color)
print_red_color()

def print_numbers(highest,lowest):
    print(highest)
    print(lowest)

print_numbers(10,3)

print_numbers(3,10)

print_numbers(lowest=3,highest=10)

def multiply(a,b):
    return a*b

print(multiply(5,5))

def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)

number_list = [1,2,3,4,5]
print_list(number_list)


def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)

def add_tax_to_item(cost_of_item):
    current_tax = 0.03
    return cost_of_item * current_tax

final_cost = buy_item(1000)
print(final_cost)