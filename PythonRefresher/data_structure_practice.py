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

print('='*50)

numbers = [10, 45, 23, 89, 67]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest:", largest)

numbers = [10, 45, 23, 89, 67]

largest = max(numbers)

print("Largest:", largest)

numbers = [10, 45, 23, 89, 67]

numbers.sort()
print("Largest:", numbers[-1])