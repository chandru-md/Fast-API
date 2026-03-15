"""
If - else Statement - conditional statements
"""
x = 1

if x == 1:
    print("x is 1...")

print("if else statement")
print("Outside of the if statement")


print("="*50)

x = 2

if x == 1:
    print("x is 1...")

print("if else statement")
print("Outside of the if statement")

print("="*50)

x = 2

if x > 1:
    print("x is greater than one...")
else:
    print("x is not greater than one...")

print("if else statement")

print("="*50)

x = 1

if x > 1:
    print("x is greater than one...")
else:
    print("x is not greater than one...")

print("if else statement")
print("="*50)

hour = 13

if hour < 15:
    print("Good Morning!!!")
else:
    print("Goof Afternoon!!!")

print("="*50)

hour = 17

if hour < 15:
    print("Good Morning!!!")
else:
    print("Goof Afternoon!!!")

print("="*50)

hour = 21

if hour < 15:
    print("Good Morning!!!")
elif hour < 20:
    print("Goof Afternoon!!!")
else:
    print("Good Night!!!")