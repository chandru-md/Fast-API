"""
for loop and while loop
"""

my_list = [1,2,3,4,5]

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])

print('*'*50)

for i in my_list:
    print(i)

for i in range(3,6):
    print(i)

print('+'*50)


sum_of_for_loop = 0

for x in my_list:
    sum_of_for_loop = sum_of_for_loop + x
print(sum_of_for_loop)

mylist = ['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
for i in mylist:
    print(f"Happy {i}!!!")


i = 0

while i < 10:
    i = i + 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print('i is now larger or equal to 5')