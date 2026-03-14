"""
string formatting in python
"""

first_name ="chandru"
print(first_name)

print("Welcome "+first_name)

print(f"Hello {first_name}")

last_name = "M D"
sentence = "{} {} started Fast API lectures from udemy business"
print(sentence.format(first_name, last_name))

print(f"Hi {first_name} {last_name} learning fast api from udemy")
