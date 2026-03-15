"""
Function assignment

create a function that takes in 3 parameter (first name, last name, age) and returns
dictionary based on those values
"""
def user_data(first_name,last_name,age):
    created_user = {
        "first_name":first_name,
        "last_name":last_name,
        "age":age
    }
    return created_user

print(user_data("Lokesh",'Umamaheshwari ethirajan',25))