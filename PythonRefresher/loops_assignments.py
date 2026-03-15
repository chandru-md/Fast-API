mylist = ['Monday','Tuesday','Wednesday','Thrusday','Friday']
x = 0

while x<3:
    x += 1
    for i in mylist:
        if i == "Monday":
            print("-"*20)
            continue
        print(i)