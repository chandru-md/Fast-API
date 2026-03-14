"""
String assignment we will do together:

ask the user how many days until their birthday
and print an approx number of weeks until their birthday

weeks is = 7 days

decimal within the return is allowed.
"""
# option 1

days  = input("How many days until your birthday? ")
print(type(days))
days = int(input("How many days until your birthday? "))
print(type(days))
print(days/7)

# option 2
user_name = input("Enter your name: ")
days = int(input("How many days before your birthday: "))
weeks = days // 7
print(f"Hi {user_name} only {weeks} weeks before your birthday.")