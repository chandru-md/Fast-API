numbers = [10, 20, 30, 40]

total = 0
for num in numbers:
    total += num

print("Sum:", total)

numbers = [10, 20, 30, 40]

total = sum(numbers)

print("Sum:", total)

numbers = [10, 20, 30, 40]

i = 0
total = 0

while i < len(numbers):
    total += numbers[i]
    i += 1

print("Sum:", total)